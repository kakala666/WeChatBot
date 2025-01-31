# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BotCofing.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_BotCofing(object):
    def setupUi(self, BotCofing):
        if not BotCofing.objectName():
            BotCofing.setObjectName(u"BotCofing")
        BotCofing.resize(1063, 691)
        self.gridLayout = QGridLayout(BotCofing)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.BotCofingList = QListWidget(BotCofing)
        self.BotCofingList.setObjectName(u"BotCofingList")

        self.verticalLayout.addWidget(self.BotCofingList)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save = QPushButton(BotCofing)
        self.save.setObjectName(u"save")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.save)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(BotCofing)

        QMetaObject.connectSlotsByName(BotCofing)
    # setupUi

    def retranslateUi(self, BotCofing):
        BotCofing.setWindowTitle(QCoreApplication.translate("BotCofing", u"BotCofing", None))
        self.save.setText(QCoreApplication.translate("BotCofing", u"\u4fdd\u5b58", None))
    # retranslateUi

