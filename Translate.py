import requests
import json


URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"                                      # Это адрес для обращения к API
headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 ''Firefox/14.0.1')}

class Translate():
    """"класс Translate содержит методы для хранения и последующего
    перевода слов с русского языка на английский"""

    def __init__(self,word):
        self.word=word
        self.memory=[]
        self.key=''


    def translate_me(self, word, headers=headers, key=input('Для начала работы введите ваш API ключ.: ').strip()):    # Здесь ваш API ключ. Для правильной работы его необходимо получить через авторизацию на yandex.ru
        try:
            params = {"key": key, "text": word,"lang": 'ru-en'}                                                       # Здесь мы указываем с какого языка на какой делаем перевод
            response = requests.get(URL, params=params, headers=headers)
            trans_result = ''.join(response.json()['text'])
        except KeyError:
            trans_result='возможно была введенна пустая строка или получен неверный API ключ.'
        except requests.exceptions.ConnectionError:
            trans_result = 'перевод невозможен из-за отсутствия подключения к интернету'
        return trans_result


    def store_memory(self, new_element_memory):
        """"Хранение введенных слов"""
        self.memory.append(new_element_memory)

