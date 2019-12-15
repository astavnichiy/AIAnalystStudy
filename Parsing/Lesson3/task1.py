from bs4 import BeautifulSoup
import requests
from logging import exception

import pymongo
from pymongo import MongoClient
import random

db_url = 'mongodb://192.168.0.81:27017/'
client = MongoClient(db_url)

#Создание или открытие базы 
db = client.lesson3

#Создание или открытие коллекции 
collection1 = db['tmp2']

strct_tmplt = {}
start_url1 = "https://geekbrains.ru/"
start_url2 = "https://geekbrains.ru/posts?page="
must_urls =[]
res_urls = []

# Получение последней страницы
response = requests.get(start_url2 + "1")
soup = BeautifulSoup(response.text, 'lxml')


paginator1 = soup.select_one('ul.gb__pagination')
paginator2 = paginator1.findAll('a', attrs={'next':''})

#Номер последней страницы
last_page = paginator2[-2].text


# Заполнили массив с страницами
for i in range(1, int(last_page)+1):
    new_url = start_url2 + str(i) 
#    print(new_url)
    must_urls.append(new_url)

print(must_urls[1])

# пошли получать все ссылки 
for j in range(0, len(must_urls)):
    response1 = requests.get(must_urls[j])
    soup1 = BeautifulSoup(response1.text, 'lxml')

# Получаем все ссылки на посты на каждой странице
    for link in soup1.findAll('a'):
        try: 
            link1 = link.get('href')[0:7]
        except:
            link1 = "12345"
        if link1 == "/posts/":
            res = "https://geekbrains.ru" + link.get('href')
            res_urls.append(res)


        print(res_urls)

    for k in range(8, len(res_urls)):
        response2 = requests.get(res_urls[k])
        soup2 = BeautifulSoup(response2.text, 'lxml')
        
        res_author1 = soup2.find("", itemprop="author")
        
        strct_tmplt = {'writer_name':res_author1.text, 'ref':res_urls[k]}
        
#===============================================================================
# Пойдет запись в монго
#===============================================================================
        collection1.insert_one(strct_tmplt)        
               
        print(strct_tmplt)


