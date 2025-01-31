import requests
import json
import random
import hashlib
class fanyi:
    def __init__(self,appid,key):
        self.url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
        self.ContentType = 'application/x-www-form-urlencoded'
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'}
        self.appid = appid
        self.key = key
    def fanyi(self, query:str, from_lang='auto', to_lang='zh'):
        randomInt = str(random.randint(1, 100))
        Sign1 = self.appid + query + randomInt + self.key
        Sing2 = hashlib.md5(Sign1.encode('utf-8'))
        data = {
            'q': query,
            'from': from_lang,
            'to': to_lang,
            'appid': self.appid,
            'salt': randomInt,
            'sign': Sing2
        }
        response = requests.post(self.url, headers=self.headers, data=data)
        return response.json()

print(fanyi("20201108000611875","fLn5mzvKEQUo08HISzZk").fanyi("hello"))