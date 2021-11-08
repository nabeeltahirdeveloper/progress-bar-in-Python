# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPaAxCR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 442)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(117, 14, 50, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"color:#fff;\n"
"border:none;")
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamily(u"Rage Italic")
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:#fff; background:none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.main_container_frame = QFrame(self.tab)
        self.main_container_frame.setObjectName(u"main_container_frame")
        self.main_container_frame.setStyleSheet(u"background:none; color: #fff;")
        self.main_container_frame.setFrameShape(QFrame.NoFrame)
        self.main_container_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_container_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.main_container_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_2 = QLabel(self.main_container_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_4 = QLabel(self.main_container_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.progress_1_cont = QFrame(self.main_container_frame)
        self.progress_1_cont.setObjectName(u"progress_1_cont")
        self.progress_1_cont.setMinimumSize(QSize(200, 200))
        self.progress_1_cont.setMaximumSize(QSize(200, 200))
        self.progress_1_cont.setStyleSheet(u"QFrame{\n"
"border: 3px solid;\n"
"border-radius: 100;\n"
"border-color: transparent;\n"
"}")
        self.progress_1_cont.setFrameShape(QFrame.NoFrame)
        self.progress_1_cont.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.progress_1_cont)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progress_1 = roundProgressBar(self.progress_1_cont)
        self.progress_1.setObjectName(u"progress_1")

        self.horizontalLayout.addWidget(self.progress_1)


        self.gridLayout.addWidget(self.progress_1_cont, 1, 0, 1, 1)

        self.progress_2_cont = QFrame(self.main_container_frame)
        self.progress_2_cont.setObjectName(u"progress_2_cont")
        self.progress_2_cont.setMinimumSize(QSize(200, 200))
        self.progress_2_cont.setMaximumSize(QSize(200, 200))
        self.progress_2_cont.setStyleSheet(u"QFrame{\n"
"border: 3px solid;\n"
"border-color: transparent;\n"
"border-radius: 100;\n"
"}")
        self.progress_2_cont.setFrameShape(QFrame.NoFrame)
        self.progress_2_cont.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.progress_2_cont)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.progress_2 = roundProgressBar(self.progress_2_cont)
        self.progress_2.setObjectName(u"progress_2")

        self.horizontalLayout_2.addWidget(self.progress_2)


        self.gridLayout.addWidget(self.progress_2_cont, 1, 1, 1, 1)

        self.progress_3_cont = QFrame(self.main_container_frame)
        self.progress_3_cont.setObjectName(u"progress_3_cont")
        self.progress_3_cont.setMinimumSize(QSize(200, 200))
        self.progress_3_cont.setMaximumSize(QSize(200, 200))
        self.progress_3_cont.setStyleSheet(u"QFrame{\n"
"border: 3px solid;\n"
"border-color: transparent;\n"
"border-radius: 100;\n"
"}")
        self.progress_3_cont.setFrameShape(QFrame.NoFrame)
        self.progress_3_cont.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.progress_3_cont)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progress_3 = roundProgressBar(self.progress_3_cont)
        self.progress_3.setObjectName(u"progress_3")

        self.horizontalLayout_3.addWidget(self.progress_3)


        self.gridLayout.addWidget(self.progress_3_cont, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.main_container_frame)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 100))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color:#fff; background:none;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.main_container_frame_2 = QFrame(self.tab_2)
        self.main_container_frame_2.setObjectName(u"main_container_frame_2")
        self.main_container_frame_2.setStyleSheet(u"background:none; color: #fff;")
        self.main_container_frame_2.setFrameShape(QFrame.NoFrame)
        self.main_container_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.main_container_frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.main_container_frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.main_container_frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_8 = QLabel(self.main_container_frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)

        self.progress_1_cont_2 = QFrame(self.main_container_frame_2)
        self.progress_1_cont_2.setObjectName(u"progress_1_cont_2")
        self.progress_1_cont_2.setMinimumSize(QSize(200, 200))
        self.progress_1_cont_2.setMaximumSize(QSize(200, 200))
        self.progress_1_cont_2.setStyleSheet(u"QFrame{\n"
"border: 3px solid;\n"
"border-radius: 100;\n"
"border-color: transparent;\n"
"}")
        self.progress_1_cont_2.setFrameShape(QFrame.NoFrame)
        self.progress_1_cont_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.progress_1_cont_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.progress_4 = spiralProgressBar(self.progress_1_cont_2)
        self.progress_4.setObjectName(u"progress_4")

        self.horizontalLayout_4.addWidget(self.progress_4)


        self.gridLayout_2.addWidget(self.progress_1_cont_2, 1, 0, 1, 1)

        self.progress_2_cont_2 = QFrame(self.main_container_frame_2)
        self.progress_2_cont_2.setObjectName(u"progress_2_cont_2")
        self.progress_2_cont_2.setMinimumSize(QSize(200, 200))
        self.progress_2_cont_2.setMaximumSize(QSize(200, 200))
        self.progress_2_cont_2.setStyleSheet(u"QFrame{\n"
"border: 3px solid;\n"
"border-color: transparent;\n"
"border-radius: 100;\n"
"}")
        self.progress_2_cont_2.setFrameShape(QFrame.NoFrame)
        self.progress_2_cont_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.progress_2_cont_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.progress_5 = spiralProgressBar(self.progress_2_cont_2)
        self.progress_5.setObjectName(u"progress_5")

        self.horizontalLayout_5.addWidget(self.progress_5)


        self.gridLayout_2.addWidget(self.progress_2_cont_2, 1, 1, 1, 1)

        self.progress_3_cont_2 = QFrame(self.main_container_frame_2)
        self.progress_3_cont_2.setObjectName(u"progress_3_cont_2")
        self.progress_3_cont_2.setMinimumSize(QSize(200, 200))
        self.progress_3_cont_2.setMaximumSize(QSize(200, 200))
        self.progress_3_cont_2.setStyleSheet(u"QFrame{\n"
"border: 3px solid;\n"
"border-color: transparent;\n"
"border-radius: 100;\n"
"}")
        self.progress_3_cont_2.setFrameShape(QFrame.NoFrame)
        self.progress_3_cont_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.progress_3_cont_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.progress_6 = spiralProgressBar(self.progress_3_cont_2)
        self.progress_6.setObjectName(u"progress_6")

        self.horizontalLayout_6.addWidget(self.progress_6)


        self.gridLayout_2.addWidget(self.progress_3_cont_2, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.main_container_frame_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Circular Progress Bars", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Progress 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Progress 2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Progress 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Circular Progressbars", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Spiral Progress Bars", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Progress 1", None))
        # self.label_7.setText(QCoreApplication.translate("MainWindow", u"Progress 2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Progress 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Spiral Progressbars", None))
    # retranslateUi

