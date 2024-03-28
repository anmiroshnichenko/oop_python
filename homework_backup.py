# Фото  нужно загружать на яндекс диск по ссылке без скачивания
#хранения токена и id  в ini файле? библиотека  configparser
# import configparser  # импортируем библиотеку
# config = configparser.ConfigParser()  # создаём объекта парсера
from configparser import ConfigParser  # импортируем библиотеку
config = ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг
token = config['vk_client']['token']  # обращаемся как к обычному словарю!

import requests
from pprint import pprint
# ссздать файл зависимостей  requirements.txt


#  Kласс  пользователя(взаимодествия)  ВКонтакте

class VkUser:
    url = 'https://api.vk.com/method/'  # единый для всех запросов базовый url
    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        self.owner_id = requests.get(self.url+'users.get', self.params).json()['response'][0]['id']

    def get_photos(self, owner_id=None):
        if owner_id is None:
            owner_id = self.owner_id
        photos_url = self.url + 'photos.get'
        photos_params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'photo_sizes': 1,
            'extended': 0
        }
        res = requests.get(photos_url, params={**self.params, **photos_params})
        return res.json()['response']['items'][0]['sizes'][]
vk_client = VkUser(token, '5.199')
# print(vk_client.params)
# print(vk_client.owner_id) 
pprint(vk_client.get_photos())
# pprint(vk_client.get_groups())

#  Класс пользователя  яндекс диска


# побочная логика

