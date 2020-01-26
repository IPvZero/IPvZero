from nornir import InitNornir
from nornir.plugins.functions.text import print_result, print_title
from nornir.plugins.tasks.networking import netmiko_send_config, netmiko_send_command

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

def base(ipvzero):
    ipvzero.run(task=netmiko_send_config, config_file= "secure-copy")
    ipvzero.run(task=netmiko_send_command, command_string = "show run | sec ip scp")

results = nr.run(task = base)

print_title("ENABLING SECURE COPY FOR NAPALM")
print_result(results)
