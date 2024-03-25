import requests
from pprint import pprint
# https://<адрес-сервера>/method/<имя-API-метода>?<параметры>
# <адрес-сервера> — один из адресов API ВКонтакте:
# api.vk.com
# api.vk.ru

TOKEN = ''

class VKAPIClient:
    API_BASE_URL = 'https://api.vk.com/method'  # единый для всех запросов базовый url
    def __init__(self, token, user_id):        
        self.token = token
        self.user_id = user_id

    def get_common_params(self):
        return {
            'access_token': self.token,
            'v': '5.199'
        }

    def get_status(self):
        params = self.get_common_params()
        params.update({'user_id': self.user_id})          
        response = requests.get(f'{self.API_BASE_URL}/status.get', params=params)
        # return response.json()  
        return response.json().get('response', {}).get('text')        
        # print(response.json())
    
    def set_status(self, new_status):   
        params = self.get_common_params()
        params.update({'user_id': self.user_id, 'text': new_status})
        response = requests.get(f'{self.API_BASE_URL}/status.set', params=params)
        # return response.json().get('response', {}).get('text')  
        response.raise_for_status()  
    
    def replace_status(self, target, replace_string):
        status = self.get_status()
        new_status = status.replace(target, replace_string)
        self.set_status(new_status)


if __name__ == '__main__':
    vk_client = VKAPIClient(TOKEN, 855721559)
    # print(vk_client.user_id)
    # print(vk_client.get_status())
    vk_client.replace_status('Hello', 'Hi')



class VK:   
   def __init__(self, access_token, user_id, version='5.199'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id, 'fields': 'education, sex'}
       response = requests.get(url, params={**self.params, **params})
       return response.json()
   
access_token = TOKEN
user_id = 855721559
# user_id = 1 
vk = VK(access_token, user_id)
# print(vk.users_info())

# def search_query(q, sorting=0):
#     # Параметры sort
#     # 0 - сортировать по умолчанию (аналогичено рузультатам  поиска в полной версии сайта)
#     # 1 - сортировать по скорости роста;
#     # 2 - сортировать по отношению дневной посещаемости и количеству пользователей;
#     # 3 - сортировать по отношению количества лайков к количеству  польователей;
#     # 4 - сортировать по отношению количества комментариев к количеству пользователей;
#     # 5 - сортировать по отношению  количества записей в обсуждениях  к количеству пользователей;
#     params = {
#         'q': q,
#         'access_token': TOKEN,
#         'v': '5.199',
#         'sort': sorting,
#         'count': 3
#     }
#     req =  requests.get('https://api.vk.com/method/groups.search', params).json()
#     # pprint(req)
#     req = req['response']['items']
#     return req
# # search_query('python', 0)

# pprint(search_query('python', 0))


        