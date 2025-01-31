from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import TogglePushButton
from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont
from qfluentwidgets import FluentIcon as FIF
from PySide6.QtWidgets import QFrame,QApplication,QHBoxLayout,QFileDialog,QMessageBox,QVBoxLayout,QCompleter
from PySide6.QtCore import Qt,Signal
from PySide6.QtGui import QIcon
from UI.setting import Ui_setting
from UI.Home import Ui_Home
import sys
import json
import re
from configparser import ConfigParser
from qfluentwidgets import TogglePushButton,PushButton
import WeChatApi
from moudle.Exception import HttpError
class TwoStateList(QWidget):
    def __init__(self, parent=None):
        super(TwoStateList, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.buttons = {}  # 存储按钮引用

        # 示例数据，实际使用时可以动态生成
        items = ["Item 1", "Item 2", "Item 3"]

        for item in items:
            toggle_button = TogglePushButton(item, self)
            toggle_button.setFixedSize(100, 50)  # 设置按钮大小
            self.layout.addWidget(toggle_button)
            # 示例数据，实际使用时可以动态生成
            #self.add_button(item)

            # 连接信号
            toggle_button.toggled.connect(self.on_button_toggled)

    def add_button(self, text):
        """
        向TwoStateList中添加一个新的二态按钮。

        :param text: 新按钮的文本标签。
        """
        toggle_button = TogglePushButton(text, self)
        toggle_button.setFixedSize(100, 50)  # 设置按钮大小
        self.layout.addWidget(toggle_button)
        self.buttons[text] = toggle_button  # 存储按钮引用

        # 连接信号
        toggle_button.toggled.connect(self.on_button_toggled)
    def on_button_toggled(self, is_checked):
        # 当按钮状态改变时，更新数据模型
        # 可以根据需要实现更复杂的逻辑
        sender = self.sender()
        print(f"Button toggled: {sender.text()}, State: {is_checked}")

# 主函数，用于创建应用程序和控件实例
def main():
    app = QApplication(sys.argv)
    two_state_list = TwoStateList()
    two_state_list.add_button("按钮四")
    two_state_list.show()
    app.exec_()

if __name__ == "__main__":
    main()