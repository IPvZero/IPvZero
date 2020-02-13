from nornir import InitNornir
from nornir.plugins.functions.text import print_result, print_title
from nornir.plugins.tasks.networking import netmiko_send_config, netmiko_send_command
from nornir.core.filter import F

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

def ipvzero(task):
    task.run(task=netmiko_send_config, config_file= "config_textfile")
    task.run(task=netmiko_send_command, command_string = "show banner motd")

notactor = nr.filter(~F(groups__contains="actor"))
results = notactor.run(task = ipvzero)

print_title("DEPLOYING FILTERED CONFIGURATIONS")
print_result(results)
