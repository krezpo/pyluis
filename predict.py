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

q = ""

while q != 'sair':

    q = str(input("Digite a Frase a ser classificada: "))

    if q == 'sair':
        continue

    headers = {'Ocp-Apim-Subscription-Key': data['key']}

    params ={'q': q,
             'timezoneOffset': data['timezoneOffset'],
             'verbose': data['verbose'],
             'spellCheck': data['spellCheck'],
             'staging': data['staging']}

    try:
        r = requests.get(data['endpoint'], headers=headers, params=params)
        
        if r.status_code != 200:
            print("An error has occurred, please verify.")
            print("HTTP STATUS CODE: {}".format(r.status_code))
        else:
            print("Resultado: {}\n".format(r.json()))

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
