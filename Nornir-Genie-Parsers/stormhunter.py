from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
from pyfiglet import Figlet

custom_fig = Figlet(font='slant')
sub_fig = Figlet(font='digital')
print(custom_fig.renderText('STORMHUNTER!'))
print(sub_fig.renderText('''Storm's a-brewin'...'''))


def get_facts(task):
    r = task.run(netmiko_send_command, command_string="show interfaces", use_genie=True)
    task.host["facts"] = r.result
    for i in range(0,3):
        for j in range(0,4):
            broadcast_value = int(task.host['facts']['GigabitEthernet' + str(i) + "/" + str(j)]['counters']['in_broadcast_pkts'])
            if broadcast_value >= 1500:
                print("Potential broadcast storm on " + task.host.hostname + "'s GigabitEthernet" + str(i) + "/" + str(j) + " interface")



def main() -> None:
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=get_facts)
    #print_result(result)
    #import ipdb;
    #ipdb.set_trace()

if __name__ == '__main__':
    main()
