# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_picker.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(682, 600)
        MainWindow.setStyleSheet(u"background: #1b1b1b; color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background: #282828; color: white;")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.exit_button = QPushButton(self.widget)
        self.exit_button.setObjectName(u"exit_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.setStyleSheet(u"border: 0px solid black;")
        icon = QIcon()
        icon.addFile(u"resources/icons/left-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.exit_button, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.bttn_00ff00 = QPushButton(self.widget)
        self.bttn_00ff00.setObjectName(u"bttn_00ff00")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bttn_00ff00.sizePolicy().hasHeightForWidth())
        self.bttn_00ff00.setSizePolicy(sizePolicy1)
        self.bttn_00ff00.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"background: #00ff00;\n"
"borde")

        self.horizontalLayout_12.addWidget(self.bttn_00ff00)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.bttn_00ff55 = QPushButton(self.widget)
        self.bttn_00ff55.setObjectName(u"bttn_00ff55")
        sizePolicy1.setHeightForWidth(self.bttn_00ff55.sizePolicy().hasHeightForWidth())
        self.bttn_00ff55.setSizePolicy(sizePolicy1)
        self.bttn_00ff55.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #00ff55")

        self.horizontalLayout_11.addWidget(self.bttn_00ff55)

        self.bttn_55ff00 = QPushButton(self.widget)
        self.bttn_55ff00.setObjectName(u"bttn_55ff00")
        sizePolicy1.setHeightForWidth(self.bttn_55ff00.sizePolicy().hasHeightForWidth())
        self.bttn_55ff00.setSizePolicy(sizePolicy1)
        self.bttn_55ff00.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #55ff00")

        self.horizontalLayout_11.addWidget(self.bttn_55ff00)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.bttn_00ffaa = QPushButton(self.widget)
        self.bttn_00ffaa.setObjectName(u"bttn_00ffaa")
        sizePolicy1.setHeightForWidth(self.bttn_00ffaa.sizePolicy().hasHeightForWidth())
        self.bttn_00ffaa.setSizePolicy(sizePolicy1)
        self.bttn_00ffaa.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #00ffaa")

        self.horizontalLayout_10.addWidget(self.bttn_00ffaa)

        self.bttn_55ff55 = QPushButton(self.widget)
        self.bttn_55ff55.setObjectName(u"bttn_55ff55")
        sizePolicy1.setHeightForWidth(self.bttn_55ff55.sizePolicy().hasHeightForWidth())
        self.bttn_55ff55.setSizePolicy(sizePolicy1)
        self.bttn_55ff55.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #55ff55")

        self.horizontalLayout_10.addWidget(self.bttn_55ff55)

        self.bttn_aaff00 = QPushButton(self.widget)
        self.bttn_aaff00.setObjectName(u"bttn_aaff00")
        sizePolicy1.setHeightForWidth(self.bttn_aaff00.sizePolicy().hasHeightForWidth())
        self.bttn_aaff00.setSizePolicy(sizePolicy1)
        self.bttn_aaff00.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #aaff00")

        self.horizontalLayout_10.addWidget(self.bttn_aaff00)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.bttn_00ffff = QPushButton(self.widget)
        self.bttn_00ffff.setObjectName(u"bttn_00ffff")
        sizePolicy1.setHeightForWidth(self.bttn_00ffff.sizePolicy().hasHeightForWidth())
        self.bttn_00ffff.setSizePolicy(sizePolicy1)
        self.bttn_00ffff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #00ffff")

        self.horizontalLayout_9.addWidget(self.bttn_00ffff)

        self.bttn_55ffaa = QPushButton(self.widget)
        self.bttn_55ffaa.setObjectName(u"bttn_55ffaa")
        sizePolicy1.setHeightForWidth(self.bttn_55ffaa.sizePolicy().hasHeightForWidth())
        self.bttn_55ffaa.setSizePolicy(sizePolicy1)
        self.bttn_55ffaa.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #55ffaa")

        self.horizontalLayout_9.addWidget(self.bttn_55ffaa)

        self.bttn_aaff55 = QPushButton(self.widget)
        self.bttn_aaff55.setObjectName(u"bttn_aaff55")
        sizePolicy1.setHeightForWidth(self.bttn_aaff55.sizePolicy().hasHeightForWidth())
        self.bttn_aaff55.setSizePolicy(sizePolicy1)
        self.bttn_aaff55.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #aaff55")

        self.horizontalLayout_9.addWidget(self.bttn_aaff55)

        self.bttn_ffff00 = QPushButton(self.widget)
        self.bttn_ffff00.setObjectName(u"bttn_ffff00")
        sizePolicy1.setHeightForWidth(self.bttn_ffff00.sizePolicy().hasHeightForWidth())
        self.bttn_ffff00.setSizePolicy(sizePolicy1)
        self.bttn_ffff00.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ffff00")

        self.horizontalLayout_9.addWidget(self.bttn_ffff00)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.bttn_00aaff = QPushButton(self.widget)
        self.bttn_00aaff.setObjectName(u"bttn_00aaff")
        sizePolicy1.setHeightForWidth(self.bttn_00aaff.sizePolicy().hasHeightForWidth())
        self.bttn_00aaff.setSizePolicy(sizePolicy1)
        self.bttn_00aaff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #00aaff")

        self.horizontalLayout_8.addWidget(self.bttn_00aaff)

        self.bttn_aaffff = QPushButton(self.widget)
        self.bttn_aaffff.setObjectName(u"bttn_aaffff")
        sizePolicy1.setHeightForWidth(self.bttn_aaffff.sizePolicy().hasHeightForWidth())
        self.bttn_aaffff.setSizePolicy(sizePolicy1)
        self.bttn_aaffff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #aaffff")

        self.horizontalLayout_8.addWidget(self.bttn_aaffff)

        self.bttn_ffffff = QPushButton(self.widget)
        self.bttn_ffffff.setObjectName(u"bttn_ffffff")
        sizePolicy1.setHeightForWidth(self.bttn_ffffff.sizePolicy().hasHeightForWidth())
        self.bttn_ffffff.setSizePolicy(sizePolicy1)
        self.bttn_ffffff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ffffff")

        self.horizontalLayout_8.addWidget(self.bttn_ffffff)

        self.bttn_ffffaa = QPushButton(self.widget)
        self.bttn_ffffaa.setObjectName(u"bttn_ffffaa")
        sizePolicy1.setHeightForWidth(self.bttn_ffffaa.sizePolicy().hasHeightForWidth())
        self.bttn_ffffaa.setSizePolicy(sizePolicy1)
        self.bttn_ffffaa.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ffffaa")

        self.horizontalLayout_8.addWidget(self.bttn_ffffaa)

        self.bttn_ffaa00 = QPushButton(self.widget)
        self.bttn_ffaa00.setObjectName(u"bttn_ffaa00")
        sizePolicy1.setHeightForWidth(self.bttn_ffaa00.sizePolicy().hasHeightForWidth())
        self.bttn_ffaa00.setSizePolicy(sizePolicy1)
        self.bttn_ffaa00.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ffaa00")

        self.horizontalLayout_8.addWidget(self.bttn_ffaa00)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.bttn_0055ff = QPushButton(self.widget)
        self.bttn_0055ff.setObjectName(u"bttn_0055ff")
        sizePolicy1.setHeightForWidth(self.bttn_0055ff.sizePolicy().hasHeightForWidth())
        self.bttn_0055ff.setSizePolicy(sizePolicy1)
        self.bttn_0055ff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #0055ff")

        self.horizontalLayout_7.addWidget(self.bttn_0055ff)

        self.bttn_55aaff = QPushButton(self.widget)
        self.bttn_55aaff.setObjectName(u"bttn_55aaff")
        sizePolicy1.setHeightForWidth(self.bttn_55aaff.sizePolicy().hasHeightForWidth())
        self.bttn_55aaff.setSizePolicy(sizePolicy1)
        self.bttn_55aaff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #55aaff")

        self.horizontalLayout_7.addWidget(self.bttn_55aaff)

        self.bttn_aaaaff = QPushButton(self.widget)
        self.bttn_aaaaff.setObjectName(u"bttn_aaaaff")
        sizePolicy1.setHeightForWidth(self.bttn_aaaaff.sizePolicy().hasHeightForWidth())
        self.bttn_aaaaff.setSizePolicy(sizePolicy1)
        self.bttn_aaaaff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #aaaaff")

        self.horizontalLayout_7.addWidget(self.bttn_aaaaff)

        self.bttn_ffaaaa = QPushButton(self.widget)
        self.bttn_ffaaaa.setObjectName(u"bttn_ffaaaa")
        sizePolicy1.setHeightForWidth(self.bttn_ffaaaa.sizePolicy().hasHeightForWidth())
        self.bttn_ffaaaa.setSizePolicy(sizePolicy1)
        self.bttn_ffaaaa.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ffaaaa")

        self.horizontalLayout_7.addWidget(self.bttn_ffaaaa)

        self.bttn_ffaa55 = QPushButton(self.widget)
        self.bttn_ffaa55.setObjectName(u"bttn_ffaa55")
        sizePolicy1.setHeightForWidth(self.bttn_ffaa55.sizePolicy().hasHeightForWidth())
        self.bttn_ffaa55.setSizePolicy(sizePolicy1)
        self.bttn_ffaa55.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ffaa55")

        self.horizontalLayout_7.addWidget(self.bttn_ffaa55)

        self.bttn_ff5500 = QPushButton(self.widget)
        self.bttn_ff5500.setObjectName(u"bttn_ff5500")
        sizePolicy1.setHeightForWidth(self.bttn_ff5500.sizePolicy().hasHeightForWidth())
        self.bttn_ff5500.setSizePolicy(sizePolicy1)
        self.bttn_ff5500.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ff5500")

        self.horizontalLayout_7.addWidget(self.bttn_ff5500)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)

        self.bttn_0000ff = QPushButton(self.widget)
        self.bttn_0000ff.setObjectName(u"bttn_0000ff")
        sizePolicy1.setHeightForWidth(self.bttn_0000ff.sizePolicy().hasHeightForWidth())
        self.bttn_0000ff.setSizePolicy(sizePolicy1)
        self.bttn_0000ff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #0000ff")

        self.horizontalLayout_6.addWidget(self.bttn_0000ff)

        self.bttn_5500ff = QPushButton(self.widget)
        self.bttn_5500ff.setObjectName(u"bttn_5500ff")
        sizePolicy1.setHeightForWidth(self.bttn_5500ff.sizePolicy().hasHeightForWidth())
        self.bttn_5500ff.setSizePolicy(sizePolicy1)
        self.bttn_5500ff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #5500ff")

        self.horizontalLayout_6.addWidget(self.bttn_5500ff)

        self.bttn_aa00ff = QPushButton(self.widget)
        self.bttn_aa00ff.setObjectName(u"bttn_aa00ff")
        sizePolicy1.setHeightForWidth(self.bttn_aa00ff.sizePolicy().hasHeightForWidth())
        self.bttn_aa00ff.setSizePolicy(sizePolicy1)
        self.bttn_aa00ff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #aa00ff")

        self.horizontalLayout_6.addWidget(self.bttn_aa00ff)

        self.bttn_ff00ff = QPushButton(self.widget)
        self.bttn_ff00ff.setObjectName(u"bttn_ff00ff")
        sizePolicy1.setHeightForWidth(self.bttn_ff00ff.sizePolicy().hasHeightForWidth())
        self.bttn_ff00ff.setSizePolicy(sizePolicy1)
        self.bttn_ff00ff.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ff00ff")

        self.horizontalLayout_6.addWidget(self.bttn_ff00ff)

        self.bttn_ff00aa = QPushButton(self.widget)
        self.bttn_ff00aa.setObjectName(u"bttn_ff00aa")
        sizePolicy1.setHeightForWidth(self.bttn_ff00aa.sizePolicy().hasHeightForWidth())
        self.bttn_ff00aa.setSizePolicy(sizePolicy1)
        self.bttn_ff00aa.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ff00aa")

        self.horizontalLayout_6.addWidget(self.bttn_ff00aa)

        self.bttn_ff0055 = QPushButton(self.widget)
        self.bttn_ff0055.setObjectName(u"bttn_ff0055")
        sizePolicy1.setHeightForWidth(self.bttn_ff0055.sizePolicy().hasHeightForWidth())
        self.bttn_ff0055.setSizePolicy(sizePolicy1)
        self.bttn_ff0055.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ff0055")

        self.horizontalLayout_6.addWidget(self.bttn_ff0055)

        self.bttn_ff0000 = QPushButton(self.widget)
        self.bttn_ff0000.setObjectName(u"bttn_ff0000")
        sizePolicy1.setHeightForWidth(self.bttn_ff0000.sizePolicy().hasHeightForWidth())
        self.bttn_ff0000.setSizePolicy(sizePolicy1)
        self.bttn_ff0000.setStyleSheet(u"min-width: 80px;\n"
"border: 0px solid 3f3f3f;\n"
"margin: 0px;\n"
"background: #ff0000")

        self.horizontalLayout_6.addWidget(self.bttn_ff0000)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 4)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 3)


        self.gridLayout_2.addWidget(self.widget, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.exit_button.setText("")
        self.bttn_00ff00.setText("")
        self.bttn_00ff55.setText("")
        self.bttn_55ff00.setText("")
        self.bttn_00ffaa.setText("")
        self.bttn_55ff55.setText("")
        self.bttn_aaff00.setText("")
        self.bttn_00ffff.setText("")
        self.bttn_55ffaa.setText("")
        self.bttn_aaff55.setText("")
        self.bttn_ffff00.setText("")
        self.bttn_00aaff.setText("")
        self.bttn_aaffff.setText("")
        self.bttn_ffffff.setText("")
        self.bttn_ffffaa.setText("")
        self.bttn_ffaa00.setText("")
        self.bttn_0055ff.setText("")
        self.bttn_55aaff.setText("")
        self.bttn_aaaaff.setText("")
        self.bttn_ffaaaa.setText("")
        self.bttn_ffaa55.setText("")
        self.bttn_ff5500.setText("")
        self.bttn_0000ff.setText("")
        self.bttn_5500ff.setText("")
        self.bttn_aa00ff.setText("")
        self.bttn_ff00ff.setText("")
        self.bttn_ff00aa.setText("")
        self.bttn_ff0055.setText("")
        self.bttn_ff0000.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Color Picker", None))
    # retranslateUi

