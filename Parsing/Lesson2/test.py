#===============================================================================
# 
# a1 = "https://5ka.ru/api/v2/special_offers/"
# a2 = str(1)
# a3 = "/"
# 
# print(a1+a2+a3)
#===============================================================================



import json

json5 = json.loads('{"id":25594,"name":"РАСТИШ.Йогурт с клуб.дет.2,6% 70г","mech":null,"img_link":"https://media.5ka.ru/media/products/3637008.jpg","promo":{"id":1111317669,"date_begin":"2019-11-28","date_end":"2020-01-03","type":"PROM","description":"ЦФ 28.11-03.01.20 Сезон №14. ЦФ ФРЕШ","kind":"Z011","expired_at":19},"current_prices":{"price_reg__min":29.99,"price_promo__min":26.99},"product":{"plu":3637008,"name":"РАСТИШ.Йогурт с клуб.дет.2,6% 70г","group":{"parent_group_name":"Детские молочные продукты","group_name":"Йогурты свежие от 3 лет"},"brand":"РАСТИШКА","country":null,"weight":"0.070","ingredients":null,"protein":null,"fat":null,"carbohydrate":null,"calories":null,"shelf_life":35,"remaining_shelf_life":7,"package_type":16,"measure_type":null},"store_name":null}')

print(json5["name"])
print(json5["id"])
print(json5["current_prices"]["price_reg__min"])
print(json5["current_prices"]["price_promo__min"])
print(json5["product"]["group"]["group_name"])




