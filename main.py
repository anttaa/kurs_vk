from cloud import YaUploader
from social import VkApi
import configparser


if __name__ == '__main__':
    INI = configparser.ConfigParser()  # Инициализация INI
    INI.read('settings.ini')  # Считываем настройки
    yadisk_token = INI.get('tokens', 'yadisk')
    vkapi_token = INI.get('tokens', 'vkapi')

    social = VkApi(vkapi_token, '5.131')
    uploader = YaUploader(yadisk_token)
    ids = 'id11994299,id11994315,id11994316'
    for item in social.get_profile(ids, 'photo_max_orig'):
        uploader.upload_from_url(item['photo_max_orig'], f'{item["last_name"]} {item["first_name"]}')
