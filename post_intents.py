# -*- coding: utf-8 -*-

import json
import requests
import yaml
import sys
import time

MAX_RETRIES = 3
SLEEP_RETRY = 2

with open("config.yml", 'r') as stream:
    try:
        data = yaml.load(stream)
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(-1)

with open(data['intentsfile'], encoding="UTF8") as stream:
    try:
        intents = json.loads(stream.read())

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(-2)

headers = {'Ocp-Apim-Subscription-Key': data['key']}
url = "https://westus.api.cognitive.microsoft.com/luis/api/v2.0/apps/{appid}/versions/{versionid}/intents".format(appid = data['appid'], versionid = data['versionid'])

for i in intents:
    try:
        for retry in range(MAX_RETRIES):
            r = requests.post(url, headers=headers, data=i)
            print("Intent: {intent}".format(intent=i['name']))
            print("\t.HTTP STATUS: {status}".format(status=r.status_code))
            if r.status_code == 201:
                break
            else:
                print("\t.Retrying in {sec} seconds".format(sec=SLEEP_RETRY))
                time.sleep(SLEEP_RETRY)
    except Exception as e:
        print("Error for creating intent {intent}: {e}".format(intent=i, e=e))
