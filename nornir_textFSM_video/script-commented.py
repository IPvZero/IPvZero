from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_config

def get_facts(task):

    # use Netmiko to poll devices for switchport infomation, and return structured response with textFSM
    r = task.run(netmiko_send_command, command_string="show interface switchport", use_textfsm=True)
    # save the result of the Show Command under the dict key "facts" so we can access the structered results for parsing
    task.host["facts"] = r.result
    # create For loop to be able to parse out information for each interface of the device
    for x in range(0,8):
        # define the commands to be sent when a Trunk interface is detected
        trunk_commands = ['interface ' + task.host['facts'][x]['interface'], 'description This is a TRUNK link']
        # define the commands to be sent when an Access interface is detected
        access_commands = ['interface ' + task.host['facts'][x]['interface'], 'description Access port connected to VLAN ' +
                task.host['facts'][x]['access_vlan']]
        # define the commands to be sent when a shutlink interface is detected
        shut_commands = ['interface ' + task.host['facts'][x]['interface'], 'description This link is Shutdown']
        # Condition 1: If the word "trunk" is in the targeted key-pair value output, use Netmiko to send the trunk_commands
        if "trunk" in task.host['facts'][x]['admin_mode']:
            trunk_description = task.run(netmiko_send_config, config_commands = trunk_commands)
        # Condition 2: if the word "access" is in the targeted key-pair value output, use Netmiko to send the access_commands
        elif "access" in task.host['facts'][x]['admin_mode']:
            access_description = task.run(netmiko_send_config, config_commands = access_commands)
        # Condition 3: if the word "down" is in the targeted key-pair value output, use Netmiko to send the shut_commands
        elif "down" in task.host['facts'][x]['mode']:
            shut_description = task.run(netmiko_send_config, config_commands = shut_commands)

# Call the get_facts function and print the results of the script
def main() -> None:
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=get_facts)
    print_result(result)
    #import ipdb;
    #ipdb.set_trace()

# Python good practices
if __name__ == '__main__':
    main()
