import json
from urllib import response
import requests

#requests.packages.urillib3.disable_warnings()

api_url = "https://192.168.0.101/restconf/data/ietf-interfaces:interfaces"

headers = { "accept": "application/yang-data+json",
            "Content-type": "application/yang-data+json"
            }

auth = ("cisco","cisco123")

respuesta = requests.get(api_url, headers=headers, auth=auth, verify=False)
rensponse_json = respuesta.json()
#print(rensponse_json)
print(json.dumps(rensponse_json, indent=4))