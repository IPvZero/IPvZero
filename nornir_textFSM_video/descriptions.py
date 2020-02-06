from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_config



def get_facts(task):
    r = task.run(netmiko_send_command, command_string="show interface switchport", use_textfsm=True)
    task.host["facts"] = r.result
    for x in range(0,8):
        trunk_commands = ['interface ' + task.host['facts'][x]['interface'], 'description This is a TRUNK link']
        access_commands = ['interface ' + task.host['facts'][x]['interface'], 'description Access port connected to VLAN ' +
                task.host['facts'][x]['access_vlan']]
        shut_commands = ['interface ' + task.host['facts'][x]['interface'], 'description This link is Shutdown']
        if "trunk" in task.host['facts'][x]['admin_mode']:
            trunk_description = task.run(netmiko_send_config, config_commands = trunk_commands)
        elif "access" in task.host['facts'][x]['admin_mode']:
            access_description = task.run(netmiko_send_config, config_commands = access_commands)
        elif "down" in task.host['facts'][x]['mode']:
            shut_description = task.run(netmiko_send_config, config_commands = shut_commands)

def main() -> None:
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=get_facts)
    print_result(result)
    #import ipdb;
    #ipdb.set_trace()

if __name__ == '__main__':
    main()
