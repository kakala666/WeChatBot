import requests
import json
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from moudle.Exception import HttpError
port = 8888
with open("../config.json", encoding="utf-8") as f:
    cof = json.load(f)
    port = cof["WeChatPort"]
url = f"http://127.0.0.1:{port}/api/"
def search_friend():
    data = {
            "type": 10058,
            "dbName": "MicroMsg.db",
            "sql": "SELECT UserName,Remark,NickName,PYInitial,RemarkPYInitial,t2.smallHeadImgUrl FROM Contact t1 LEFT JOIN ContactHeadImgUrl t2 ON t1.UserName = t2.usrName WHERE t1.VerifyFlag = 0 AND (t1.Type = 3 OR t1.Type > 50) and t1.Type != 2050 AND t1.UserName NOT IN ('qmessage', 'tmessage') ORDER BY t1.Remark DESC;"
            }
    try:
        re = requests.post(url=url,json=data,timeout=0.1).json()["data"]["data"]
    except HTTPError as http_err:
        print(f'HTTP错误: {http_err}')  # HTTP错误
        raise HttpError("HTTP错误")
    except ConnectionError as conn_err:
        print(f'连接错误: {conn_err}')  # 连接错误
        raise HttpError("连接错误")
    except Timeout as timeout_err:
        print(f'请求超时: {timeout_err}')  # 请求超时
        raise HttpError("请求超时")
    except RequestException as req_err:
        print(f'请求引发的其他错误: {req_err}')  # 请求引发的其他错误
        raise HttpError("请求引发的其他错误")
        # 处理响应的内容
    except Exception as e:
        # 捕获其他非请求相关的异常
        print(f'An error occurred: {e}')
        raise HttpError(e)
    else:
        return re


