import hashlib
import random
import time
import urllib.parse
from string import hexdigits
import Web_Pay
#from encodings.hex_codec import hex_encode

import requests
from collections import OrderedDict

def sign_hash(data, secret):
    # 将字典转换为有序字典，确保键的顺序
    ordered_data = OrderedDict(sorted(data.items()))
    # 过滤掉键名为 'hash' 的元素、空值或者 None
    filtered_data = ((key, value) for key, value in ordered_data.items() if key != 'hash' and value is not None and value != '')
    # 将过滤后的数据拼接成字符串
    str_to_sign = '&'.join(f"{key}={value}" for key, value in filtered_data)
    # 将 secret 拼接到字符串末尾
    str_to_sign += secret
    # 使用 SHA-256 算法生成哈希值
    hash_256 = hashlib.sha256(str_to_sign.encode()).hexdigest()
    print(hash_256)
    return hash_256

def generate_sign(data, secret):
    # 对字典进行排序
    sorted_data = sorted(data.items())
    print(len(sorted_data))
    # 拼接成字符串
    string_a = "&".join(f"{key}={urllib.parse.quote_plus(str(value))}" for key, value in sorted_data if value)
    print(string_a)
    # 拼接AppSecret
    string_sign_temp = string_a + secret
    print(string_sign_temp)
    # 进行hash运算，得到sign值(64位小写)
    sign = hashlib.sha256(string_sign_temp.encode('utf-8')).hexdigest()
    print(sign)
    return sign

def request_payment_url(appid, mch_orderid, description, total, payType, notify_url, nopay_url, callback_url, secret):
    # 构造请求参数
    data = {
        'appid': appid,
        'mch_orderid': mch_orderid,
        'description': description,
        'total': str(total * 100),  # 单位为分
        'payType': payType,
        'notify_url': notify_url,
        'nopay_url': nopay_url,
        'callback_url': callback_url,
        'time': str(int(time.time())),
        'nonce_str': str(random.randint(0, 999999)),
    }

    # 生成签名
    data['sign'] = sign_hash(data, secret)

    # 发送POST请求
    response = requests.post('https://www.yishoumi.cn/u/payment', data=data)

    # 解析响应
    response_data = response.json()

    if response_data['code'] == 0:
        payment_url = response_data['url']
        return payment_url
    else:
        raise Exception(f"Request failed: {response_data['msg']}")

# 填入你的参数
appid = 'YSMa3e82d6f'
mch_orderid = str("S"+str(int(time.time())))
description = '商品描述'
total = 300  # 100元
payType = 1  # 微信
notify_url = 'www.baidu.com'
nopay_url = 'www.baidu.com'
callback_url = 'www.baidu.com'
secret = 'aa8d82fdd6894144556c9fe7a07412fa'

# 请求支付URL
try:
    payment_url = request_payment_url(appid, mch_orderid, description, total, payType, notify_url, nopay_url,
                                      callback_url, secret)
    print(f"Payment URL: {payment_url}")
    Web_Pay.up_data(total,payment_url)
except Exception as e:
    print(e)