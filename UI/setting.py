# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (ComboBox, LineEdit, Slider)

class Ui_setting(object):
    def setupUi(self, setting):
        if not setting.objectName():
            setting.setObjectName(u"setting")
        setting.resize(1329, 704)
        self.gridLayout = QGridLayout(setting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(350, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(setting)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = ComboBox(setting)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(800, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(setting)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.kimi_api_key = LineEdit(setting)
        self.kimi_api_key.setObjectName(u"kimi_api_key")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.kimi_api_key.sizePolicy().hasHeightForWidth())
        self.kimi_api_key.setSizePolicy(sizePolicy1)
        self.kimi_api_key.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.kimi_api_key)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(setting)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.DouBao_api_key = LineEdit(setting)
        self.DouBao_api_key.setObjectName(u"DouBao_api_key")
        self.DouBao_api_key.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.DouBao_api_key)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(setting)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.DouBao_bot_id = LineEdit(setting)
        self.DouBao_bot_id.setObjectName(u"DouBao_bot_id")
        self.DouBao_bot_id.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.DouBao_bot_id)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.label_13 = QLabel(setting)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_13)

        self.tongYi_api_key = QLineEdit(setting)
        self.tongYi_api_key.setObjectName(u"tongYi_api_key")
        self.tongYi_api_key.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_11.addWidget(self.tongYi_api_key)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(setting)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.WeChatWebSocketPort = QLineEdit(setting)
        self.WeChatWebSocketPort.setObjectName(u"WeChatWebSocketPort")
        self.WeChatWebSocketPort.setMinimumSize(QSize(0, 30))
        self.WeChatWebSocketPort.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.WeChatWebSocketPort)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.label_6 = QLabel(setting)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.WeChatApiPort = QLineEdit(setting)
        self.WeChatApiPort.setObjectName(u"WeChatApiPort")
        self.WeChatApiPort.setMinimumSize(QSize(0, 30))
        self.WeChatApiPort.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.WeChatApiPort)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(setting)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.QQWebSocketPort = LineEdit(setting)
        self.QQWebSocketPort.setObjectName(u"QQWebSocketPort")
        self.QQWebSocketPort.setMinimumSize(QSize(0, 30))
        self.QQWebSocketPort.setMaximumSize(QSize(100, 16777215))
        self.QQWebSocketPort.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.QQWebSocketPort)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.label_7 = QLabel(setting)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.QQAPIPort = LineEdit(setting)
        self.QQAPIPort.setObjectName(u"QQAPIPort")
        self.QQAPIPort.setMinimumSize(QSize(0, 30))
        self.QQAPIPort.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.QQAPIPort)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, -1, -1)
        self.label_9 = QLabel(setting)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.temperature_val = QLabel(setting)
        self.temperature_val.setObjectName(u"temperature_val")

        self.horizontalLayout_7.addWidget(self.temperature_val)

        self.temperature = Slider(setting)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.temperature)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.label_10 = QLabel(setting)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.top_p_val = QLabel(setting)
        self.top_p_val.setObjectName(u"top_p_val")

        self.horizontalLayout_8.addWidget(self.top_p_val)

        self.top_p = Slider(setting)
        self.top_p.setObjectName(u"top_p")
        self.top_p.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.top_p)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.label_11 = QLabel(setting)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.presence_penalty_val = QLabel(setting)
        self.presence_penalty_val.setObjectName(u"presence_penalty_val")

        self.horizontalLayout_9.addWidget(self.presence_penalty_val)

        self.presence_penalty = Slider(setting)
        self.presence_penalty.setObjectName(u"presence_penalty")
        self.presence_penalty.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.presence_penalty)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.label_12 = QLabel(setting)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_12)

        self.max_tokens_val = QLabel(setting)
        self.max_tokens_val.setObjectName(u"max_tokens_val")

        self.horizontalLayout_10.addWidget(self.max_tokens_val)

        self.max_tokens = Slider(setting)
        self.max_tokens.setObjectName(u"max_tokens")
        self.max_tokens.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.max_tokens)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.gridLayout.addLayout(self.verticalLayout, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 450, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 3, 1, 1)


        self.retranslateUi(setting)

        QMetaObject.connectSlotsByName(setting)
    # setupUi

    def retranslateUi(self, setting):
        setting.setWindowTitle(QCoreApplication.translate("setting", u"setting", None))
        self.label.setText(QCoreApplication.translate("setting", u"Bot\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("setting", u"KiMi Api-key", None))
        self.label_3.setText(QCoreApplication.translate("setting", u"\u8c46\u5305 Api-key", None))
        self.label_4.setText(QCoreApplication.translate("setting", u"\u8c46\u5305Bot-id", None))
        self.label_13.setText(QCoreApplication.translate("setting", u"\u901a\u4e49\u5343\u95eeApi-key", None))
        self.label_5.setText(QCoreApplication.translate("setting", u"WeChat WebSocket\u7aef\u53e3", None))
        self.label_6.setText(QCoreApplication.translate("setting", u"WeChatAPI\u7aef\u53e3", None))
        self.label_8.setText(QCoreApplication.translate("setting", u"QQ WebSocket\u7aef\u53e3", None))
        self.label_7.setText(QCoreApplication.translate("setting", u"QQAPI\u7aef\u53e3", None))
        self.label_9.setText(QCoreApplication.translate("setting", u"\u91c7\u6837\u6e29\u5ea6", None))
        self.temperature_val.setText(QCoreApplication.translate("setting", u"0", None))
        self.label_10.setText(QCoreApplication.translate("setting", u"\u6838\u91c7\u6837\u6982\u7387\u9608\u503c", None))
        self.top_p_val.setText(QCoreApplication.translate("setting", u"0", None))
        self.label_11.setText(QCoreApplication.translate("setting", u"\u5185\u5bb9\u91cd\u590d\u5ea6", None))
        self.presence_penalty_val.setText(QCoreApplication.translate("setting", u"0", None))
        self.label_12.setText(QCoreApplication.translate("setting", u"\u6700\u5927\u6587\u672c\u957f\u5ea6", None))
        self.max_tokens_val.setText(QCoreApplication.translate("setting", u"0", None))
    # retranslateUi

