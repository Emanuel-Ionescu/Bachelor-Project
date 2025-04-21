# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 720)
        MainWindow.setStyleSheet(u"background : #121212;\n"
"color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.home_tab = QWidget()
        self.home_tab.setObjectName(u"home_tab")
        self.home_tab.setStyleSheet(u"background: #3f3f3f")
        self.gridLayout = QGridLayout(self.home_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_8 = QSpacerItem(381, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(381, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(381, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)

        self.home_qr = QLabel(self.home_tab)
        self.home_qr.setObjectName(u"home_qr")

        self.gridLayout.addWidget(self.home_qr, 1, 2, 1, 1)

        self.home_date = QLabel(self.home_tab)
        self.home_date.setObjectName(u"home_date")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.home_date.sizePolicy().hasHeightForWidth())
        self.home_date.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.home_date.setFont(font1)
        self.home_date.setStyleSheet(u"color: #9972a9;\n"
"padding:20px;")
        self.home_date.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.home_date, 2, 1, 1, 1)

        self.tabWidget.addTab(self.home_tab, "")
        self.lights_tab = QWidget()
        self.lights_tab.setObjectName(u"lights_tab")
        self.lights_tab.setStyleSheet(u"background: #3f3f3f")
        self.gridLayout_3 = QGridLayout(self.lights_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.lights_tab)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(20)
        self.label.setFont(font2)

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.lights_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout_3.addWidget(self.label_2, 1, 3, 1, 1)

        self.light_location_selector = QComboBox(self.lights_tab)
        self.light_location_selector.setObjectName(u"light_location_selector")
        self.light_location_selector.setFont(font2)
        self.light_location_selector.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid #232323;\n"
"	border-radius: 5px;\n"
"	background: #575757;\n"
"	padding-right: 15px;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down{\n"
"	border: 0px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	image: url(/home/emanuel/gui_licenta/resources/icons/down-arrow.svg);\n"
"	width: 30px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.light_location_selector, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.light_source_selector = QComboBox(self.lights_tab)
        self.light_source_selector.setObjectName(u"light_source_selector")
        self.light_source_selector.setFont(font2)
        self.light_source_selector.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid #232323;\n"
"	border-radius: 5px;\n"
"	background: #575757;\n"
"	padding-right: 15px;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down{\n"
"	border: 0px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	image: url(/home/emanuel/gui_licenta/resources/icons/down-arrow.svg);\n"
"	width: 30px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.light_source_selector, 1, 4, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.lights_on_bttn = QPushButton(self.lights_tab)
        self.lights_on_bttn.setObjectName(u"lights_on_bttn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lights_on_bttn.sizePolicy().hasHeightForWidth())
        self.lights_on_bttn.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(False)
        self.lights_on_bttn.setFont(font3)
        self.lights_on_bttn.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 15px;\n"
"background: #575757;")

        self.verticalLayout_4.addWidget(self.lights_on_bttn)

        self.lights_off_bttn = QPushButton(self.lights_tab)
        self.lights_off_bttn.setObjectName(u"lights_off_bttn")
        sizePolicy2.setHeightForWidth(self.lights_off_bttn.sizePolicy().hasHeightForWidth())
        self.lights_off_bttn.setSizePolicy(sizePolicy2)
        self.lights_off_bttn.setFont(font3)
        self.lights_off_bttn.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 15px;\n"
"background: #575757;")

        self.verticalLayout_4.addWidget(self.lights_off_bttn)

        self.lights_color_bttn = QPushButton(self.lights_tab)
        self.lights_color_bttn.setObjectName(u"lights_color_bttn")
        sizePolicy2.setHeightForWidth(self.lights_color_bttn.sizePolicy().hasHeightForWidth())
        self.lights_color_bttn.setSizePolicy(sizePolicy2)
        self.lights_color_bttn.setFont(font3)
        self.lights_color_bttn.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 15px;\n"
"background: #575757;")

        self.verticalLayout_4.addWidget(self.lights_color_bttn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 2, 1, 1)

        self.tabWidget.addTab(self.lights_tab, "")
        self.temperature_tab = QWidget()
        self.temperature_tab.setObjectName(u"temperature_tab")
        self.temperature_tab.setStyleSheet(u"background: #3f3f3f")
        self.gridLayout_4 = QGridLayout(self.temperature_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_11 = QLabel(self.temperature_tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 3, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.temperature_tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.temperature_tab)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.temperature_tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)

        self.label_10 = QLabel(self.temperature_tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 1)

        self.horizontalSlider = QSlider(self.temperature_tab)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider, 1, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.temperature_tab)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_4.addWidget(self.comboBox_3, 1, 1, 1, 1)

        self.tabWidget.addTab(self.temperature_tab, "")
        self.camera_tab = QWidget()
        self.camera_tab.setObjectName(u"camera_tab")
        self.camera_tab.setStyleSheet(u"background: #3f3f3f;")
        self.gridLayout_6 = QGridLayout(self.camera_tab)
        self.gridLayout_6.setSpacing(20)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.label_12 = QLabel(self.camera_tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(15)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.camera_display = QLabel(self.camera_tab)
        self.camera_display.setObjectName(u"camera_display")
        sizePolicy2.setHeightForWidth(self.camera_display.sizePolicy().hasHeightForWidth())
        self.camera_display.setSizePolicy(sizePolicy2)
        self.camera_display.setStyleSheet(u"background: rgba(0,0,0,0);")
        self.camera_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.camera_display, 1, 1, 1, 1)

        self.camera_bttn_down = QPushButton(self.camera_tab)
        self.camera_bttn_down.setObjectName(u"camera_bttn_down")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.camera_bttn_down.sizePolicy().hasHeightForWidth())
        self.camera_bttn_down.setSizePolicy(sizePolicy3)
        self.camera_bttn_down.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 15px;\n"
"background: #575757;")
        icon = QIcon()
        icon.addFile(u"resources/icons/down-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_bttn_down.setIcon(icon)
        self.camera_bttn_down.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.camera_bttn_down, 2, 1, 1, 1)

        self.camera_bttn_up = QPushButton(self.camera_tab)
        self.camera_bttn_up.setObjectName(u"camera_bttn_up")
        sizePolicy3.setHeightForWidth(self.camera_bttn_up.sizePolicy().hasHeightForWidth())
        self.camera_bttn_up.setSizePolicy(sizePolicy3)
        self.camera_bttn_up.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 15px;\n"
"background: #575757;")
        icon1 = QIcon()
        icon1.addFile(u"resources/icons/up-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_bttn_up.setIcon(icon1)
        self.camera_bttn_up.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.camera_bttn_up, 0, 1, 1, 1)

        self.camera_bttn_left = QPushButton(self.camera_tab)
        self.camera_bttn_left.setObjectName(u"camera_bttn_left")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.camera_bttn_left.sizePolicy().hasHeightForWidth())
        self.camera_bttn_left.setSizePolicy(sizePolicy4)
        self.camera_bttn_left.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 15px;\n"
"background: #575757;")
        icon2 = QIcon()
        icon2.addFile(u"resources/icons/left-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_bttn_left.setIcon(icon2)
        self.camera_bttn_left.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.camera_bttn_left, 1, 0, 1, 1)

        self.camera_bttn_right = QPushButton(self.camera_tab)
        self.camera_bttn_right.setObjectName(u"camera_bttn_right")
        sizePolicy4.setHeightForWidth(self.camera_bttn_right.sizePolicy().hasHeightForWidth())
        self.camera_bttn_right.setSizePolicy(sizePolicy4)
        self.camera_bttn_right.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 15px;\n"
"background: #575757;")
        icon3 = QIcon()
        icon3.addFile(u"resources/icons/right-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_bttn_right.setIcon(icon3)
        self.camera_bttn_right.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.camera_bttn_right, 1, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 3)

        self.camera_location_selector = QComboBox(self.camera_tab)
        self.camera_location_selector.setObjectName(u"camera_location_selector")
        sizePolicy1.setHeightForWidth(self.camera_location_selector.sizePolicy().hasHeightForWidth())
        self.camera_location_selector.setSizePolicy(sizePolicy1)
        self.camera_location_selector.setFont(font3)
        self.camera_location_selector.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid #232323;\n"
"	border-radius: 5px;\n"
"	background: #575757;\n"
"	padding-right: 15px;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down{\n"
"	border: 0px solid white;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	image: url(/home/emanuel/gui_licenta/resources/icons/down-arrow.svg);\n"
"	width: 30px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.camera_location_selector, 0, 1, 1, 1)

        self.tabWidget.addTab(self.camera_tab, "")
        self.devices_tab = QWidget()
        self.devices_tab.setObjectName(u"devices_tab")
        self.devices_tab.setStyleSheet(u"background: #3f3f3f")
        self.tabWidget.addTab(self.devices_tab, "")
        self.security_tab = QWidget()
        self.security_tab.setObjectName(u"security_tab")
        self.security_tab.setStyleSheet(u"background: #3f3f3f")
        self.gridLayout_8 = QGridLayout(self.security_tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(576, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(576, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_10 = QPushButton(self.security_tab)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_7.addWidget(self.pushButton_10, 1, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.security_tab)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_7.addWidget(self.pushButton_11, 1, 2, 1, 1)

        self.label_16 = QLabel(self.security_tab)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_14 = QLabel(self.security_tab)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_2.addWidget(self.label_14)

        self.scrollArea = QScrollArea(self.security_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 84, 36))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_3.addWidget(self.label_15)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.gridLayout_8.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.security_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_qr.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.home_date.setText(QCoreApplication.translate("MainWindow", u" 1 Nov 2025", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Light source", None))
        self.lights_on_bttn.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.lights_off_bttn.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.lights_color_bttn.setText(QCoreApplication.translate("MainWindow", u"Choose\n"
"Color", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lights_tab), QCoreApplication.translate("MainWindow", u"Lights", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.temperature_tab), QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.camera_display.setText("")
        self.camera_bttn_down.setText("")
        self.camera_bttn_up.setText("")
        self.camera_bttn_left.setText("")
        self.camera_bttn_right.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.camera_tab), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.devices_tab), QCoreApplication.translate("MainWindow", u"Devices", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.security_tab), QCoreApplication.translate("MainWindow", u"Security", None))
    # retranslateUi

