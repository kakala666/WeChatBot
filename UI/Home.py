# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (LineEdit, PushButton, SearchLineEdit)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(1066, 693)
        self.gridLayout_2 = QGridLayout(Home)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = SearchLineEdit(Home)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(800, 30))

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.optionFriend = PushButton(Home)
        self.optionFriend.setObjectName(u"optionFriend")
        self.optionFriend.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.optionFriend)

        self.label = QLabel(Home)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.UserName = LineEdit(Home)
        self.UserName.setObjectName(u"UserName")
        self.UserName.setMinimumSize(QSize(0, 30))
        self.UserName.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.UserName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.runWeChatBot = PushButton(Home)
        self.runWeChatBot.setObjectName(u"runWeChatBot")
        self.runWeChatBot.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.runWeChatBot)

        self.Bot_image = QLabel(Home)
        self.Bot_image.setObjectName(u"Bot_image")
        self.Bot_image.setFont(font)

        self.horizontalLayout_2.addWidget(self.Bot_image)

        self.BotName = LineEdit(Home)
        self.BotName.setObjectName(u"BotName")
        self.BotName.setMinimumSize(QSize(0, 30))
        self.BotName.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.BotName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.runQQBot = PushButton(Home)
        self.runQQBot.setObjectName(u"runQQBot")

        self.horizontalLayout_3.addWidget(self.runQQBot)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Home", None))
        self.optionFriend.setText(QCoreApplication.translate("Home", u"\u9009\u62e9\u597d\u53cb", None))
        self.label.setText(QCoreApplication.translate("Home", u"\u4f60\u7684\u79f0\u547c\uff1a", None))
#if QT_CONFIG(accessibility)
        self.UserName.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.UserName.setPlaceholderText(QCoreApplication.translate("Home", u"\u53ea\u6709\u77e5\u9053\u4f60\u7684\u79f0\u547c\u624d\u80fd\u66f4\u597d\u548c\u4f60\u7684\u597d\u53cb\u5bf9\u8bdd", None))
        self.runWeChatBot.setText(QCoreApplication.translate("Home", u"\u542f\u52a8\u5fae\u4fe1\u673a\u5668\u4eba", None))
        self.Bot_image.setText(QCoreApplication.translate("Home", u"\u673a\u5668\u4eba\u7684\u8eab\u4efd\uff1a", None))
#if QT_CONFIG(accessibility)
        self.BotName.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.BotName.setPlaceholderText(QCoreApplication.translate("Home", u"\u4f60\u60f3\u8ba9\u673a\u5668\u4eba\u662f\u4f60\u7684\u4ec0\u4e48", None))
        self.runQQBot.setText(QCoreApplication.translate("Home", u"\u542f\u52a8QQ\u673a\u5668\u4eba", None))
    # retranslateUi

