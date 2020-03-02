from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_config

def underlay(task):
    john = str(f"{task.host.hostname}")
    num = john[-1]
    loopback_ip = "10.10.10." + str(num)

    loopback_commands = ['interface loop0', 'ip address 10.10.10.' + str(num) + ' 255.255.255.255', 'ip ospf 1 area 0']
    deploy_loopback = task.run(netmiko_send_config, config_commands = loopback_commands)
    ospf_commands = ['router ospf 1', 'router-id ' + loopback_ip]
    deploy_ospf = task.run(netmiko_send_config, config_commands = ospf_commands)
    interface_commands = ['interface range e0/1-3','ip unnumbered loop0', 'ip ospf network point-to-point', 'ip ospf 1 area 0']
    deploy_interface = task.run(netmiko_send_config, config_commands = interface_commands)
    for i in range(1,9):
        if str(i) == str(num):
            continue
        bgp_commands = ['router bgp ' + str(task.host['asn']), 'neighbor 10.10.10.' + str(i) + ' remote-as ' + str(task.host['asn']),
                'neighbor 10.10.10.' + str(i) + ' update-source loopback0', 'neighbor 10.10.10.' + str(i) + ' password cisco',
                'neighbor 10.10.10.' + str(i) + ' timers 10 30']
        deploy_bgp = task.run(netmiko_send_config, config_commands = bgp_commands)


def main() -> None:
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=underlay)
    print_result(result)

if __name__ == '__main__':
        main()
