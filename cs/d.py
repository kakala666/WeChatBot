# coding:utf-8
import sys

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout,QListWidgetItem

from qfluentwidgets import MessageBoxBase, SubtitleLabel, LineEdit, PushButton, setTheme, Theme,ListWidget,CheckBox


class CustomMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('打开 URL', self)
        self.urlLineEdit = LineEdit(self)

        self.urlLineEdit.setPlaceholderText('输入文件、流或者播放列表的 URL')
        self.urlLineEdit.setClearButtonEnabled(True)

        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        # change the text of button
        self.yesButton.setText('打开')
        self.cancelButton.setText('取消')

        self.widget.setMinimumWidth(350)
        self.yesButton.setDisabled(True)
        self.urlLineEdit.textChanged.connect(self._validateUrl)

        # self.hideYesButton()

    def _validateUrl(self, text):
        self.yesButton.setEnabled(QUrl(text).isValid())
class friendList(MessageBoxBase):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.listWidget = ListWidget()
        # CheckBox = QCheckBox()

        stands = [
            '白金之星', '绿色法皇', "天堂制造", "绯红之王",
            '银色战车', '疯狂钻石', "壮烈成仁", "败者食尘",
            "隐者之紫", "黄金体验", "虚无之王", "纸月之王",
            "骇人恶兽", "男子领域", "华丽挚爱", "牙 Act 4",
            "铁球破坏者", "性感手枪", 'D4C • 爱之列车', "天生完美",
            "软又湿", "佩斯利公园", "奇迹于你", "行走的心",
            "护霜旅行者", "十一月雨", "调情圣手", "片刻静候"
        ]
        self.ListWidgetItem = QListWidgetItem()
        # 添加列表项
        for stand in stands:
            self.checkbox = CheckBox()
            self.item = QListWidgetItem()
            # self.item.setIcon(QIcon(':/qfluentwidgets/images/logo.png'))
            self.listWidget.addItem(self.item)
            self.listWidget.setItemWidget(self.item, self.checkbox)
            self.checkbox.setText(stand)
        self.hBoxLayout.addWidget(self.listWidget)
        self.viewLayout.addWidget(self.listWidget)
        self.yesButton.clicked.connect(self.clicked_Yes)

    def clicked_Yes(self):
        friendList = []
        for i in range(self.listWidget.count()):
            if self.listWidget.itemWidget(self.listWidget.item(i)).isChecked():
                friendList.append(self.listWidget.itemWidget(self.listWidget.item(i)).text())
        print(friendList)
class Demo(QWidget):

    def __init__(self,parent=None):
        super().__init__()
        # setTheme(Theme.DARK)
        # self.setStyleSheet('Demo{background:rgb(32,32,32)}')

        self.hBxoLayout = QHBoxLayout(self)
        self.button = PushButton('打开 URL', self)

        self.resize(600, 600)
        self.hBxoLayout.addWidget(self.button, 0, Qt.AlignCenter)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        b= ["a","b"]
        w = friendList(self)
        if w.exec():
            #print(w.urlLineEdit.text())
            pass

if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)


    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()