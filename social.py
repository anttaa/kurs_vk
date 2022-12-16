import requests


class VkApi:
    url = 'https://api.vk.com/method'

    def __init__(self, token: str, version: str):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_profile(self, ids, fields):
        params = {'user_ids': ids, 'fields': fields}
        res = requests.get(f'{self.url}/users.get', params={**self.params, **params}).json()
        if 'error' in res:
            print('Ошибка: ', res['error']['error_msg'])
            return None
        return res['response']
