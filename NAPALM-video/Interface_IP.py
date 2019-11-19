from napalm import get_network_driver
import json

cisco_ip = ["SWITCH2",
            "SWITCH3",
            "SWITCH4",
            "SWITCH5",
            ]

for ip in cisco_ip:
    print("*********************************      " + ip + "     *********************************")
    DRV = get_network_driver('ios')
    cisco_device = DRV(ip, 'john', 'ipvzero')
    cisco_device.open()

    response = cisco_device.get_interfaces_ip()
    dump_output = json.dumps(response, indent=4)
    print(dump_output)

arista_ip = ["SWITCH6",
             "SWITCH7",
             "SWITCH8",
             ]

for ip in arista_ip:
    print("**********************************     " + ip + "     ***********************************")
    DRV = get_network_driver('eos')
    arista_device = DRV(ip, 'john', 'ipvzero')
    arista_device.open()

    response = arista_device.get_interfaces_ip()
    dump_output = json.dumps(response, indent=4)
    print(dump_output)
