# Домашнее задание к Уроку 1:

import requests
import json
from pprint import pprint

    # Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
    # сохранить JSON-вывод в файле *.json.

url = 'https://api.github.com'
user = 'Sharovatov-N'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/84.0.4147.135 Safari/537.36'
}

req = requests.get(f'{url}/users/{user}/repos',headers=headers)
with open('data.json', 'w') as f:
    json.dump(req.json(), f)
for i in req.json():
    print(i['name'])

print('*' * 50)
    # Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему,
    # пройдя авторизацию. Ответ сервера записать в файл.

url = 'https://api.nasa.gov/planetary/apod'
key = 'G0rV8PEuizVjvE83pRDdmW1jzw9hVAWfccSoFwVG'

params = {
    'date': '2020-08-01',
    'api_key':key
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/84.0.4147.135 Safari/537.36'
}
response = requests.get(url,headers=headers,params=params)
j_data = response.json()
pprint(j_data)
with open('planetary.json', 'w') as f:
    json.dump(response.json(), f)
