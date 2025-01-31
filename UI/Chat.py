# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Chat.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidgetItem, QSizePolicy, QWidget)

from qfluentwidgets import ListWidget

class Ui_Chat(object):
    def setupUi(self, Chat):
        if not Chat.objectName():
            Chat.setObjectName(u"Chat")
        Chat.resize(1064, 694)
        self.listWidget = ListWidget(Chat)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(240, 70, 511, 281))

        self.retranslateUi(Chat)

        QMetaObject.connectSlotsByName(Chat)
    # setupUi

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(QCoreApplication.translate("Chat", u"Chat", None))
    # retranslateUi

