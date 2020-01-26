from nornir import InitNornir
from nornir.plugins.tasks import networking, text
from nornir.plugins.functions.text import print_title, print_result

nr = InitNornir(config_file="config.yaml", dry_run=True)

def basic_configuration(task):
    # Transform inventory data to configuration via a template file
    r = task.run(task=text.template_file,
                 name="EIGRP Configuration",
                 template="eigrp.j2",
                 path=f"templates/{task.host['vendor']}")

    # Save the compiled configuration into a host variable
    task.host["config"] = r.result

    # Deploy that configuration to the device using NAPALM
    task.run(task=networking.napalm_configure,
             name="Loading Configuration on the device",
             replace=False,
             configuration=task.host["config"])

nr.data.dry_run = False
print_title("Runbook to configure the network")
result = nr.run(task=basic_configuration)
print_result(result)
