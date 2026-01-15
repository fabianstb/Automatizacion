import requests
import netmiko
import json
from netmiko import ConnectHandler

cisco1 = { "ip": "192.168.0.101",
            "device_type": "cisco_ios",
            "username": "cisco",
            "password": "cisco123",

}
comando = "show ip int bri"

with ConnectHandler(**cisco1) as net_connect:
    salida = net_connect.send_command(comando)

print(salida)