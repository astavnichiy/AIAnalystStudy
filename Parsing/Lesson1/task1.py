# -*- coding: utf-8 -*-

import requests
import os

req = requests.get("https://api.github.com/users/astavnichiy/repos")

#print(req)
print(req.headers)
print(req.text)

#result = str(req.text)
#print(result)

try:
    f = open('my_repo.json', 'w')
    f.write(req.text)
except:
    print("Есть проблема с файлом")
