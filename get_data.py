#!/bin/python

import requests

url = 'https://console.devopshumans.com:8443/oapi/v1'
headers = {'Authorization': 'Bearer GEG7SjadJVaYU2lU1q-4pLb-6XKmCuexG0BweY8lbiI'}

requests.get(url, headers=headers, verify=False)
