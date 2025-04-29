# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"background : #333333;\n"
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
        font.setFamilies([u"Sans"])
        font.setPointSize(45)
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    \n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 15px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(36, 31, 49, 255));\n"
"	color: #aaaaaa;\n"
"	border-radius: 10px;\n"
"    min-width: 8ex;\n"
"    padding: 10px;\n"
"	margin-left:5px;\n"
"	margin-top:5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.home_tab = QWidget()
        self.home_tab.setObjectName(u"home_tab")
        self.home_tab.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(34, 34, 34, 255))")
        self.gridLayout = QGridLayout(self.home_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_9 = QSpacerItem(381, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.clock_display = QLabel(self.home_tab)
        self.clock_display.setObjectName(u"clock_display")

        self.gridLayout.addWidget(self.clock_display, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.tabWidget.addTab(self.home_tab, "")
        self.lights_tab = QWidget()
        self.lights_tab.setObjectName(u"lights_tab")
        self.lights_tab.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(34, 34, 34, 255))")
        self.gridLayout_3 = QGridLayout(self.lights_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.lights_tab)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(40)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background: rgba(0,0,0,0);")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.lights_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background: rgba(0,0,0,0);")

        self.gridLayout_3.addWidget(self.label_2, 1, 3, 1, 1)

        self.light_location_selector = QComboBox(self.lights_tab)
        self.light_location_selector.setObjectName(u"light_location_selector")
        self.light_location_selector.setFont(font1)
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
"	image: url(/home/debian/gui_licenta/resources/icons/down-arrow.svg);\n"
"	width: 30px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.light_location_selector, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.light_source_selector = QComboBox(self.lights_tab)
        self.light_source_selector.setObjectName(u"light_source_selector")
        self.light_source_selector.setFont(font1)
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
"	image: url(/home/debian/gui_licenta/resources/icons/down-arrow.svg);\n"
"	width: 30px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.light_source_selector, 1, 4, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.lights_on_bttn = QPushButton(self.lights_tab)
        self.lights_on_bttn.setObjectName(u"lights_on_bttn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lights_on_bttn.sizePolicy().hasHeightForWidth())
        self.lights_on_bttn.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(False)
        self.lights_on_bttn.setFont(font2)
        self.lights_on_bttn.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 15px;\n"
"background: #444444;")

        self.verticalLayout_4.addWidget(self.lights_on_bttn)

        self.lights_off_bttn = QPushButton(self.lights_tab)
        self.lights_off_bttn.setObjectName(u"lights_off_bttn")
        sizePolicy1.setHeightForWidth(self.lights_off_bttn.sizePolicy().hasHeightForWidth())
        self.lights_off_bttn.setSizePolicy(sizePolicy1)
        self.lights_off_bttn.setFont(font2)
        self.lights_off_bttn.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 15px;\n"
"background: #444444;")

        self.verticalLayout_4.addWidget(self.lights_off_bttn)

        self.lights_color_bttn = QPushButton(self.lights_tab)
        self.lights_color_bttn.setObjectName(u"lights_color_bttn")
        sizePolicy1.setHeightForWidth(self.lights_color_bttn.sizePolicy().hasHeightForWidth())
        self.lights_color_bttn.setSizePolicy(sizePolicy1)
        self.lights_color_bttn.setFont(font2)
        self.lights_color_bttn.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 15px;\n"
"background: #444444;")

        self.verticalLayout_4.addWidget(self.lights_color_bttn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 2, 1, 1)

        self.tabWidget.addTab(self.lights_tab, "")
        self.temperature_tab = QWidget()
        self.temperature_tab.setObjectName(u"temperature_tab")
        self.temperature_tab.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(34, 34, 34, 255))")
        self.gridLayout_13 = QGridLayout(self.temperature_tab)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.verticalSpacer_6, 4, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.temperature_display = QLabel(self.temperature_tab)
        self.temperature_display.setObjectName(u"temperature_display")
        sizePolicy1.setHeightForWidth(self.temperature_display.sizePolicy().hasHeightForWidth())
        self.temperature_display.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(40)
        font3.setBold(True)
        self.temperature_display.setFont(font3)
        self.temperature_display.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.temperature_display, 1, 2, 1, 1)

        self.temperature_down = QPushButton(self.temperature_tab)
        self.temperature_down.setObjectName(u"temperature_down")
        sizePolicy1.setHeightForWidth(self.temperature_down.sizePolicy().hasHeightForWidth())
        self.temperature_down.setSizePolicy(sizePolicy1)
        self.temperature_down.setFont(font1)
        self.temperature_down.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border: 0px solid black;")
        icon = QIcon()
        icon.addFile(u"resources/icons/left-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.temperature_down.setIcon(icon)
        self.temperature_down.setIconSize(QSize(100, 100))

        self.gridLayout_14.addWidget(self.temperature_down, 1, 1, 2, 1)

        self.temperature_up = QPushButton(self.temperature_tab)
        self.temperature_up.setObjectName(u"temperature_up")
        sizePolicy1.setHeightForWidth(self.temperature_up.sizePolicy().hasHeightForWidth())
        self.temperature_up.setSizePolicy(sizePolicy1)
        self.temperature_up.setFont(font1)
        self.temperature_up.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border: 0px solid black;")
        icon1 = QIcon()
        icon1.addFile(u"resources/icons/right-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.temperature_up.setIcon(icon1)
        self.temperature_up.setIconSize(QSize(100, 100))

        self.gridLayout_14.addWidget(self.temperature_up, 1, 3, 2, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.verticalSpacer_5, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.temperature_tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(25)
        font4.setBold(True)
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border: 0px solid black;")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.temperature_tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setFont(font4)
        self.pushButton_6.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border: 0px solid black;")

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.temperature_tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setFont(font4)
        self.pushButton_5.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border: 0px solid black;")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_3 = QPushButton(self.temperature_tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border: 0px solid black;")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.gridLayout_14.addLayout(self.horizontalLayout, 2, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_10, 1, 4, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_14, 1, 0, 1, 3)

        self.label_5 = QLabel(self.temperature_tab)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setFamilies([u"Sans"])
        font5.setPointSize(40)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"background: rgba(0,0,0,0);")

        self.gridLayout_13.addWidget(self.label_5, 0, 0, 1, 1)

        self.light_location_selector_3 = QComboBox(self.temperature_tab)
        self.light_location_selector_3.setObjectName(u"light_location_selector_3")
        self.light_location_selector_3.setFont(font1)
        self.light_location_selector_3.setStyleSheet(u"QComboBox{\n"
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
"	image: url(/home/debian/gui_licenta/resources/icons/down-arrow.svg);\n"
"	width: 30px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"")

        self.gridLayout_13.addWidget(self.light_location_selector_3, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.tabWidget.addTab(self.temperature_tab, "")
        self.camera_tab = QWidget()
        self.camera_tab.setObjectName(u"camera_tab")
        self.camera_tab.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(34, 34, 34, 255))")
        self.gridLayout_6 = QGridLayout(self.camera_tab)
        self.gridLayout_6.setSpacing(20)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.camera_location_selector = QComboBox(self.camera_tab)
        self.camera_location_selector.setObjectName(u"camera_location_selector")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.camera_location_selector.sizePolicy().hasHeightForWidth())
        self.camera_location_selector.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setPointSize(40)
        font6.setBold(False)
        self.camera_location_selector.setFont(font6)
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
"	image: url(/home/debian/gui_licenta/resources/icons/down-arrow.svg);\n"
"	width: 30px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.camera_location_selector, 0, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(15)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(200, 0, 200, 0)
        self.camera_bttn_up = QPushButton(self.camera_tab)
        self.camera_bttn_up.setObjectName(u"camera_bttn_up")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.camera_bttn_up.sizePolicy().hasHeightForWidth())
        self.camera_bttn_up.setSizePolicy(sizePolicy3)
        self.camera_bttn_up.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 30px;\n"
"background: rgba(0,0,0,0,);\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"resources/icons/up-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_bttn_up.setIcon(icon2)
        self.camera_bttn_up.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.camera_bttn_up, 0, 1, 1, 1)

        self.camera_bttn_down = QPushButton(self.camera_tab)
        self.camera_bttn_down.setObjectName(u"camera_bttn_down")
        sizePolicy3.setHeightForWidth(self.camera_bttn_down.sizePolicy().hasHeightForWidth())
        self.camera_bttn_down.setSizePolicy(sizePolicy3)
        self.camera_bttn_down.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 30px;\n"
"background: rgba(0,0,0,0,);\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"resources/icons/down-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_bttn_down.setIcon(icon3)
        self.camera_bttn_down.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.camera_bttn_down, 2, 1, 1, 1)

        self.camera_bttn_right = QPushButton(self.camera_tab)
        self.camera_bttn_right.setObjectName(u"camera_bttn_right")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.camera_bttn_right.sizePolicy().hasHeightForWidth())
        self.camera_bttn_right.setSizePolicy(sizePolicy4)
        self.camera_bttn_right.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 30px;\n"
"background: rgba(0,0,0,0,);\n"
"\n"
"")
        self.camera_bttn_right.setIcon(icon1)
        self.camera_bttn_right.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.camera_bttn_right, 1, 2, 1, 1)

        self.camera_display = QLabel(self.camera_tab)
        self.camera_display.setObjectName(u"camera_display")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.camera_display.sizePolicy().hasHeightForWidth())
        self.camera_display.setSizePolicy(sizePolicy5)
        self.camera_display.setStyleSheet(u"background: rgba(0,0,0,0);")

        self.gridLayout_5.addWidget(self.camera_display, 1, 1, 1, 1)

        self.camera_bttn_left = QPushButton(self.camera_tab)
        self.camera_bttn_left.setObjectName(u"camera_bttn_left")
        sizePolicy4.setHeightForWidth(self.camera_bttn_left.sizePolicy().hasHeightForWidth())
        self.camera_bttn_left.setSizePolicy(sizePolicy4)
        self.camera_bttn_left.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 30px;\n"
"background: rgba(0,0,0,0,);\n"
"\n"
"")
        self.camera_bttn_left.setIcon(icon)
        self.camera_bttn_left.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.camera_bttn_left, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 3)

        self.label_12 = QLabel(self.camera_tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"border: 0px solid white;\n"
"border-radius: 30px;\n"
"background: rgba(0,0,0,0,);\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 1)

        self.tabWidget.addTab(self.camera_tab, "")
        self.devices_tab = QWidget()
        self.devices_tab.setObjectName(u"devices_tab")
        self.devices_tab.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(34, 34, 34, 255))")
        self.tabWidget.addTab(self.devices_tab, "")
        self.security_tab = QWidget()
        self.security_tab.setObjectName(u"security_tab")
        self.security_tab.setStyleSheet(u"background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(34, 34, 34, 255))")
        self.gridLayout_8 = QGridLayout(self.security_tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(576, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(576, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_14 = QLabel(self.security_tab)
        self.label_14.setObjectName(u"label_14")
        font7 = QFont()
        font7.setPointSize(20)
        self.label_14.setFont(font7)

        self.verticalLayout_2.addWidget(self.label_14)

        self.scrollArea = QScrollArea(self.security_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 935, 422))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_3.addWidget(self.label_15)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.gridLayout_8.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.user_camera_preview = QLabel(self.security_tab)
        self.user_camera_preview.setObjectName(u"user_camera_preview")

        self.verticalLayout_5.addWidget(self.user_camera_preview)

        self.username_entry = QLineEdit(self.security_tab)
        self.username_entry.setObjectName(u"username_entry")
        font8 = QFont()
        font8.setFamilies([u"Ubuntu Sans"])
        font8.setPointSize(50)
        self.username_entry.setFont(font8)
        self.username_entry.setStyleSheet(u"\n"
"border: 0px solid black;\n"
"\n"
"padding:10px;\n"
"margin:5px;")

        self.verticalLayout_5.addWidget(self.username_entry)

        self.add_user_bttn = QPushButton(self.security_tab)
        self.add_user_bttn.setObjectName(u"add_user_bttn")
        font9 = QFont()
        font9.setPointSize(50)
        self.add_user_bttn.setFont(font9)
        self.add_user_bttn.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"border: 0px solid black;\n"
"\n"
"padding:10px;\n"
"margin:5px;")

        self.verticalLayout_5.addWidget(self.add_user_bttn)

        self.remove_user_bttn = QPushButton(self.security_tab)
        self.remove_user_bttn.setObjectName(u"remove_user_bttn")
        self.remove_user_bttn.setFont(font9)
        self.remove_user_bttn.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"border: 0px solid black;\n"
"\n"
"padding:10px;\n"
"margin:5px;")

        self.verticalLayout_5.addWidget(self.remove_user_bttn)


        self.gridLayout_8.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.tabWidget.addTab(self.security_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.clock_display.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Light source", None))
        self.lights_on_bttn.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.lights_off_bttn.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.lights_color_bttn.setText(QCoreApplication.translate("MainWindow", u"Choose\n"
"Color", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lights_tab), QCoreApplication.translate("MainWindow", u"Lights", None))
        self.temperature_display.setStyleSheet(QCoreApplication.translate("MainWindow", u"background: rgba(0,0,0,0);\n"
"border: 0px solid black;", None))
        self.temperature_display.setText(QCoreApplication.translate("MainWindow", u"22\u00b0C", None))
        self.temperature_down.setText("")
        self.temperature_up.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Hot", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Cold", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Dry", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Turbo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.temperature_tab), QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.camera_bttn_up.setText("")
        self.camera_bttn_down.setText("")
        self.camera_bttn_right.setText("")
        self.camera_display.setText("")
        self.camera_bttn_left.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.camera_tab), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.devices_tab), QCoreApplication.translate("MainWindow", u"Devices", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.user_camera_preview.setText("")
        self.add_user_bttn.setText(QCoreApplication.translate("MainWindow", u"ADD User", None))
        self.remove_user_bttn.setText(QCoreApplication.translate("MainWindow", u"REMOVE User", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.security_tab), QCoreApplication.translate("MainWindow", u"Security", None))
    # retranslateUi

