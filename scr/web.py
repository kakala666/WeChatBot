import requests
import ssl
import json
import asyncio
import websockets
import kimi
import douBao
import time
import threading
headers = {'Content-Type': 'application/json'}
url = "http://127.0.0.1:8888/api/"
with open('../WeChatfriend.json') as f:
  friends = json.load(f)
async def async_callback(message,AItype):
    wxid = json.loads(message)["data"]["from"]
    contenet = json.loads(message)["data"]["content"]
    if wxid in friends:
        msg = friends[wxid]
        msg["msg"] = contenet
    else:
        friendIni = {
            "type": 10015,
            "userName": wxid
        }
        friendName = requests.post(url="http://127.0.0.1:8888/api/", json=friendIni).json()["data"]["data"]["remark"]
        msg=friends["void"]
        msg["username"]=friendName
        msg["msg"]=contenet
    if AItype == "doubao":
        AImsg = douBao.chat(json.dumps(msg))
    elif AItype == "kimi":
        AImsg = kimi.chat(json.dumps(msg))
    text = {
        "type": 10009,
        "userName": wxid,
        "msgContent": AImsg,
        "insertToDatabase": True
    }
    r = requests.post(headers=headers, url="http://127.0.0.1:8888/api/", json=text).json()
    print(r)
def run(port,AItype):
    Websocket = {
        "type": 1001,
        "protocol": 3,
        "url": f"http://127.0.0.1:{port}/"
    }
    requests.post(url=url, json=Websocket)
    time.sleep(0.01)
    async def echo(websocket, path):
        async for message in websocket:
            # 处理接收到的消息
            print(message)
            asyncio.create_task(async_callback(message,AItype))
    print("a")
    start_server = websockets.serve(echo, "127.0.0.1", port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


def AIrun(port, AItype):
    headers = {'Content-Type': 'application/json'}
    url = "http://127.0.0.0:8888/api/"
    print(port)
    print(AItype)
    Websocket = {
        "type": 1001,
        "protocol": 3,
        "url": f"http://127.0.0.1:{port}/"
    }
    requests.post(url=url, json=Websocket)
    #time.sleep(0.01)

    async def echo(websocket, path):
        async for message in websocket:
            # 处理接收到的消息
            print(message)
            asyncio.create_task(async_callback(message, AItype))

    def start_server_in_thread():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        start_server = websockets.serve(echo, "127.0.0.1", port)
        loop.run_until_complete(start_server)
        loop.run_forever()
    print("aaa")
    websocket_thread = threading.Thread(target=start_server_in_thread)
    websocket_thread.start()