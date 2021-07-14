# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fra_cal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_fra_cal(object):
    def setupUi(self, fra_cal):
        if not fra_cal.objectName():
            fra_cal.setObjectName(u"fra_cal")
        fra_cal.resize(460, 312)
        self.centralwidget = QWidget(fra_cal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title1 = QLabel(self.centralwidget)
        self.title1.setObjectName(u"title1")
        self.title1.setGeometry(QRect(190, 10, 61, 31))
        font = QFont()
        font.setPointSize(15)
        self.title1.setFont(font)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(29, 49, 411, 211))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.title4 = QLabel(self.gridLayoutWidget)
        self.title4.setObjectName(u"title4")
        font1 = QFont()
        font1.setPointSize(13)
        self.title4.setFont(font1)

        self.gridLayout.addWidget(self.title4, 3, 2, 1, 1)

        self.deno2 = QLineEdit(self.gridLayoutWidget)
        self.deno2.setObjectName(u"deno2")
        font2 = QFont()
        font2.setPointSize(12)
        self.deno2.setFont(font2)

        self.gridLayout.addWidget(self.deno2, 4, 2, 1, 1)

        self.numer2 = QLineEdit(self.gridLayoutWidget)
        self.numer2.setObjectName(u"numer2")
        self.numer2.setFont(font2)

        self.gridLayout.addWidget(self.numer2, 6, 2, 1, 1)

        self.title2 = QLabel(self.gridLayoutWidget)
        self.title2.setObjectName(u"title2")
        self.title2.setFont(font1)

        self.gridLayout.addWidget(self.title2, 3, 0, 1, 1)

        self.title3 = QLabel(self.gridLayoutWidget)
        self.title3.setObjectName(u"title3")
        self.title3.setFont(font1)

        self.gridLayout.addWidget(self.title3, 5, 0, 1, 1)

        self.deno1 = QLineEdit(self.gridLayoutWidget)
        self.deno1.setObjectName(u"deno1")
        self.deno1.setFont(font2)

        self.gridLayout.addWidget(self.deno1, 4, 0, 1, 1)

        self.title5 = QLabel(self.gridLayoutWidget)
        self.title5.setObjectName(u"title5")
        self.title5.setFont(font1)

        self.gridLayout.addWidget(self.title5, 5, 2, 1, 1)

        self.numer1 = QLineEdit(self.gridLayoutWidget)
        self.numer1.setObjectName(u"numer1")
        self.numer1.setFont(font2)

        self.gridLayout.addWidget(self.numer1, 6, 0, 1, 1)

        self.method = QComboBox(self.gridLayoutWidget)
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.setObjectName(u"method")
        self.method.setFont(font2)

        self.gridLayout.addWidget(self.method, 4, 1, 1, 1)

        self.start = QPushButton(self.gridLayoutWidget)
        self.start.setObjectName(u"start")
        self.start.setFont(font2)

        self.gridLayout.addWidget(self.start, 6, 1, 1, 1)

        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(160, 269, 111, 31))
        font3 = QFont()
        font3.setPointSize(14)
        self.result.setFont(font3)
        fra_cal.setCentralWidget(self.centralwidget)

        self.retranslateUi(fra_cal)

        QMetaObject.connectSlotsByName(fra_cal)
    # setupUi

    def retranslateUi(self, fra_cal):
        fra_cal.setWindowTitle(QCoreApplication.translate("fra_cal", u"\u5206\u6570\u8ba1\u7b97", None))
        self.title1.setText(QCoreApplication.translate("fra_cal", u"\u5206\u6570\u8ba1\u7b97", None))
        self.title4.setText(QCoreApplication.translate("fra_cal", u"\u5206\u6bcd", None))
        self.title2.setText(QCoreApplication.translate("fra_cal", u"\u5206\u6bcd", None))
        self.title3.setText(QCoreApplication.translate("fra_cal", u"\u5206\u5b50", None))
        self.title5.setText(QCoreApplication.translate("fra_cal", u"\u5206\u5b50", None))
        self.method.setItemText(0, QCoreApplication.translate("fra_cal", u"\u52a0", None))
        self.method.setItemText(1, QCoreApplication.translate("fra_cal", u"\u51cf", None))
        self.method.setItemText(2, QCoreApplication.translate("fra_cal", u"\u4e58", None))
        self.method.setItemText(3, QCoreApplication.translate("fra_cal", u"\u9664", None))

        self.start.setText(QCoreApplication.translate("fra_cal", u"\u5f00\u59cb\u8ba1\u7b97", None))
        self.result.setText("")
    # retranslateUi

