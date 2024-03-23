# https:// # протокол
# market.yandex.ru #  адреc хостf(сервера)
# /catalog--mobilnye-telefony/34512430/list # путь
# ?hid=91491 #query params
# &text=iphone%2014 #query params %20-пробел
# &glfilter=7893318%3A153043&rt=11&was_redir=1&cpa=1 #query params
# &rs=eJwzilZy5OLMLMjIz0tVMDQROPboIbMSCweDABuYZICQGgxZCDVVbIamxgYmxg2Mj0-xdjEycTAEMFaxcAA5qxi5OKbducMjsO7rDO4NjAwAA-kYKg%2C%2C&suggest=1 #query params
# &suggest_type=search  #query params означает поисковый запрос
# &parsed-glfilter=7893318%3A153043 #query params 
# &_redirectCount=1 #query params
# &page=15 #query params 15 страница

#  pip3 установить внешнию библиотеку 
# sudo apt install python3-pip
# pip  install requests
import requests
import json
from pprint import pprint

# url_anketa = 'https://functions.yandexcloud.net/d4e8qsrmeednndemfsus'
# payload = {    
#     "name": "Александр",
#     "surname": "Мирошниченко",
#     "patronymic": "Отсутствует",
#     "telephone": "+7(111)111-11-11",
#     "birthdate": "11111-11-11",
#     "passport": "11111 11111111"
# }
# Универсальны метод для все типов(text, xml)
#======================================================================================================
# headers = {
#     "Content-Type": "application/json"
# }
# # response = requests.post(url_anketa, data=payload) # не уазано что payload  это json  
# response = requests.post(url_anketa, 
#                          headers=headers, 
#                          data=json.dumps(payload)) # добавил json
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Простой метод для json
#=======================================================================================================
# response = requests.post(url_anketa, json=payload) # 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# if 200 <= response.status_code < 300: #обычно делают так
# print(response.status_code)
# print(response.content)
# print(response.text)
# print(response.json()) # если можем используем метод json
# pprint(response.headers)
# answer = response.json() #возвращает словарь и False с большой буквы
# print(type(answer))
#**************************************************************************************************

# Работаем с NASA & YANDEX DISK

# 1. Получаем информацию о картинке дня
#**************************************************************************************************
params = {
    'api_key': 'mLNN5BJ0myCI63JGyKYQ1A9sdgILh4dFQNDKJ',
    'date': '2024-03-16'
}
response =  requests.get('https://api.nasa.gov/planetary/apod', params=params)
# print(response.status_code)  
# print(response.headers)  
# pprint(response.json())

# url_image = response.json().get('url') # преобразуем к словарю и возьмем ключ 'hdurl' или 'url'
image_url = response.json()['hdurl'] # преобразуем к словарю и возьмем ключ 'hdurl' или 'url'
image_name = image_url.split('/')[-1]
# print(image_name)
# print(url_image)

# 2. Скачать картинку дня
response = requests.get(image_url)
# print(response.text)
# print(response.content)
with open(image_name, 'wb') as f:
    f.write(response.content)

# 3. Создать папку на диске
#********************************************************************************************************************
headers = {
    'Authorization': 'OAuth y0_AADLWwAAAAD-VgUL9FjfIhGCsEEn0XHOVnjjVVg'
}
response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params={'path': 'image'}, headers=headers)
# params = {
#     'path': 'image'
# }
# response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params=params)

print(response.status_code)
pprint(response.json())

# 4. Загрузка  файла на диск
response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', 
                        headers=headers, 
                        params={'path': f'image/{image_name}'})
print(response.json())
url_for_upload = response.json()['href']
with open(image_name, 'rb') as f:
    requests.put(url_for_upload, files={'file': f})





