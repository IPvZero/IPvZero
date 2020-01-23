from nornir import InitNornir
from nornir.plugins.functions.text import print_result, print_title
from nornir.plugins.tasks.networking import netmiko_send_config, netmiko_send_command

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

def baseconfig(ipvzero):
    ipvzero.run(task=netmiko_send_config, config_file= "config_textfile")
    ipvzero.run(task=netmiko_send_command, command_string = "show banner motd")


targets = nr.filter(region="north")
results = targets.run(task = baseconfig)

print_title("DEPLOYING AUTOMATED BASELINE CONFIGURATIONS")
print_result(results)
