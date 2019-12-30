from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
import colorama
from colorama import Fore, Style

print("\n")
print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
print(" " * 20 + "Welcome to " + Fore.RED + "Nornir!" + Style.RESET_ALL)
print(" " * 15 + "This is a Dynamic script!")
print("\n Please enter the commands you wish to execute, separated by commas")
print("Example: " + Fore.GREEN + "< show ip int brief, show ip route, show version >")
print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
commands = input ("\nEnter Commands: ")
cmds = commands.split(",")

for cmd in cmds:
    nr = InitNornir()

    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd
        )

    print_result(result)
