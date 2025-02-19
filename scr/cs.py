import time
from turtledemo.penrose import start

from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont
from qfluentwidgets import FluentIcon as FIF
from PySide6.QtWidgets import QHBoxLayout,QMessageBox,QCompleter
from PySide6.QtCore import Qt,Signal
from UI.setting import Ui_setting
from UI.Home import Ui_Home
from UI.BotCofing import Ui_BotCofing
from UI.Chat import Ui_Chat
from UI.setQQBot import Ui_setQQBot
import sys
import json
import re
from qfluentwidgets import PushButton,MessageBoxBase,ListWidget,CheckBox,SearchLineEdit,LineEdit
import WeChatApi
from moudle.Exception import HttpError
from PySide6.QtWidgets import QApplication, QWidget,QListWidgetItem,QLabel,QButtonGroup
from PySide6.QtGui import QFont
import threading
import web
from functools import partial
import MySignal
import QQApi
import asyncio

FriendList = []
GroupList = []



class QFrame(QWidget):
    QQBot = QQApi.BotApi(start_type="init")

class Widget(QFrame):
    '''这个类不重要，不需要看，无用，但别删'''
    sig_Photo = Signal(str)
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)

        # 必须给子界面设置全局唯一的对象名
        self.setObjectName(text.replace(' ', '-'))

class setting(QFrame):

    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_setting()
        #初始化UI
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(["kimi","douBao","tongYi","ChatGpt","deepseek"])
        self.ui.kimi_api_key.setClearButtonEnabled(True)
        self.ui.DouBao_bot_id.setClearButtonEnabled(True)
        self.ui.DouBao_api_key.setClearButtonEnabled(True)
        control_list = ["kimi_api_key","DouBao_api_key","DouBao_bot_id","WeChatWebSocketPort","WeChatApiPort","QQWebSocketPort","QQAPIPort"]
        for control in control_list:
            getattr(self.ui,control).editingFinished.connect(lambda :self.dumpConfig(getattr(self.ui,control),control))

        self.ui.comboBox.currentTextChanged.connect(lambda :self.dumpConfig(self.ui.comboBox,"bot"))
        self.ui.temperature.sliderMoved.connect(lambda :self.dumpConfig(self.ui.temperature,"temperature"))
        self.ui.top_p.sliderMoved.connect(lambda :self.dumpConfig(self.ui.top_p,"top_p"))
        self.ui.presence_penalty.sliderMoved.connect(lambda :self.dumpConfig(self.ui.presence_penalty,"presence_penalty"))
        self.ui.max_tokens.sliderMoved.connect(lambda :self.dumpConfig(self.ui.max_tokens,"max_tokens"))
        self.ui.temperature.setRange(0, 200)
        self.ui.top_p.setRange(0,100)
        self.ui.presence_penalty.setRange(-200,200)
        self.ui.presence_penalty.setValue(-200)
        self.ui.max_tokens.setRange(0,100000)
        #设置步长
        self.ui.temperature.sliderMoved.connect(lambda :self.update_Silder(self.ui.temperature.value(),"temperature_val"))
        self.ui.top_p.sliderMoved.connect(lambda :self.update_Silder(self.ui.top_p.value(),"top_p_val"))
        self.ui.presence_penalty.sliderMoved.connect(lambda :self.update_Silder(self.ui.presence_penalty.value(),"presence_penalty_val"))
        self.ui.max_tokens.sliderMoved.connect(lambda :self.update_Silder(self.ui.max_tokens.value(),"max_tokens_val"))

        # 配置读取
        self.loadConfig()
    def get_bot_setting(self,set):
        if not set == "max_tokens":
            return getattr(self.ui, set).value()/100
        return getattr(self.ui, set).value()
    def update_Silder(self,value,slider):
        if not slider == "max_tokens_val":
            getattr(self.ui, slider).setText(str(value/100))
            return
        getattr(self.ui, slider).setText(str(value))
    def loadConfig(self):
        with open("../config.json", encoding="utf-8") as f:
            cof = json.load(f)
            self.ui.kimi_api_key.setText(cof["kimi"]["api-key"])
            self.ui.DouBao_api_key.setText(cof["doubao"]["api-key"])
            self.ui.DouBao_bot_id.setText(cof["doubao"]["bot-id"])
            self.ui.tongYi_api_key.setText(cof["tongYi"]["api-key"])
            self.ui.WeChatWebSocketPort.setText(str(cof["WebsocketPort"]))
            self.ui.WeChatApiPort.setText(str(cof["WeChatPort"]))
            self.ui.QQWebSocketPort.setText(str(cof["QQWebsocketPort"]))
            self.ui.QQAPIPort.setText(str(cof["QQAPIPort"]))
            self.ui.temperature.setValue(cof["temperature"]*100)
            self.ui.temperature_val.setText(str(cof["temperature"]))
            self.ui.top_p.setValue(cof["top_p"]*100)
            self.ui.top_p_val.setText(str(cof["top_p"]))
            self.ui.presence_penalty.setValue(cof["presence_penalty"]*100)
            self.ui.presence_penalty_val.setText(str(cof["presence_penalty"]))
            self.ui.max_tokens.setValue(cof["max_tokens"]*100)
            self.ui.max_tokens_val.setText(str(cof["max_tokens"]))

    def dumpConfig(self,obj,objName):
        def process_config_value(text):
            # 首先检查文本是否为数字（包括整数和小数）
            if not text.replace(".", "", 1).isdigit() and not (text.startswith('-') and text[1:].replace(".", "", 1).isdigit()):
                # 如果不是数字，直接返回原始文本
                return text

            # 尝试将文本转换为浮点数
            try:
                number = float(text)
            except ValueError:
                # 如果转换失败，说明文本不是一个有效的数字，返回原始文本
                return text

            # 检查数字是否为整数（即没有小数部分）
            if number == round(number):
                # 如果是整数，返回整数类型
                return int(number)
            else:
                # 否则，返回浮点数类型
                return number
        try:
            text = obj.text()
        except Exception as e:
            text = str(obj.value()/100)
        if objName == "DouBao_bot_id":
            # 正则表达式，用于匹配 "ep-" 后跟 14 位数字（8位日期 + 6位时间）
            pattern = re.compile(r'^ep-\d{14}-[a-zA-Z0-9]{5}$')
            if not pattern.match(text):
                QMessageBox.warning(self, '格式错误', '请检查DouBao_bot_id')
                return
        with open("../config.json", encoding="utf-8") as f:
            cof = json.load(f)
            config_mapping = {
                "kimi_api_key": {"section": "kimi", "key": "api-key"},
                "DouBao_api_key": {"section": "doubao", "key": "api-key"},
                "DouBao_bot_id": {"section": "doubao", "key": "bot-id"},
                "tongYi_api_key":{ "section": "tongYi", "key": "api-key"},
                "WebSocketPort":{"section":"WebsocketPort"},
                "WeChatApiPort":{"section":"WeChatPort"},
                "QQWebSocketPort":{"section":"QQWebsocketPort"},
                "QQAPIPort":{"section":"QQAPIPort"},
                "bot":{"section":"Bot"},
                "temperature":{"section":"temperature"},
                "top_p":{"section":"top_p"},
                "presence_penalty":{"section":"presence_penalty"},
                "max_tokens":{"section":"max_tokens"}
            }
            # 获取方法的名称，这里假设 obj 是一个方法
            # 根据方法名称找到对应的配置项
            config_item = config_mapping.get(objName)
            if config_item and ("key" in config_item):
                # 访问字典来设置 cof 字典中的值
                cof[config_item["section"]][config_item["key"]] = text
            elif config_item and (not("key" in config_item)):
                cof[config_item["section"]]=process_config_value(text)

        with open("../config.json", "w", encoding="utf-8") as f:
            # json.dumps(cof).encode("gbk")
            json.dump(cof, f,indent=4, sort_keys=True, ensure_ascii=False)

class setQQBot(QFrame):
    def __init__(self):
        start_time = time.time()
        super().__init__()
        self.ui = Ui_setQQBot()
        self.ui.setupUi(self)
        #将按钮添加到按钮组
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.addButton(self.ui.onlyGroup,1)
        self.buttonGroup.addButton(self.ui.onlyPrivate,2)
        self.buttonGroup.addButton(self.ui.All,3)
        button_end_time = time.time()
        self.friendNameList, self.friendUserIdList = asyncio.run(self.QQBot.get_friend_list(update=False)) #获取好友列表
        get_friend_end_time = time.time()
        # 默认选择只接收私聊消息
        self.ui.onlyPrivate.setChecked(True)
        self.ui.option.clicked.connect(partial(self.optionFriend, "Private", self.friendNameList))
        self.onlyPrivate()
        def switchbutton(button):
            if button.isChecked():
                ID = button.group().checkedId()
                if ID == 1:
                    print("只接收群消息")
                    self.onlyGroup()
                elif ID == 2:
                    print("只接收私聊消息")
                    self.onlyPrivate()
                elif ID == 3:
                    print("接收所有消息")
                    self.All()
        self.buttonGroup.buttonToggled.connect(switchbutton)
        MySignal.SaveMessageList.message_received.connect(self.saveMessageList)
    def onlyGroup(self):
        self.groupNameList,self.groupIdList = asyncio.run(self.QQBot.get_group_list()) #获取群聊列表
        self.ui.option.clicked.disconnect() #清除旧的信号连接
        self.ui.save_text.setText("已选择群聊数量：")
        #显示选择群聊数量文本
        self.ui.save_num.show()
        with open("../QQfriend.json",encoding="utf-8") as f:
            cof = json.load(f)
        self.ui.save_num.setText(str(len(cof["Group"])))
        self.ui.option.setEnabled(True) #启用选择好友按钮
        self.ui.option.setText("选择群聊")
        self.ui.option.clicked.connect(partial(self.optionFriend,"Group", self.groupNameList))
    def onlyPrivate(self):
        self.ui.option.clicked.disconnect() #清除旧的信号连接
        self.ui.save_text.setText("已选择好友数量：")
        # 显示选择好友数量文本
        self.ui.save_num.show()
        with open("../QQfriend.json",encoding="utf-8") as f:
            cof = json.load(f)
        self.ui.save_num.setText(str(len(cof["Private"])))
        self.ui.option.setEnabled(True) #启用选择好友按钮
        self.ui.option.setText("选择好友")
        self.ui.option.clicked.connect(partial(self.optionFriend,"Private", self.friendNameList))
    def All(self):
        self.ui.save_text.setText("此模式无需选择好友")
        self.ui.save_num.hide() #隐藏选择好友数量文本
        self.ui.option.setEnabled(False) #禁用选择好友按钮
    def saveMessageList(self, Type, List):
        with open("../QQfriend.json",encoding="utf-8") as f:
            friendUserIdList = []
            friendCof = json.load(f)
            if Type == "Private":
                for i in List:
                    friendUserIdList.append(self.friendUserIdList[self.friendNameList.index(i)])
                friendCof["Private"] = friendUserIdList

            elif Type == "Group":
                for i in List:
                    friendUserIdList.append(self.groupIdList[self.groupNameList.index(i)])
                friendCof["Group"] = friendUserIdList

        #将friendCof写入QQfriend.json
        with open("../QQfriend.json", "w", encoding="utf-8") as f:
            json.dump(friendCof, f,indent=4, sort_keys=True, ensure_ascii=False)
    def optionFriend(self,Type,friendList):
        w = optionFriend(parent=self,stands=friendList,Type=Type)
        w.show()

class optionFriend(MessageBoxBase,QFrame):
    def __init__(self,Type, stands,parent=None):
        self.BotApi = self.QQBot
        self.FriendList = []
        self.GroupList = []
        with open("../QQfriend.json", encoding="utf-8") as f:
            cof = json.load(f)
            self.FriendList = cof["Private"]
            self.GroupList = cof["Group"]
        self.type = Type
        self.stands = stands
        super().__init__(parent)
        self.listWidget = ListWidget()
        self.labal = QLabel("选择好友")
        self.optionLine = SearchLineEdit() #搜索框
        self.completer = QCompleter(self.stands, self)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)  # 不区分大小写
        self.completer.setCompletionMode(QCompleter.PopupCompletion)  # 下拉列表补全模式
        self.optionLine.setCompleter(self.completer)  # 设置补全器
        # CheckBox = QCheckBox()

        self.ListWidgetItem = QListWidgetItem()
        # 添加列表项
        for stand in stands:
            self.checkbox = CheckBox()
            self.item = QListWidgetItem()
            # self.item.setIcon(QIcon(':/qfluentwidgets/images/logo.png'))
            self.listWidget.addItem(self.item)
            self.listWidget.setItemWidget(self.item, self.checkbox)
            self.checkbox.setText(stand)
            if Type == "Private":
                stand_user_id = self.BotApi.name_id_swapping(stand)
                if stand_user_id in self.FriendList:
                    if sys.gettrace():
                        print(f"{stand}的ID是{stand_user_id}")
                    self.checkbox.setChecked(True)
            elif Type == "Group":
                stand_group_id = self.BotApi.groupName_ID_swapping(stand)
                if stand_group_id in self.GroupList:
                    self.checkbox.setChecked(True)

        self.viewLayout.addWidget(self.labal)
        self.viewLayout.addWidget(self.optionLine)
        self.viewLayout.addWidget(self.listWidget)
        self.optionLine.searchSignal.connect(self.search_Yes)
        self.yesButton.clicked.connect(self.clicked_Yes)
        self.completer.activated.connect(self.search_Yes)

    def clicked_Yes(self):
        List = []
        for i in range(self.listWidget.count()):
            if self.listWidget.itemWidget(self.listWidget.item(i)).isChecked():
                List.append(self.listWidget.itemWidget(self.listWidget.item(i)).text())
        QQ_id_List = []
        for i in List:
            QQ_id_List.append(self.BotApi.name_id_swapping(i))
        self.FriendList=QQ_id_List
        print(List)
        del self.BotApi
        MySignal.SaveMessageList.message_received.emit(self.type,List)

    def search_Yes(self,text):
        self.listWidget.itemWidget(self.listWidget.item(self.stands.index(text))).setChecked(True)
        self.optionLine.clear()
        print(text)

class Home(QFrame):

    def __init__(self,parent=None):
        super().__init__(parent=parent)

        with open("../config.json", encoding="utf-8") as f:
            self.cof = json.load(f)
        self.ui = Ui_Home()
        # 初始化UI
        self.ui.setupUi(self)


        try:
            friendDataList = WeChatApi.search_friend()
            friendUserNameList = [item["NickName"] for item in friendDataList]  # 使用列表推导式提取所有用户名
            friendNameList = [item["Remark"] for item in friendDataList]  # 使用列表推导式提取所有备注名
            friendUserNameList.extend([item["Remark"] for item in friendDataList])  # 合并两种用户名
        except HttpError as e:
            friendUserNameList = []
            #禁用启动微信机器人按钮
            self.ui.runWeChatBot.setEnabled(False)
            #隐藏机器人身份以及对应输入框
            self.ui.Bot_image.hide()
            self.ui.BotName.hide()
            #在horizontalLayout_2中添加一个label，并设置label字号为11
            self.label = QLabel("无法连接到微信")
            font = QFont()
            font.setPointSize(11)
            self.label.setFont(font)
            self.ui.horizontalLayout_2.addWidget(self.label)
            # 设置启动微信机器人按钮的最大宽度是lable的五分之一
            self.ui.runWeChatBot.setMaximumWidth(self.label.width() / 5)


        if not self.QQBot.isStart():
            #禁用启动QQ机器人按钮
            self.ui.runQQBot.setEnabled(False)
            #在horizontalLayout_3中添加一个label，并设置label字号为11
            self.label = QLabel("无法连接到QQ")
            font = QFont()
            font.setPointSize(11)
            self.label.setFont(font)
            self.ui.horizontalLayout_3.addWidget(self.label)
            # 设置启动QQ机器人按钮的最大宽度是lable的五分之一
            self.ui.runQQBot.setMaximumWidth(self.label.width() / 5)
            #在verticalLayout中添加一个pushButton
            self.pushButton = PushButton("刷新状态")
            self.ui.verticalLayout.addWidget(self.pushButton)
            self.pushButton.clicked.connect(self.refresh_bot_status)
        #self.completer = QCompleter(friendUserNameList, self)
        #self.completer.setCaseSensitivity(Qt.CaseInsensitive)  # 不区分大小写
        #self.completer.setCompletionMode(QCompleter.PopupCompletion)  # 下拉列表补全模式
        #self.ui.lineEdit.setCompleter(self.completer)  # 设置补全器
        #self.ui.optionFriend.clicked.connect(partial(self.optionFriend, friendUserNameList))
        self.ui.runWeChatBot.clicked.connect(self.runWeChatBot)
        self.ui.runQQBot.clicked.connect(self.runQQBot)
    def refresh_bot_status(self):
        print("尝试刷新状态")
        if self.QQBot.isStart():
            #启用启动QQ机器人按钮
            self.ui.runQQBot.setEnabled(True)
            #删除label
            self.ui.horizontalLayout_3.removeWidget(self.label)
            #删除pushButton
            self.label.deleteLater()
            self.ui.runQQBot.setMaximumWidth(16777215)
            self.ui.horizontalLayout_3.removeWidget(self.pushButton)
            self.pushButton.deleteLater()
    def optionFriend(self,friendList):
        w = optionFriend(parent=self,stands=friendList)
        w.exec()
    def runWeChatBot(self):
        with open("../config.json", encoding="utf-8") as f:
            cof = json.load(f)
        thread = threading.Thread(target=web.AIrun,args=(cof["WeChatWebSocketPort"],cof["Bot"],))
        thread.start()
    def runQQBot(self):
        with open("../config.json", encoding="utf-8") as f:
            cof = json.load(f)
        self.QQBot.run(cof["QQWebsocketPort"])
        if self.QQBot.bot_is_run():
            self.ui.runQQBot.setText("停止QQ机器人")
            self.ui.runQQBot.clicked.disconnect() #清除旧的信号连接
            self.ui.runQQBot.clicked.connect(self.stopQQBot)
    def stopQQBot(self):
        self.QQBot.stop()
        if not self.QQBot.bot_is_run():
            self.ui.runQQBot.setText("启动QQ机器人")
            self.ui.runQQBot.clicked.disconnect() #清除旧的信号连接
            self.ui.runQQBot.clicked.connect(self.runQQBot) #重新连接信号

class BotCofing(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_BotCofing()
        self.ui.setupUi(self)
        user_set_list = self.__get_user_seting()
        user_set_list_num = len(user_set_list)
        for i in range(10):
            self.Line = LineEdit()
            self.item = QListWidgetItem()
            self.ui.BotCofingList.addItem(self.item)
            self.ui.BotCofingList.setItemWidget(self.item,self.Line)
            self.ui.BotCofingList.itemWidget(self.ui.BotCofingList.item(i)).setPlaceholderText("详细设置Bot")
            if i < user_set_list_num:
                self.ui.BotCofingList.itemWidget(self.ui.BotCofingList.item(i)).setText(user_set_list[i])
            self.ui.BotCofingList.setSpacing(20)
        self.ui.save.clicked.connect(self.__save_user_seting)

    def __get_user_seting(self):
        user_set = self.QQBot.get_user_setting()
        return user_set
    def __save_user_seting(self):
        user_set_list = []
        for i in range(10):
            user_set_list.append(self.ui.BotCofingList.itemWidget(self.ui.BotCofingList.item(i)).text())
        self.QQBot.save_user_setting(user_set_list)

class Chat(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent=parent)

        self.ui = Ui_Chat()
        self.ui.setupUi(self)
        MySignal.getPrivateMessage.message_received.connect(self.upMsg)

    def upMsg(self,Msg):
        print(Msg)
        #self.ui.listWidget.addItem(json.loads(Msg)["raw_message"])

class Window(FluentWindow):
    #初始化
    def __init__(self):
        start_time = time.time()
        super().__init__()

        #self.init_2()
        # 创建子界面
        self.homeInterface = Home()
        homeInterface_end_time = time.time()
        print(f'Home类初始化耗时：{homeInterface_end_time-start_time}')
        self.BotCofing = BotCofing()
        BotCofing_end_time = time.time()
        print(f'BotCofing类初始化耗时：{BotCofing_end_time-homeInterface_end_time}')
        self.chat = Chat()
        chat_end_time = time.time()
        print(f'Chat类初始化耗时：{chat_end_time-BotCofing_end_time}')
        self.settingInterface = setting()
        settingInterface_end_time = time.time()
        print(f'setting类初始化耗时：{settingInterface_end_time-chat_end_time}')
        self.setQQBot = setQQBot()
        setQQBot_end_time = time.time()
        print(f'setQQBot类初始化耗时：{setQQBot_end_time-settingInterface_end_time}')
        '''
        self.albumInterface = Widget('Album Interface', self)
        self.albumInterface1 = Widget('Album Interface 1', self)
        '''
        self.initNavigation()

        self.initWindow()
        end_time=time.time()
        print(f'Window类初始化耗时：{end_time-start_time}')
    #次初始化
    def init_2(self):
        friends = WeChatApi.search_friend()
        with open("../WeChatfriend.json") as f:
            self.friendCof = json.load(f)
            friendUserNameList = [item["NickName"] for item in self.friendCof]  # 使用列表推导式提取所有用户名
            friendWxidList = [item["UserName"] for item in self.friendCof]
            friendNameList = [item["Remark"] for item in self.friendCof]
            for i in len(friendWxidList):
                self.friendCof[friendWxidList[i]] = {"username":friendUserNameList[i],
                                              "name":friendNameList[i],
                                              "type":"",
                                              "msg":""}
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(self.friendCof, f, ensure_ascii=False)
    #添加子页面
    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页')
        self.addSubInterface(self.BotCofing, FIF.ROBOT, 'Bot设置')
        self.addSubInterface(self.chat, FIF.VIDEO, '聊天')
        self.addSubInterface(self.setQQBot, FIF.SETTING, 'QQBot设置')
        self.navigationInterface.addSeparator()
        '''
        self.addSubInterface(self.albumInterface, FIF.ALBUM, 'Albums', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.albumInterface1, FIF.ALBUM, 'Album 1', parent=self.albumInterface)
        '''
        self.addSubInterface(self.settingInterface, FIF.SETTING, '设置', NavigationItemPosition.BOTTOM)

    #程序图标。标题，大小设置
    def initWindow(self):
        self.resize(900, 700) #设置窗口大小
        #self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png')) #设置图标
        self.setWindowTitle('WeChatBot') #设置名称

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    #QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    #QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()