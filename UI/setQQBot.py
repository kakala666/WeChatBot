# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setQQBot.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (PushButton, RadioButton)

class Ui_setQQBot(object):
    def setupUi(self, setQQBot):
        if not setQQBot.objectName():
            setQQBot.setObjectName(u"setQQBot")
        setQQBot.resize(1066, 693)
        self.gridLayout = QGridLayout(setQQBot)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.onlyGroup = RadioButton(setQQBot)
        self.onlyGroup.setObjectName(u"onlyGroup")

        self.verticalLayout.addWidget(self.onlyGroup)

        self.onlyPrivate = RadioButton(setQQBot)
        self.onlyPrivate.setObjectName(u"onlyPrivate")

        self.verticalLayout.addWidget(self.onlyPrivate)

        self.All = RadioButton(setQQBot)
        self.All.setObjectName(u"All")

        self.verticalLayout.addWidget(self.All)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.option = PushButton(setQQBot)
        self.option.setObjectName(u"option")

        self.verticalLayout_2.addWidget(self.option)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_text = QLabel(setQQBot)
        self.save_text.setObjectName(u"save_text")

        self.horizontalLayout.addWidget(self.save_text)

        self.save_num = QLabel(setQQBot)
        self.save_num.setObjectName(u"save_num")

        self.horizontalLayout.addWidget(self.save_num)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 1, 1, 1)


        self.retranslateUi(setQQBot)

        QMetaObject.connectSlotsByName(setQQBot)
    # setupUi

    def retranslateUi(self, setQQBot):
        setQQBot.setWindowTitle(QCoreApplication.translate("setQQBot", u"setQQBot", None))
        self.onlyGroup.setText(QCoreApplication.translate("setQQBot", u"\u4ec5\u7fa4\u804a", None))
        self.onlyPrivate.setText(QCoreApplication.translate("setQQBot", u"\u4ec5\u79c1\u804a", None))
        self.All.setText(QCoreApplication.translate("setQQBot", u"\u5168\u90e8", None))
        self.option.setText(QCoreApplication.translate("setQQBot", u"\u9009\u62e9\u597d\u53cb", None))
        self.save_text.setText(QCoreApplication.translate("setQQBot", u"\u5df2\u9009\u62e9\u597d\u53cb\u6570\u91cf\uff1a", None))
        self.save_num.setText(QCoreApplication.translate("setQQBot", u"0", None))
    # retranslateUi

