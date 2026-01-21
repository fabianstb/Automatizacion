import requests
import netmiko
import json
from netmiko import ConnectHandler

cisco1 = { "ip": "192.168.100.3",
            "device_type": "cisco_ios",
            "username": "cisco",
            "password": "cisco123!",

}
rev = "show ip int bri"
comm1 = ["interface Loopback10","ip address 20.20.20.1 255.255.255.255 ","no shutdown"]

with ConnectHandler(**cisco1) as net_connect:
    salida = net_connect.send_command("show interface Loopback10")
    #net_connect.send_config_set(comm1)
    use_textfsm=True

print(salida)

with ConnectHandler(**cisco1) as net_connect:
    salida = net_connect.send_config_set(comm1)



