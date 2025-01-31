import base64
from time import sleep

import requests
import json
API_KEY = "nxpAU8gWxT7BpPqTvimnveom"
SECRET_KEY = "IoKJKFhcklMi5kdVyPzhpAC5j6CmsI8o"
__all__ = ['OCR']
def _image_to_base64(image_path):
    # 以二进制模式打开图片文件
    with open(image_path, 'rb') as image_file:
        # 读取图片的二进制内容
        image_data = image_file.read()

    # 将二进制内容编码为Base64
    encoded_data = base64.b64encode(image_data)

    # 将Base64编码的字节转换为字符串
    encoded_str = encoded_data.decode('utf-8')

    return encoded_str

def _OCR_image(image_url:str=None, image_path:str=None, image_base64:str=None):
    json_body = {}
    if image_url != None:
        json_body["url"] = image_url
    elif image_path != None:
        image_base64 = _image_to_base64(image_path)
        json_body["image"] = image_base64
    elif image_base64 != None:
        json_body["image"] = image_base64
    json_body["question"] = "这张图片里有什么，详细描述场景，如果有文字，把文字内容也详细说出来"
    url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/image-understanding/request?access_token=" + _get_access_token()

    payload = json.dumps(json_body)
    headers = {
        'Content-Type': 'application/json'
    }

    #response = requests.request("POST", url, headers=headers, data=payload)
    response = requests.post(url=url,headers=headers,data=payload)
    print(response.json().get('result').get('task_id'))
    return response.json().get('result').get('task_id')

def _get_OCR(task_id:str) -> dict:
    url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/image-understanding/get-result?access_token=" + _get_access_token()
    payload = {"task_id":task_id}
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.json())
    return response.json()

def _get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

def OCR(image_path) -> str:
    '''
    传入图片路径，等待即可获取结果
    :param image_path:
    :return:
    '''
    def is_valid_base64(base64_str):
        pattern = '^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
        return bool(pattern.match(base64_str))

    OCR_task_id = _OCR_image(image_path=image_path)
    while True:
        re = _get_OCR(OCR_task_id)
        if re.get('result').get('ret_code') == 0:
            print('识图结果：'+re.get('result').get('description'))
            return re.get('result').get('description')
        sleep(1)

