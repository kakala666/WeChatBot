from qfluentwidgets import ListWidget,CheckBox
# coding:utf-8
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QTreeWidgetItem, QFileSystemModel, QHBoxLayout,QListWidgetItem,QCheckBox,QPushButton
from PySide6.QtGui import QIcon
from qfluentwidgets import TreeWidget, setTheme, Theme, TreeView
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.hBoxLayout = QHBoxLayout(self)
        self.listWidget = ListWidget()
        #CheckBox = QCheckBox()

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
            #self.item.setIcon(QIcon(':/qfluentwidgets/images/logo.png'))
            self.listWidget.addItem(self.item)
            self.listWidget.setItemWidget(self.item, self.checkbox)
            self.checkbox.setText(stand)
        self.hBoxLayout.addWidget(self.listWidget)


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    sys.exit(app.exec_())