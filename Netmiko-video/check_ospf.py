from netmiko import ConnectHandler
import colorama
from colorama import Fore, Style


devices = '''
R1
R2
R3
R4
R5
R6
R7
R8
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'john'
password = 'cisco'
verbose = True

for device in devices:
        print(Fore.MAGENTA + "#" * 70)
        print(" " * 18 + " Connecting to Device: " + device)
        print(Fore.MAGENTA + "#" * 70)
        print(Style.RESET_ALL)
        net_connect = ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
        prompter = net_connect.find_prompt()
        if '>' in prompter:
                net_connect.enable()

        output = net_connect.send_command('show run | sec ospf')
        ospf_commands = ['router ospf 1', 'net 0.0.0.0 255.255.255.255 area 0']
        if not 'router ospf' in output:
            print("\n")
            print("~" * 70)
            print(' ' * 15 + Fore.WHITE + 'OSPF is ' + Fore.RED + 'not' + Fore.WHITE + ' enabled on device: ' + device +'!' + Style.RESET_ALL)
            print("~" * 70)
            print("\n")
            answer = input('Would you like you enable default OSPF settings on: ' + device + ' <y/n> ')
            if answer == 'y':
                output = net_connect.send_config_set(ospf_commands)
                print(output)
                print("\n")
                print("+" * 70)
                print(' ' * 20 + Fore.GREEN + 'OSPF is now configured!' + Style.RESET_ALL)
                print("+" * 70)
                print("\n")
            else:
                print("\n")
                print("-" * 70)
                print(' ' * 15 + Fore.RED + 'No OSPF configurations have been made!' + Style.RESET_ALL)
                print("-" * 70)
                print("\n")

        else:
            print("\n")
            print(Fore.YELLOW + "+" * 70)
            print( " " * 10 + " OSPF is already configured on device: " + device + "!")
            print("+" * 70)
            print("\n")
            print(Style.RESET_ALL)
