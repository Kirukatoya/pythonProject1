# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prorhPEih.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(False)
        MainWindow.resize(1130, 688)
        MainWindow.setFocusPolicy(Qt.StrongFocus)
        MainWindow.setStyleSheet(u"*{\n"
"   border: none;\n"
"   background-color: transparent;\n"
"   background: none;\n"
"   padding: 0;\n"
"   margin: 0;\n"
"   color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: rgb(77, 80, 85);\n"
"}\n"
"#LeftMenuContainer {\n"
"	\n"
"	background-color: rgb(80, 70, 85);\n"
"}\n"
"#LeftMenuContainer QPushButton{\n"
"text-align:left;\n"
"padding: 15px 15px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"#frame_3{\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QWidget(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.LeftMenuContainer.setEnabled(False)
        self.LeftMenuContainer.setMaximumSize(QSize(55, 16777215))
        self.LeftMenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MenuBtn = QPushButton(self.frame)
        self.MenuBtn.setObjectName(u"MenuBtn")
        self.MenuBtn.setEnabled(False)
        self.MenuBtn.setStyleSheet(u"background-color: rgb(80, 70, 85);")
        icon = QIcon()
        icon.addFile(u":/icon/icon/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuBtn.setIcon(icon)
        self.MenuBtn.setIconSize(QSize(24, 24))
        self.MenuBtn.setCheckable(False)

        self.verticalLayout_3.addWidget(self.MenuBtn)

        self.HomeBtn = QPushButton(self.frame)
        self.HomeBtn.setObjectName(u"HomeBtn")
        self.HomeBtn.setEnabled(False)
        self.HomeBtn.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/coffee.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeBtn.setIcon(icon1)
        self.HomeBtn.setIconSize(QSize(24, 24))
        self.HomeBtn.setCheckable(False)
        self.HomeBtn.setAutoRepeat(False)
        self.HomeBtn.setAutoExclusive(False)
        self.HomeBtn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.HomeBtn)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.LeftMenuContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.NewTaskBtn = QPushButton(self.frame_2)
        self.NewTaskBtn.setObjectName(u"NewTaskBtn")
        self.NewTaskBtn.setStyleSheet(u"background-color: rgb(80, 70, 85);")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.NewTaskBtn.setIcon(icon2)
        self.NewTaskBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.NewTaskBtn)

        self.SaveBtn = QPushButton(self.frame_2)
        self.SaveBtn.setObjectName(u"SaveBtn")
        self.SaveBtn.setStyleSheet(u"background-color: rgb(80, 70, 85);")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveBtn.setIcon(icon3)
        self.SaveBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.SaveBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.HelpBtn = QPushButton(self.frame_2)
        self.HelpBtn.setObjectName(u"HelpBtn")
        self.HelpBtn.setStyleSheet(u"background-color: rgb(80, 70, 85);")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HelpBtn.setIcon(icon4)
        self.HelpBtn.setIconSize(QSize(24, 24))
        self.HelpBtn.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.HelpBtn)

        self.InformationBtn = QPushButton(self.frame_2)
        self.InformationBtn.setObjectName(u"InformationBtn")
        self.InformationBtn.setEnabled(False)
        self.InformationBtn.setStyleSheet(u"background-color: rgb(80, 70, 85);")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.InformationBtn.setIcon(icon5)
        self.InformationBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.InformationBtn)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.LeftMenuContainer, 0, Qt.AlignLeft)

        self.CenterMenuSubContainer = QWidget(self.centralwidget)
        self.CenterMenuSubContainer.setObjectName(u"CenterMenuSubContainer")
        self.CenterMenuSubContainer.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CenterMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.CenterMenuSubContainer.setSizePolicy(sizePolicy1)
        self.CenterMenuSubContainer.setMouseTracking(True)
        self.CenterMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.CenterMenuSubContainer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.CenterMenuSubContainer)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	border: 2px add rgb(255, 0, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.lineEdit_2)

        self.frame_4 = QFrame(self.CenterMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:11, stop:0 rgba(51, 64, 22, 255), stop:0.121053 rgba(102, 79, 16, 255), stop:0.225 rgba(122, 102, 30, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(157, 145, 68, 255), stop:0.415 rgba(172, 164, 79, 255), stop:0.52 rgba(166, 150, 60, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(152, 140, 59, 255), stop:0.815789 rgba(166, 148, 58, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"\n"
"border-radius: 10px;")

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_3 = QFrame(self.CenterMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(80, 70, 85);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.verticalLayout_7 = QVBoxLayout(self.Home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit = QLineEdit(self.Home)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px add rgb(255, 0, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.lineEdit)

        self.label = QLabel(self.Home)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Franklin Gothic Medium")
        self.label.setFont(font)

        self.verticalLayout_7.addWidget(self.label)

        self.stackedWidget.addWidget(self.Home)
        self.Help = QWidget()
        self.Help.setObjectName(u"Help")
        self.verticalLayout_8 = QVBoxLayout(self.Help)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.Help)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_8.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.Help)
        self.Info = QWidget()
        self.Info.setObjectName(u"Info")
        self.verticalLayout_9 = QVBoxLayout(self.Info)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.Info)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_9.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.Info)
        self.NewTask = QWidget()
        self.NewTask.setObjectName(u"NewTask")
        self.frame_7 = QFrame(self.NewTask)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 10, 971, 531))
        self.frame_7.setMouseTracking(True)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 391, 341))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_17 = QLabel(self.frame_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_13.addWidget(self.label_17)

        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.verticalLayout_13.addWidget(self.label_19)

        self.lineEdit_7 = QLineEdit(self.frame_8)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setTabletTracking(True)
        self.lineEdit_7.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"	border: 2px add rgb(255, 0, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_7.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setReadOnly(False)

        self.verticalLayout_13.addWidget(self.lineEdit_7)

        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.verticalLayout_13.addWidget(self.label_18)

        self.lineEdit_8 = QLineEdit(self.frame_8)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.lineEdit_8)

        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.verticalLayout_13.addWidget(self.label_20)

        self.lineEdit_6 = QLineEdit(self.frame_8)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.lineEdit_6)

        self.label_21 = QLabel(self.frame_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.verticalLayout_13.addWidget(self.label_21)

        self.lineEdit_5 = QLineEdit(self.frame_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.lineEdit_5)

        self.OkBtn = QPushButton(self.frame_7)
        self.OkBtn.setObjectName(u"OkBtn")
        self.OkBtn.setGeometry(QRect(400, 310, 101, 31))
        self.OkBtn.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(0, 0, 0);")
        self.HumansPerHour = QLineEdit(self.frame_7)
        self.HumansPerHour.setObjectName(u"HumansPerHour")
        self.HumansPerHour.setEnabled(False)
        self.HumansPerHour.setGeometry(QRect(420, 100, 331, 18))
        self.HumansPerHour.setTabletTracking(True)
        self.HumansPerHour.setFocusPolicy(Qt.ClickFocus)
        self.HumansPerHour.setStyleSheet(u"QLineEdit {\n"
"	border: 2px add rgb(255, 0, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit.hover{\n"
"	border: 2px add rgb(85, 255, 255);\n"
"}\n"
"\n"
"QLineEdit.focus {\n"
"	border: 2px add rgb(85, 255, 255);	\n"
"}")
        self.HumansPerHour.raise_()
        self.frame_8.raise_()
        self.OkBtn.raise_()
        self.stackedWidget.addWidget(self.NewTask)
        self.NewTask2 = QWidget()
        self.NewTask2.setObjectName(u"NewTask2")
        self.frame_9 = QFrame(self.NewTask2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 10, 961, 531))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(False)
        self.frame_10.setGeometry(QRect(10, 20, 511, 281))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_33 = QLabel(self.frame_10)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.verticalLayout_16.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_10)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)

        self.verticalLayout_16.addWidget(self.label_34)

        self.label_15_Vi1_3 = QLabel(self.frame_10)
        self.label_15_Vi1_3.setObjectName(u"label_15_Vi1_3")
        self.label_15_Vi1_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_15_Vi1_3)

        self.label_37 = QLabel(self.frame_10)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)

        self.verticalLayout_16.addWidget(self.label_37)

        self.label_16_Vi2_3 = QLabel(self.frame_10)
        self.label_16_Vi2_3.setObjectName(u"label_16_Vi2_3")
        self.label_16_Vi2_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_16_Vi2_3)

        self.label_35 = QLabel(self.frame_10)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)

        self.verticalLayout_16.addWidget(self.label_35)

        self.label_17_Vi3_3 = QLabel(self.frame_10)
        self.label_17_Vi3_3.setObjectName(u"label_17_Vi3_3")
        self.label_17_Vi3_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_17_Vi3_3)

        self.label_38 = QLabel(self.frame_10)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)

        self.verticalLayout_16.addWidget(self.label_38)

        self.label_36 = QLabel(self.frame_10)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_36)

        self.stackedWidget.addWidget(self.NewTask2)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.CenterMenuSubContainer)

        self.mainBodyCotntainer = QWidget(self.centralwidget)
        self.mainBodyCotntainer.setObjectName(u"mainBodyCotntainer")
        self.horizontalLayout = QHBoxLayout(self.mainBodyCotntainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalLayout_2.addWidget(self.mainBodyCotntainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.HumansPerHour.textChanged.connect(self.HumansPerHour.setText)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SmartBubble", None))
#if QT_CONFIG(tooltip)
        self.MenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.MenuBtn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
#if QT_CONFIG(tooltip)
        self.HomeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.HomeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.NewTaskBtn.setToolTip(QCoreApplication.translate("MainWindow", u"New task", None))
#endif // QT_CONFIG(tooltip)
        self.NewTaskBtn.setText(QCoreApplication.translate("MainWindow", u"New task", None))
#if QT_CONFIG(tooltip)
        self.SaveBtn.setToolTip(QCoreApplication.translate("MainWindow", u"save", None))
#endif // QT_CONFIG(tooltip)
        self.SaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.HelpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.HelpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.InformationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.InformationBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"hret", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">SmartBubble</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TextHere", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 SmartBubble </span></p><p align=\"center\"><span style=\" font-size:9pt;\">\u0427\u0442\u043e\u0431\u044b \u043d\u0430\u0447\u0430\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443, \u043d\u0430\u0436\u043c\u0438\u0442\u0435 &quot;New task&quot; \u0432 \u043c\u0435\u043d\u044e \u0441\u043b\u0435\u0432\u0430.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">\u0415\u0441\u043b\u0438 \u0432\u044b \u0432\u043f\u0435\u0440\u0432\u044b\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442\u0435 \u0432 \u044d\u0442\u043e\u0439 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435, \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u043d\u043a\u0442 &quot;information&quot;, \u0447\u0442\u043e\u0431\u044b \u043e\u0437\u043d\u0430\u043a\u043e\u043c\u0438\u0442\u044c\u0441\u044f \u0441 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c"
                        "\u0438 \u0444\u0443\u043d\u043a\u0446\u0438\u044f\u043c\u0438.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">\u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0432\u043e\u0437\u043d\u0438\u043a\u043b\u0438 \u0442\u0440\u0443\u0434\u043d\u043e\u0441\u0442\u0438 \u0438\u043b\u0438 \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0438\u0442\u044c \u0438\u0434\u0435\u0438 \u043f\u043e \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044e SmartBubble, \u0432\u043e\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435\u0441\u044c \u043f\u0443\u043d\u043a\u0442\u043e\u043c \u043c\u0435\u043d\u044e &quot;Help&quot;.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">\u0423\u0434\u0430\u0447\u0438!</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u0434\u043b\u044f \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u0438 \u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439:</p><p><br/></p><p><br/></p><p align=\"center\">\u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0432\u043e\u0437\u043d\u0438\u043a\u043b\u0438 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u043f\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e SmartBubble, \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, <br/>\u0441\u0432\u044f\u0436\u0438\u0442\u0435\u0441\u044c \u0441 \u043d\u0430\u0448\u0435\u0439 \u0441\u043b\u0443\u0436\u0431\u043e\u0439 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0438 \u043f\u043e \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e"
                        "\u0439 \u043f\u043e\u0447\u0442\u0435 support_smartbubble@mail.com. </p><p align=\"center\">\u041c\u044b \u043f\u0440\u0438\u043b\u043e\u0436\u0438\u043c \u0432\u0441\u0435 \u0443\u0441\u0438\u043b\u0438\u044f, \u0447\u0442\u043e\u0431\u044b \u043e\u0442\u0432\u0435\u0442\u0438\u0442\u044c \u043d\u0430 \u0432\u0430\u0448 \u0437\u0430\u043f\u0440\u043e\u0441 \u0432 \u0442\u0435\u0447\u0435\u043d\u0438\u0435 24 \u0447\u0430\u0441\u043e\u0432.</p><p align=\"center\">\u041e\u0442\u0437\u044b\u0432\u044b \u0438 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043f\u043e \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044e SmartBubble:</p><p align=\"center\">\u041c\u044b \u0432\u0441\u0435\u0433\u0434\u0430 \u0440\u0430\u0434\u044b \u043e\u0442\u0437\u044b\u0432\u0430\u043c \u0438 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f\u043c \u043e\u0442 \u043d\u0430\u0448\u0438\u0445 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439, \u043a\u043e\u0442\u043e"
                        "\u0440\u044b\u0435 \u043f\u043e\u043c\u043e\u0433\u0430\u044e\u0442 \u043d\u0430\u043c \u0443\u043b\u0443\u0447\u0448\u0438\u0442\u044c \u0441\u0435\u0440\u0432\u0438\u0441 SmartBubble.</p><p align=\"center\">\u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u043a\u0430\u043a\u0438\u0435-\u043b\u0438\u0431\u043e \u0438\u0434\u0435\u0438 \u0438\u043b\u0438 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043f\u043e \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044e \u043d\u0430\u0448\u0435\u0433\u043e \u0441\u0435\u0440\u0432\u0438\u0441\u0430, \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u043d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u043d\u0430\u043c \u043f\u043e \u0430\u0434\u0440\u0435\u0441\u0443 feedback_smartbubble@mail.com. </p><p align=\"center\">\u041c\u044b \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0440\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0438\u043c \u0432\u0430\u0448\u0435 \u043f\u0440\u0435\u0434"
                        "\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0438 \u043e\u0442\u0432\u0435\u0442\u0438\u043c \u043d\u0430 \u0432\u0430\u0448\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0432 \u0442\u0435\u0447\u0435\u043d\u0438\u0435 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u0445 \u0434\u043d\u0435\u0439.</p><p align=\"center\"> \u0411\u043b\u0430\u0433\u043e\u0434\u0430\u0440\u0438\u043c \u0432\u0430\u0441 \u0437\u0430 \u0443\u0447\u0430\u0441\u0442\u0438\u0435 \u0432 \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u0438 SmartBubble!</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u0435\u0440\u0432\u0438\u0441\u0430 SmartBubble</p><p align=\"center\">\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u0432\u0430\u0448\u0435\u0439 \u0430\u0432\u0442\u043e\u043c\u043e\u0439\u043a\u0435</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u043a\u043e\u043b-\u0432\u043e \u043f\u043e\u0441\u0435\u0442\u0438\u0442\u0435\u043b\u0435\u0439 \u0432 \u0447\u0430\u0441", None))
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"hi", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043e\u0447\u0435\u0440\u0435\u0434\u0438", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043a\u0430\u043d\u0430\u043b\u043e\u0432 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None))
#if QT_CONFIG(tooltip)
        self.OkBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.OkBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.HumansPerHour.setText("")
        self.HumansPerHour.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hello", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u043d\u043d\u044b\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438 \u0438 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438</p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0441\u0442\u043e\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u044b", None))
        self.label_15_Vi1_3.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0434\u043b\u0438\u043d\u0430 \u043e\u0447\u0435\u0440\u0435\u0434\u0438", None))
        self.label_16_Vi2_3.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u043e\u0436\u0438\u0434\u0430\u044f \u0432 \u043e\u0447\u0435\u0440\u0435\u0434\u0438", None))
        self.label_17_Vi3_3.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u044d\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u0441\u0438\u0441\u0442\u0435\u043c\u044b", None))
        self.label_36.setText("")
    # retranslateUi

