# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pbajAXrD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.img_bg = QLabel(self.centralwidget)
        self.img_bg.setObjectName(u"img_bg")
        self.img_bg.setGeometry(QRect(0, 0, 1920, 1080))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_bg.sizePolicy().hasHeightForWidth())
        self.img_bg.setSizePolicy(sizePolicy)
        self.img_bg.setPixmap(QPixmap(u"elements/background.png"))
        self.img_bg.setScaledContents(True)
        self.img_bg.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.img_bg.setWordWrap(False)
        self.img_overlay = QLabel(self.centralwidget)
        self.img_overlay.setObjectName(u"img_overlay")
        self.img_overlay.setGeometry(QRect(0, 0, 1920, 1080))
        sizePolicy.setHeightForWidth(self.img_overlay.sizePolicy().hasHeightForWidth())
        self.img_overlay.setSizePolicy(sizePolicy)
        self.img_overlay.setAutoFillBackground(False)
        self.img_overlay.setPixmap(QPixmap(u"elements/screen_overlay.png"))
        self.img_overlay.setScaledContents(True)
        self.img_overlay.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.img_take1 = QLabel(self.centralwidget)
        self.img_take1.setObjectName(u"img_take1")
        self.img_take1.setGeometry(QRect(92, 100, 338, 190))
        sizePolicy.setHeightForWidth(self.img_take1.sizePolicy().hasHeightForWidth())
        self.img_take1.setSizePolicy(sizePolicy)
        self.img_take1.setAutoFillBackground(False)
        self.img_take1.setPixmap(QPixmap(u"img1.jpg"))
        self.img_take1.setScaledContents(True)
        self.img_take1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.img_take2 = QLabel(self.centralwidget)
        self.img_take2.setObjectName(u"img_take2")
        self.img_take2.setGeometry(QRect(92, 356, 338, 190))
        sizePolicy.setHeightForWidth(self.img_take2.sizePolicy().hasHeightForWidth())
        self.img_take2.setSizePolicy(sizePolicy)
        self.img_take2.setAutoFillBackground(False)
        self.img_take2.setPixmap(QPixmap(u"img1.jpg"))
        self.img_take2.setScaledContents(True)
        self.img_take2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.img_take3 = QLabel(self.centralwidget)
        self.img_take3.setObjectName(u"img_take3")
        self.img_take3.setGeometry(QRect(92, 617, 338, 190))
        sizePolicy.setHeightForWidth(self.img_take3.sizePolicy().hasHeightForWidth())
        self.img_take3.setSizePolicy(sizePolicy)
        self.img_take3.setAutoFillBackground(False)
        self.img_take3.setPixmap(QPixmap(u"img1.jpg"))
        self.img_take3.setScaledContents(True)
        self.img_take3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.img_cam = QLabel(self.centralwidget)
        self.img_cam.setObjectName(u"img_cam")
        self.img_cam.setGeometry(QRect(568, 106, 1244, 702))
        sizePolicy.setHeightForWidth(self.img_cam.sizePolicy().hasHeightForWidth())
        self.img_cam.setSizePolicy(sizePolicy)
        self.img_cam.setAutoFillBackground(False)
        self.img_cam.setPixmap(QPixmap(u"img1.jpg"))
        self.img_cam.setScaledContents(True)
        self.img_cam.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(928, 858, 464, 206))
        icon = QIcon()
        icon.addFile(u"elements/btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(464, 206))
        self.pushButton.setFlat(True)
        self.img_counter = QLabel(self.centralwidget)
        self.img_counter.setObjectName(u"img_counter")
        self.img_counter.setGeometry(QRect(822, 150, 676, 625))
        sizePolicy.setHeightForWidth(self.img_counter.sizePolicy().hasHeightForWidth())
        self.img_counter.setSizePolicy(sizePolicy)
        self.img_counter.setAutoFillBackground(False)
        self.img_counter.setPixmap(QPixmap(u"elements/counter_1.png"))
        self.img_counter.setScaledContents(True)
        self.img_counter.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.img_bg.raise_()
        self.img_take1.raise_()
        self.img_take2.raise_()
        self.img_take3.raise_()
        self.img_cam.raise_()
        self.img_overlay.raise_()
        self.img_counter.raise_()
        self.pushButton.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_bg.setText("")
        self.img_overlay.setText("")
        self.img_take1.setText("")
        self.img_take2.setText("")
        self.img_take3.setText("")
        self.img_cam.setText("")
        self.pushButton.setText("")
        self.img_counter.setText("")
    # retranslateUi

