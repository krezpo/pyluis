# -*- coding: utf-8 -*-

import json
import requests
import yaml
import sys

with open("config.yml", 'r') as stream:
    try:
        data = yaml.load(stream)
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(-1)

headers = {'Ocp-Apim-Subscription-Key': data['key']}

try:
    r = requests.get('https://westus.api.cognitive.microsoft.com/luis/api/v2.0/apps/{}/endpoints'.format(data['appid']), headers=headers)
        
    if r.status_code != 200:
        print("An error has occurred, please verify.")
        print("HTTP STATUS CODE: {}".format(r.status_code))
    else:
        print("Resultado: {}\n".format(r.json()))

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
