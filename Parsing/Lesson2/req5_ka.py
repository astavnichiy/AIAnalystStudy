# -*- coding: utf-8 -*-

import os
import json

#req = requests.get("https://api.github.com/users/astavnichiy/repos")







def get_value_id(json5ka):
    json5ka = json.loads(json5ka)
    try: 
        return json5ka["id"]
    except:
        return "pka_null"
    


def get_value_name(json5ka):
    json5ka = json.loads(json5ka)
    return json5ka["name"]

   
def get_value_price_reg__min(json5ka):
    json5ka = json.loads(json5ka)
    return json5ka["current_prices"]["price_reg__min"]

    
def get_value_price_promo__min(json5ka):
    json5ka = json.loads(json5ka)
    return json5ka["current_prices"]["price_promo__min"]

    
def get_value_group_name(json5ka):
    json5ka = json.loads(json5ka)
    return json5ka["product"]["group"]["group_name"]







    
#===============================================================================
# print (req.text)
# 
# try:
#     f = open('data5ka.json', 'a')
#     f.write(req.text)
#     f.write('\n')
#     #f.writelines(req.text)
#     f.close()
# except:
#     print("Есть проблема с файлом")
#===============================================================================