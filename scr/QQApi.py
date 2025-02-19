import re
import requests
import urllib3
import json
import asyncio,time
import kimi,douBao,tongYi,ChatGPT,deepseek
import websockets
import MySignal
from PySide6.QtCore import QThreadPool
from PySide6 import QtConcurrent
import threading
from openai import RateLimitError
from typing import Union
import image_Recognition.BaiDu as OCR
from fuzzywuzzy import process #模糊匹配
import aiohttp #异步请求
from scr.image_Recognition.BaiDu import _OCR_image
from pathlib import Path
headers = {'Content-Type': 'application/json'}
url = "http://localhost:3000/"
with open('../config.json', encoding="utf-8") as f:
  cof = json.load(f)
with open('../QQfriend.json', encoding="utf-8") as f:
  QQcof = json.load(f)
AIPool = {}


class BotApi():
    def __init__(self,start_type = "normal"):
        if start_type != "init":
            self.__update_cache("ALLFRIENDDATA")
            self.__update_cache("ALLGROUPDATA")
        self.__botIsRun = False
        self.AItype = cof["Bot"]
        self.AIchat = None
        self.AItypePool = {
        "kimi": kimi.chat,
        "douBao": douBao.chat,
        "tongYi": tongYi.chat,
        "ChatGPT": ChatGPT.Chat,
        "deepseek": deepseek.chat
        }
        self.history = {}


    def mag_type(self,msg):
        '''
        判断消息类型为文本还是图片
        :param msg:
        :return:
        '''

    def isStart(self) -> bool:
        '''
        判断QQAPI是否在线
        :return:
        '''
        try:
            re = requests.get(headers=headers, url=url + "get_status").json()
        except Exception as e:
            print("连接错误")
            return False
        isOnline = re["data"]["online"]
        isGood = re["data"]["good"]
        if isGood and isOnline:
            #print("启动成功")
            return True
        elif isOnline and not isGood:
            print("状态不符合预期，模块工作不正常")
            return False
        elif not isOnline and isGood:
            print("QQ不在线")
            return False
        elif not isOnline and not isGood:
            print("QQ不在线，模块工作不正常")
            return False
        else:
            print("未知异常状态")
            return False

    def bot_is_run(self) -> bool:
        '''
        判断机器人是否在运行
        :return:
        '''
        return self.__botIsRun

    def setBot(self,user_id,setting,value):
        '''

        :param user_id:
        :param setting: temperature,top_p,presence_penalty,max_tokens
        :param value:
        :return:
        '''
        return AIPool.get(user_id).set_bot(setting,value)

    # 检验QQ号是否合法
    def checkQQ(self,QQ) -> bool:
        '''
        检查QQ号是否合法
        :param QQ:QQ号
        :return:
        '''
        pattern = r'^[1-9]\d{4,11}$'
        return re.fullmatch(pattern, str(QQ)) is not None

    # 用户名QQ号互转
    def name_id_swapping(self,data: Union[str, int]):
        '''
        用户名与QQ号互转
        :param data: 用户名或QQ号
        :return:
        '''
        friendData = asyncio.run(self.get_friend_list())

        Name_to_ID = dict(zip(friendData[0], friendData[1]))
        ID_to_Name = dict(zip(friendData[1], friendData[0]))
        if isinstance(data, int):
            return ID_to_Name.get(data)
        elif isinstance(data, str):
            if data.isdigit():
                return ID_to_Name.get(int(data))
            else:
                return Name_to_ID.get(data)

    def groupName_ID_swapping(self,data: Union[str, int]):
        '''
        群名与ID互转
        :param data: 群名或群ID
        :return:
        '''
        friendData = asyncio.run(self.get_friend_list())

        Name_to_ID = dict(zip(friendData[0], friendData[1]))
        ID_to_Name = dict(zip(friendData[1], friendData[0]))
        if isinstance(data, int):
            return ID_to_Name.get(data)
        elif isinstance(data, str):
            if data.isdigit():
                return ID_to_Name.get(int(data))
            else:
                return Name_to_ID.get(data)

    def get_user_setting(self):
        '''
        获取用户设置
        :return:
        '''
        with open('../config.json', encoding="utf-8") as f:
            cof = json.load(f).get("user_setting")
        return cof

    def save_user_setting(self,coffing):
        '''
        保存用户配置
        :param coffing:
        :return:
        '''
        with open('../config.json', encoding="utf-8") as f:
            cof = json.load(f)
            cof["user_setting"] = coffing
        with open('../config.json', 'w', encoding="utf-8") as f:
            json.dump(cof, f, indent=4, sort_keys=True, ensure_ascii=False)
        print("用户设置已更新")

    def fast_send_private_msg(self,message, user_id):
        asyncio.create_task(self.send_private_msg(message=message, user_id=user_id))

    async def send_private_msg(self,message, user_id=None):
        URL = f"http://localhost:{cof['QQAPIPort']}/send_msg/"
        msg = {
            "user_id": user_id,
            "message": message
        }
        print(json.dumps(msg, ensure_ascii=False))
        print(requests.post(url=URL, data=msg).text)

    def __update_cache(self,type, data=None):
        if data is None:
            if type == "ALLFRIENDDATA":
                data = requests.get(url + "get_friend_list").json().get("data")
            elif type == "ALLGROUPDATA":
                data = requests.get(url + "get_group_list").json().get("data")
            print(data)
        with open('../QQfriend.json', encoding="utf-8") as f:
            cof = json.load(f)
            cof[type] = data
        with open('../QQfriend.json', 'w', encoding="utf-8") as f:
            json.dump(cof, f, indent=4, sort_keys=True, ensure_ascii=False)
        print("QQ好友数据缓存已更新")

    def Search_history(self,msg_id):
        return self.history.get(str(msg_id),default=None)["message"]
    async def get_friend_list(self,update:bool=False):

        if self.isStart():

            async with aiohttp.ClientSession() as session:  # 使用 aiohttp 创建异步会话
                async with session.get(url + "get_friend_list") as response:
                    data = await response.json()  # 异步获取 JSON 数据
                    data = data.get("data", [])

            friendNameList = []
            friendUserIdList = []
            for item in data:
                friendNameList.append(item.get("remark") or item["nickname"])
                friendUserIdList.append(item["user_id"])
            if update:
                self.__update_cache("ALLFRIENDDATA", data)

            return friendNameList, friendUserIdList
        else:
            with open('../QQfriend.json', encoding="utf-8") as f:
                QQcof = json.load(f)["ALLFRIENDDATA"]
            friendNameList = []
            friendUserIdList = []
            for i in QQcof:
                friendNameList.append(i["nickname"])
                friendUserIdList.append(i["user_id"])

            return friendNameList, friendUserIdList

    def fast_get_group_list(self):
        return asyncio.run(self.get_group_list())

    async def get_group_list(self):
        if self.isStart():
            data = requests.get(url + "get_group_list").json()["data"]
            groupNameList = []
            groupIDList = []
            for i in data:
                groupNameList.append(i["group_name"])
                groupIDList.append(i["group_id"])
            self.__update_cache("ALLGROUPDATA", data)
            return groupNameList, groupIDList
        else:
            with open('../QQfriend.json', encoding="utf-8") as f:
                QQcof = json.load(f)["ALLGROUPDATA"]
            groupNameList = []
            groupIDList = []
            for i in QQcof:
                groupNameList.append(i["group_name"])
                groupIDList.append(i["group_id"])
            return groupNameList, groupIDList

    def msg_is_command(self,msg):
        if msg is None:
            return False
        if not msg[0]:
            return False
        if msg[0] == "/":
            return True
        else:
            return False

    def run_command(self,msg:str,fuzz:bool = True,user_id:int = 0):
        '''
        运行对应命令
        :param msg:
        :param fuzz:
        :return:
        '''
        com_list = ["/help","/switchAI","/stop","/status",'/setBot']
        com = process.extractOne(msg,com_list)
        if fuzz and com[1] > 65:
            if not msg.split()[0] == com[0]:
                self.fast_send_private_msg("模糊匹配命令:" + com[0], self.user_id)
                if com[0] == msg.split()[-1]:
                    msg = com[0]
                else:
                    msg = com[0]+" "+msg.split()[-1] # -1获取的是列表最后一项
        if msg.split()[0] == "/help":
            return self.help()
        elif msg.split()[0] == "/switchAI":
            print(msg.split())
            return self.__switchAI(msg.split()[1],True)
        elif msg.split()[0] == "/stop":
            self.stop()
            return "机器人已停止"
        elif msg.split()[0] == "/status":
            return self.get_status()
        elif msg.split()[0] == "/setBot":
            setting = msg.split()[1]
            value = msg.split()[2]
            re = self.setBot(user_id=user_id,setting=setting,value=value)
            self.fast_send_private_msg(re,user_id)
        else:
            return "未知命令"

    def help(self):
        return "/help 帮助\n/switchAI 切换AI\n/stop 停止机器人\n/status 机器人状态"

    def get_status(self):
        return f"机器人类型{self.AItype},机器人状态{self.bot_is_run()}"

    def __switchAI(self, AItype: str,Inheritance:bool):
        AI_chat_functions = {
            "kimi": kimi.chat,
            "douBao": douBao.chat,
            "tongYi": tongYi.chat
        }
        com_list = ["kimi", "douBao", "tongYi"]
        com = process.extractOne(AItype, com_list)
        if com[1] > 70:
            if not AItype == com[0]:
                print("模糊匹配AI类型:" + com[0])
            AItype = com[0]
        history = self.AIchat.get_history() if hasattr(self.AIchat, 'get_history') else None
        if AItype in AI_chat_functions:
            # 设置新的AI类型
            self.AItype = AItype
            # 创建新的聊天对象
            self.AIchat = AI_chat_functions[AItype]()
            # 如果需要继承历史，则调用Inheritance方法
            if Inheritance and hasattr(self.AIchat, 'Inheritance'):
                self.AIchat.Inheritance(history)
            return f"切换为{AItype}"
        else:
            return "切换失败"
        """if AItype == "kimi":
            self.AItype = "kimi"
            history = self.AIchat.get_history()
            self.AIchat = kimi.chat()
            if Inheritance:
                self.AIchat.Inheritance(history)
            return "切换为kimi"
        elif AItype == "douBao":
            self.AItype = "douBao"
            history = self.AIchat.get_history()
            self.AIchat = douBao.chat()
            if Inheritance:
                self.AIchat.Inheritance(history)
            return "切换为douBao"
        elif AItype == "tongYi":
            self.AItype = "tongYi"
            history = self.AIchat.get_history()
            self.AIchat = tongYi.chat()
            if Inheritance:
                self.AIchat.Inheritance(history)
            return "切换为tongYi"
        else:
            return "切换失败" 
        """

    async def async_callback(self,message):
        def send(user_id,msg):
            AI = AIPool.get(user_id)
            retext = AI.chat(msg)
            asyncio.create_task(self.send_private_msg(message=reText, user_id=user_id))

        def download_image(image_url, save_path):
            # 发送GET请求
            response = requests.get(image_url)
            # 检查请求是否成功
            if response.status_code == 200:
                # 打开一个文件用于写入，并写入内容
                with open(save_path, 'wb') as file:
                    file.write(response.content)
                print(f"图片已下载到：{save_path}")
            else:
                print("图片下载失败")
        def msg_type_is_what(msg):
            if msg['post_type'] == "notice":
                if msg['notice_type'] == "friend_recall":
                    return "friend_recall"
            if msg['post_type'] == "message":
                if msg['message_type'] == "private":
                    if msg.get("message")[0].get("type") == 'image':
                        return "private_img"
                    elif msg.get("message")[0].get("type") == 'record':
                        return "private_record"
                    if self.msg_is_command(msg.get("message")[0].get("data").get("text")):
                        return "private_command"
                    return "private_msg"
                elif msg['message_type'] == "group":
                    return "group_msg"

        msg = json.loads(message)

        if self.bot_is_run() == False: #如果机器人停止运行
            return

        msg_type = msg_type_is_what(msg)
        if msg_type == "private_msg":
            print("开始构建AI消息结构")
            sendMsg = {}
            sendMsg["sub_type"] = "private"
            sendMsg["user_id"] = msg.get("user_id")
            sendMsg["user_name"] = msg.get("sender").get("nickname")
            sendMsg["message"] = msg.get("raw_message")
            sendMsg = json.dumps(sendMsg, ensure_ascii=False)
            print(f'消息构建完成{sendMsg}')
            self.history[str(msg.get("message_id"))] = sendMsg
            if self.AIchat == None:
                self.AIchat = self.AItypePool.get(self.AItype)()
            reText = self.AIchat.chat(sendMsg)
            self.fast_send_private_msg(reText, msg.get("user_id"))
        elif msg_type == "group_msg":
            # 如果group_id不在QQcof[gtoup]中，终止操作
            if msg.get("group_id") not in QQcof["Group"]:
                return
            sendMsg = {}
            if msg.get("sub_type") == "normal":
                sendMsg["sub_type"] = "normal"
                sendMsg["message_type"] = "group"
                sendMsg["group_id"] = msg.get("group_id")  # 群号
                sendMsg["user_id"] = msg.get("user_id")  # 发送者QQ
                sendMsg["message"] = msg.get("message")[0].get("data").get("text")  # 消息内容
                sendMsg["raw_message"] = msg.get("raw_message")  # 原始消息内容
                sendMsg["sender"] = json.loads(msg.get("sender"))  # 发送者信息
            elif msg.get("sub_type") == "anonymous":
                sendMsg["sub_type"] = "anonymous"
                sendMsg["message_type"] = "group"
                sendMsg["group_id"] = msg.get("group_id")  # 群号
                sendMsg["user_id"] = msg.get("anonymous").get("id")  # 发送者QQ
                sendMsg["message"] = msg.get("message")[0].get("data").get("text")  # 消息内容
                sendMsg["raw_message"] = msg.get("raw_message")  # 原始消息内容
                sendMsg["sender"] = msg.get("anonymous")  # 发送者信息
            elif msg.get("sub_type") == "notice":
                sendMsg["sub_type"] = "notice"
                sendMsg["message_type"] = "group"
                sendMsg["group_id"] = msg.get("group_id")  # 群号
                sendMsg["message"] = msg.get("message")[0].get("data").get("text")  # 消息内容
                sendMsg["raw_message"] = msg.get("raw_message")  # 原始消息内容

            sendMsg = json.dumps(sendMsg, ensure_ascii=False)
            AIchat = AIPool.get(msg.get("group_id"))
            try:
                if AIchat:
                    reText = AIchat.chat(sendMsg)
                    print(reText)
                    asyncio.create_task(self.send_private_msg(message=reText, user_id=msg.get("group_id")))
                else:
                    if self.AItype == "kimi":
                        AIPool[msg.get("group_id")] = kimi.chat()
                    elif self.AItype == "douBao":
                        AIPool[msg.get("group_id")] = douBao.chat()
                    else:
                        asyncio.create_task(self.send_private_msg(message="Bot配置错误", user_id=msg.get("group_id")))
                    reText = AIPool[msg.get("group_id")].chat(sendMsg)
                    print(reText)
                    asyncio.create_task(self.send_private_msg(message=reText, user_id=msg.get("group_id")))
            except RateLimitError as e:
                asyncio.create_task(self.send_private_msg(message="发的太快啦，休息一会吧", user_id=msg.get("group_id")))
                print("速率限制，请稍后再试")
            except Exception as e:
                asyncio.create_task(self.send_private_msg(message="出现未知错误", user_id=msg.get("group_id")))
        elif msg_type == "friend_recall":
            #history = self.AIchat.get_history()
            self.AIchat.del_history(self.Search_history(msg.get("message_id")))
        elif msg_type == "private_img":
            print("开始构建AI消息结构(图片)")
            sendMsg = {}
            sendMsg["sub_type"] = "private"
            sendMsg["user_id"] = msg.get("user_id")
            sendMsg["user_name"] = msg.get("sender").get("nickname")
            download_image(image_url=msg.get('message')[0].get('data').get('url'), save_path='./Temp/1.png')
            imgae_text = OCR.OCR(Path("./Temp/1.png").resolve())
            sendMsg['image'] = imgae_text
            sendMsg = json.dumps(sendMsg, ensure_ascii=False)
            print(f'消息构建完成{sendMsg}')
            if self.AIchat == None:
                self.AIchat = self.AItypePool.get(self.AItype)()
            reText = self.AIchat.chat(sendMsg)
            self.fast_send_private_msg(reText, msg.get("user_id"))


    async def listen_to_server(self,port):
        uri = f"ws://localhost:{port}"
        async with websockets.connect(uri) as websocket:
            while self.__botIsRun:
                message = await websocket.recv()
                print(f"收到消息：{message}")
                asyncio.create_task(self.async_callback(message, ))


    def run_async_function(self,port):
        asyncio.set_event_loop(asyncio.new_event_loop())
        asyncio.get_event_loop().run_until_complete(self.listen_to_server(port))


    def run(self,port):
        self.__botIsRun = True
        thread = threading.Thread(target=self.run_async_function, args=(port,))
        thread.start()


    def stop(self):
        self.__botIsRun = False
        print("Bot已停止")




