import json
import requests
import urllib3
urllib3.disable_warnings()
api_url = "https://192.168.0.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback20"
headers = { "Accept": "application/yang-data+json",
            "Content-type": "application/yang-data+json"
            }
auth = ("cisco", "cisco123")

config = {
    "ietf-interfaces:interface": {
        "name": "Loopback20",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "20.0.0.2",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

respuesta = requests.put(api_url, data=json.dumps(config), headers=headers, auth=auth, verify=False)
#print(respuesta)

if(respuesta.status_code >= 200 and respuesta.status_code <=299):
    print("ESTADO OK: {}".format(respuesta.status_code))
else:
    print("ERROR CODE: {}, REPLY: {}".format(respuesta.status_code, respuesta.json()))