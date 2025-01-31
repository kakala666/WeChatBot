# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'optionFriend.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QListWidgetItem, QSizePolicy,
    QWidget)

from qfluentwidgets import (ListWidget, PushButton)

class Ui_optionFriend(object):
    def setupUi(self, optionFriend):
        if not optionFriend.objectName():
            optionFriend.setObjectName(u"optionFriend")
        optionFriend.resize(415, 628)
        self.widget = QWidget(optionFriend)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 10, 361, 591))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = ListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)

        self.pushButton = PushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)


        self.retranslateUi(optionFriend)

        QMetaObject.connectSlotsByName(optionFriend)
    # setupUi

    def retranslateUi(self, optionFriend):
        optionFriend.setWindowTitle(QCoreApplication.translate("optionFriend", u"optionFriend", None))
        self.pushButton.setText(QCoreApplication.translate("optionFriend", u"\u786e\u5b9a", None))
    # retranslateUi

