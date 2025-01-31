import requests
import json
import web

with open('../config.json', encoding="utf-8") as f:
  cof = json.load(f)

WebsocketPort = cof["WebsocketPort"]
WeChatPort = cof["WeChatPort"]
AItype = cof["Bot"]
print(WeChatPort)
print(WebsocketPort)
print(AItype)
headers = {'Content-Type': 'application/json'}
url = "http://127.0.0.1:8888/api/"
data ={
"type": 10058,
"dbName": "MicroMsg.db",
"sql": "SELECT UserName,Remark,NickName,PYInitial,RemarkPYInitial,t2.smallHeadImgUrl FROM Contact t1 LEFT JOIN ContactHeadImgUrl t2 ON t1.UserName = t2.usrName WHERE t1.VerifyFlag = 0 AND (t1.Type = 3 OR t1.Type > 50) and t1.Type != 2050 AND t1.UserName NOT IN ('qmessage', 'tmessage') ORDER BY t1.Remark DESC;"
}
Websocket =   {
  "type": 1001,
  "protocol": 3,
  "url": f"http://127.0.0.1:{WebsocketPort}/"
}

"""requests.post(url=url,json=Websocket)

web.run(WebsocketPort,AItype)"""
