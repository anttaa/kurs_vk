import os
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_header(self):
        return {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_link_upload(self, savefile):
        url_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
        return requests.get(f'{url_upload}/upload?path={savefile}', headers=self.get_header())

    def upload(self, file_path: str):
        file_cnt = 0
        file_err = 0
        for file in os.listdir(file_path):
            file_cnt += 1
            res = self.get_link_upload(os.path.basename(file))
            if res.status_code != 200:
                print(res.json()['message'])
                file_err += 1
                continue

            with open(os.path.join(file_path, file), 'rb') as f:
                r = requests.put(res.json()['href'], files={'file': f})
            print(file, 'загружен')

        return f'\nВсего файлов {file_cnt} из них: \n загружено: {file_cnt - file_err}\n не загружено: {file_err}'

    def upload_from_url(self, url, savefile):
        url_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
        res = requests.post(f'{url_upload}/upload?path={savefile}&url={url}', headers=self.get_header())
        if res.status_code == 202:
            print(savefile, 'загружен')
        else:
            print(res.json()['message'])
