#!/bin/python

import requests

url = 'https://console.devopshumans.com:8443/api/v1/endpoints'
headers = {'Authorization': 'Bearer oc whoami -t token'}

res = requests.get(url, headers=headers, verify=False)
data_json = res.json()

items = data_json['items']

for item in items:
    if len(item['subsets']) > 0:
        subdata = item['subsets']
        for data in subdata:
            print "*" * 50
            ip = data['addresses'][0]['ip']
            if data['addresses'][0].has_key('targetRef'):
                targetRef = data['addresses'][0]['targetRef']
                print "Name = " + targetRef['name']
                print "Kind = " + targetRef['kind']
                print "Namespace = " + targetRef['namespace']
                print "Local IP = " + ip
