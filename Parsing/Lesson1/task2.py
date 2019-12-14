# -*- coding: utf-8 -*-

#Важно! Для серверной части использую Фласк и поднятый апи с авторизацией на нем.


import requests
import os
from requests.auth import HTTPBasicAuth

req = requests.get("http://127.0.0.1:5000/predictFraudGet", auth=HTTPBasicAuth('123', None))

#print(req)
print(req.headers)
print(req.text)

#result = str(req.text)
#print(result)

try:
    f = open('my_repo_auth.json', 'w')
    f.write(req.text)
except:
    print("Все супер")
