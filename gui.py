# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import threading

from strategics import Strategics
from ImageTriggers import ImageTriggers

from PyQt5 import QtCore, QtWidgets, QtGui


class MyThread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.bot = Strategics('global')
        self.farm = False

    def run(self):
        if self.farm:
            self.farm = False
            self.bot.stopFarm()
        else:
            self.farm = True
            threading.Thread(target=self.bot.startFarm).start()


class Ui_MainWindow(object):
    mySignal = QtCore.pyqtSignal(str)

    def __init__(self):
        self.farm = False
        self._textBrowser = ''
        self._textBrowser_2 = ''
        self._textBrowser_3 = ''
        self.thread = MyThread()
        self.bot = self.thread.bot

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 615)
        MainWindow.setFixedSize(440, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 421, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.Log = QtWidgets.QWidget()
        self.Log.setMinimumSize(QtCore.QSize(0, 571))
        self.Log.setObjectName("Log")
        self.pushButton = QtWidgets.QPushButton(self.Log)
        self.pushButton.setGeometry(QtCore.QRect(20, 420, 182, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Log)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 490, 91, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Log)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 490, 91, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.Log)
        self.textBrowser.setGeometry(QtCore.QRect(210, 440, 191, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.Log)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 291, 381, 111))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.Log)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 30, 381, 231))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_2 = QtWidgets.QLabel(self.Log)
        self.label_2.setGeometry(QtCore.QRect(210, 420, 191, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Log)
        self.label_3.setGeometry(QtCore.QRect(20, 270, 381, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Log)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 381, 20))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.Log, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setGeometry(QtCore.QRect(10, 55, 181, 41))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 100, 181, 41))
        self.checkBox_2.setObjectName("checkBox_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(200, 30, 201, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(200, 100, 201, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(200, 160, 201, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 145, 151, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(200, 145, 211, 16))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox.setGeometry(QtCore.QRect(20, 70, 111, 25))
        self.spinBox.setObjectName("spinBox")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(170, 30, 231, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(170, 80, 211, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(170, 130, 211, 16))
        self.label_11.setObjectName("label_11")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_2.setGeometry(QtCore.QRect(20, 120, 111, 25))
        self.spinBox_2.setObjectName("spinBox_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 10, 71, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 10, 71, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_8.setGeometry(QtCore.QRect(250, 10, 71, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_9.setGeometry(QtCore.QRect(330, 10, 71, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_11.setGeometry(QtCore.QRect(90, 50, 71, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_12.setGeometry(QtCore.QRect(170, 50, 71, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_13.setGeometry(QtCore.QRect(250, 50, 71, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_14.setGeometry(QtCore.QRect(330, 50, 71, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 90, 71, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_16.setGeometry(QtCore.QRect(90, 90, 71, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_17.setGeometry(QtCore.QRect(170, 90, 71, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_18.setGeometry(QtCore.QRect(250, 90, 71, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_19.setGeometry(QtCore.QRect(330, 90, 71, 31))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_20.setGeometry(QtCore.QRect(10, 130, 71, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_21.setGeometry(QtCore.QRect(90, 130, 71, 31))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_22.setGeometry(QtCore.QRect(170, 130, 71, 31))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_23.setGeometry(QtCore.QRect(250, 130, 71, 31))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_24.setGeometry(QtCore.QRect(330, 130, 71, 31))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_25.setGeometry(QtCore.QRect(10, 170, 71, 31))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_26.setGeometry(QtCore.QRect(90, 170, 71, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_27.setGeometry(QtCore.QRect(170, 170, 71, 31))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_28.setGeometry(QtCore.QRect(250, 170, 71, 31))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_29.setGeometry(QtCore.QRect(330, 170, 71, 31))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_30.setGeometry(QtCore.QRect(10, 210, 71, 31))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_31.setGeometry(QtCore.QRect(90, 210, 71, 31))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_32.setGeometry(QtCore.QRect(170, 210, 71, 31))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_33.setGeometry(QtCore.QRect(250, 210, 71, 31))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_34.setGeometry(QtCore.QRect(330, 210, 71, 31))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_69 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_69.setGeometry(QtCore.QRect(250, 250, 71, 31))
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_70.setGeometry(QtCore.QRect(10, 250, 71, 31))
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_71 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_71.setGeometry(QtCore.QRect(90, 250, 71, 31))
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_72 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_72.setGeometry(QtCore.QRect(170, 250, 71, 31))
        self.pushButton_72.setObjectName("pushButton_72")
        self.pushButton_73 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_73.setGeometry(QtCore.QRect(250, 250, 71, 31))
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_74 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_74.setGeometry(QtCore.QRect(330, 250, 71, 31))
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_75.setGeometry(QtCore.QRect(10, 290, 71, 31))
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_76 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_76.setGeometry(QtCore.QRect(90, 290, 71, 31))
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_77 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_77.setGeometry(QtCore.QRect(170, 290, 71, 31))
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_78.setGeometry(QtCore.QRect(250, 290, 71, 31))
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_79 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_79.setGeometry(QtCore.QRect(330, 290, 71, 31))
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_80 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_80.setGeometry(QtCore.QRect(10, 330, 71, 31))
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_81 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_81.setGeometry(QtCore.QRect(90, 330, 71, 31))
        self.pushButton_81.setObjectName("pushButton_81")
        self.pushButton_82 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_82.setGeometry(QtCore.QRect(170, 330, 71, 31))
        self.pushButton_82.setObjectName("pushButton_82")
        self.pushButton_83 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_83.setGeometry(QtCore.QRect(250, 330, 71, 31))
        self.pushButton_83.setObjectName("pushButton_83")
        self.pushButton_84 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_84.setGeometry(QtCore.QRect(330, 330, 71, 31))
        self.pushButton_84.setObjectName("pushButton_84")
        self.pushButton_85 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_85.setGeometry(QtCore.QRect(10, 370, 71, 31))
        self.pushButton_85.setObjectName("pushButton_85")
        self.pushButton_86 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_86.setGeometry(QtCore.QRect(90, 370, 71, 31))
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_87 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_87.setGeometry(QtCore.QRect(170, 370, 71, 31))
        self.pushButton_87.setObjectName("pushButton_87")
        self.pushButton_88 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_88.setGeometry(QtCore.QRect(250, 370, 71, 31))
        self.pushButton_88.setObjectName("pushButton_88")
        self.pushButton_89 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_89.setGeometry(QtCore.QRect(330, 370, 71, 31))
        self.pushButton_89.setObjectName("pushButton_89")
        self.pushButton_90 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_90.setGeometry(QtCore.QRect(10, 410, 71, 31))
        self.pushButton_90.setObjectName("pushButton_90")
        self.pushButton_91 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_91.setGeometry(QtCore.QRect(90, 410, 71, 31))
        self.pushButton_91.setObjectName("pushButton_91")
        self.pushButton_92 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_92.setGeometry(QtCore.QRect(170, 410, 71, 31))
        self.pushButton_92.setObjectName("pushButton_92")
        self.pushButton_93 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_93.setGeometry(QtCore.QRect(250, 410, 71, 31))
        self.pushButton_93.setObjectName("pushButton_93")
        self.pushButton_99 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_99.setGeometry(QtCore.QRect(330, 410, 71, 31))
        self.pushButton_99.setObjectName("pushButton_99")
        self.pushButton_100 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_100.setGeometry(QtCore.QRect(10, 450, 71, 31))
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_101 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_101.setGeometry(QtCore.QRect(90, 450, 71, 31))
        self.pushButton_101.setObjectName("pushButton_101")
        self.pushButton_102 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_102.setGeometry(QtCore.QRect(170, 450, 71, 31))
        self.pushButton_102.setObjectName("pushButton_102")
        self.pushButton_103 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_103.setGeometry(QtCore.QRect(250, 450, 71, 31))
        self.pushButton_103.setObjectName("pushButton_103")
        self.pushButton_104 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_104.setGeometry(QtCore.QRect(330, 450, 71, 31))
        self.pushButton_104.setObjectName("pushButton_104")
        self.pushButton_105 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_105.setGeometry(QtCore.QRect(10, 490, 71, 31))
        self.pushButton_105.setObjectName("pushButton_105")
        self.pushButton_106 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_106.setGeometry(QtCore.QRect(90, 490, 71, 31))
        self.pushButton_106.setObjectName("pushButton_106")
        self.pushButton_107 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_107.setGeometry(QtCore.QRect(170, 490, 71, 31))
        self.pushButton_107.setObjectName("pushButton_107")
        self.pushButton_108 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_108.setGeometry(QtCore.QRect(250, 490, 71, 31))
        self.pushButton_108.setObjectName("pushButton_108")
        self.pushButton_109 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_109.setGeometry(QtCore.QRect(330, 490, 71, 31))
        self.pushButton_109.setObjectName("pushButton_109")
        self.pushButton_110 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_110.setGeometry(QtCore.QRect(10, 530, 71, 31))
        self.pushButton_110.setObjectName("pushButton_110")
        self.pushButton_111 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_111.setGeometry(QtCore.QRect(90, 530, 71, 31))
        self.pushButton_111.setObjectName("pushButton_111")
        self.pushButton_112 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_112.setGeometry(QtCore.QRect(170, 530, 71, 31))
        self.pushButton_112.setObjectName("pushButton_112")
        self.pushButton_113 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_113.setGeometry(QtCore.QRect(250, 530, 71, 31))
        self.pushButton_113.setObjectName("pushButton_113")
        self.pushButton_114 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_114.setGeometry(QtCore.QRect(330, 530, 71, 31))
        self.pushButton_114.setObjectName("pushButton_114")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 40, 381, 401))
        self.label.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Leninka Bot CR"))
        MainWindow.setWindowIcon(QtGui.QIcon('img/Leninka.ico'))
        self.pushButton.setText(_translate("MainWindow", "Старт"))
        self.pushButton.clicked.connect(lambda: self.startStopFarm())
        self.pushButton_2.setText(_translate("MainWindow", "Получить \nтриггер"))
        self.pushButton_2.clicked.connect(lambda: self.getTrigger())
        self.pushButton_3.setText(_translate("MainWindow", "Перезагрузить"))
        self.pushButton_3.clicked.connect(lambda: self.reboot())
        self.label_2.setText(_translate("MainWindow", "Статистика:"))
        self.label_3.setText(_translate("MainWindow", "Результаты боев:"))
        self.label_4.setText(_translate("MainWindow", "Лог событий:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Log), _translate("MainWindow", "Log"))
        self.checkBox.setText(_translate("MainWindow", "Открытие сундуков"))
        self.checkBox_2.setText(_translate("MainWindow", "Запрос карт"))
        self.label_5.setText(_translate("MainWindow", "Режим боя"))
        self.label_6.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", "Выбор карты запроса"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Настройки бота"))
        self.lineEdit.setText(_translate("MainWindow", "5555"))
        self.label_9.setText(_translate("MainWindow", "Укажите порт для adb server"))
        self.label_10.setText(_translate("MainWindow", "Колличество боев до перерыва"))
        self.label_11.setText(_translate("MainWindow", "Время перерыва ( в минутах ) "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Настройки adb"))
        self.pushButton_5.setText(_translate("MainWindow", "Open \nChest 1"))
        self.pushButton_6.setText(_translate("MainWindow", "Open \nChest 2"))
        self.pushButton_7.setText(_translate("MainWindow", "Open \nChest 3"))
        self.pushButton_8.setText(_translate("MainWindow", "Open \nChest 4"))
        self.pushButton_9.setText(_translate("MainWindow", "Return\nHome"))
        self.pushButton_10.setText(_translate("MainWindow", "Go To\nClan Chat"))
        self.pushButton_11.setText(_translate("MainWindow", "Open\Close\nClan Chat"))
        self.pushButton_12.setText(_translate("MainWindow", "Go To\nDeck"))
        self.pushButton_13.setText(_translate("MainWindow", "GoTo\nShop"))
        self.pushButton_14.setText(_translate("MainWindow", "Set English \nLanguage"))
        self.pushButton_15.setText(_translate("MainWindow", "Reboot"))
        self.pushButton_16.setText(_translate("MainWindow", "Open CR"))
        self.pushButton_17.setText(_translate("MainWindow", "Close CR"))
        self.pushButton_18.setText(_translate("MainWindow", "Swipe Card\nRequest"))
        self.pushButton_19.setText(_translate("MainWindow", "Request\nCard"))
        self.pushButton_20.setText(_translate("MainWindow", "reward\nLimit"))
        self.pushButton_21.setText(_translate("MainWindow", "run Battle\nGlobal"))
        self.pushButton_22.setText(_translate("MainWindow", "run Battle \n Mode 1"))
        self.pushButton_23.setText(_translate("MainWindow", "run Battle \n Mode 2"))
        self.pushButton_24.setText(_translate("MainWindow", "24"))
        self.pushButton_25.setText(_translate("MainWindow", "25"))
        self.pushButton_26.setText(_translate("MainWindow", "26"))
        self.pushButton_27.setText(_translate("MainWindow", "27"))
        self.pushButton_28.setText(_translate("MainWindow", "28"))
        self.pushButton_29.setText(_translate("MainWindow", "29"))
        self.pushButton_30.setText(_translate("MainWindow", "30"))
        self.pushButton_31.setText(_translate("MainWindow", "31"))
        self.pushButton_32.setText(_translate("MainWindow", "32"))
        self.pushButton_33.setText(_translate("MainWindow", "33"))
        self.pushButton_34.setText(_translate("MainWindow", "34"))
        self.pushButton_69.setText(_translate("MainWindow", "69"))
        self.pushButton_70.setText(_translate("MainWindow", "70"))
        self.pushButton_71.setText(_translate("MainWindow", "71"))
        self.pushButton_72.setText(_translate("MainWindow", "72"))
        self.pushButton_73.setText(_translate("MainWindow", "73"))
        self.pushButton_74.setText(_translate("MainWindow", "74"))
        self.pushButton_75.setText(_translate("MainWindow", "74"))
        self.pushButton_76.setText(_translate("MainWindow", "76"))
        self.pushButton_77.setText(_translate("MainWindow", "77"))
        self.pushButton_78.setText(_translate("MainWindow", "78"))
        self.pushButton_79.setText(_translate("MainWindow", "79"))
        self.pushButton_80.setText(_translate("MainWindow", "80"))
        self.pushButton_81.setText(_translate("MainWindow", "81"))
        self.pushButton_82.setText(_translate("MainWindow", "82"))
        self.pushButton_83.setText(_translate("MainWindow", "83"))
        self.pushButton_84.setText(_translate("MainWindow", "84"))
        self.pushButton_85.setText(_translate("MainWindow", "85"))
        self.pushButton_86.setText(_translate("MainWindow", "86"))
        self.pushButton_87.setText(_translate("MainWindow", "87"))
        self.pushButton_88.setText(_translate("MainWindow", "88"))
        self.pushButton_89.setText(_translate("MainWindow", "89"))
        self.pushButton_90.setText(_translate("MainWindow", "90"))
        self.pushButton_91.setText(_translate("MainWindow", "91"))
        self.pushButton_92.setText(_translate("MainWindow", "92"))
        self.pushButton_93.setText(_translate("MainWindow", "93"))
        self.pushButton_99.setText(_translate("MainWindow", "99"))
        self.pushButton_100.setText(_translate("MainWindow", "100"))
        self.pushButton_101.setText(_translate("MainWindow", "101"))
        self.pushButton_102.setText(_translate("MainWindow", "102"))
        self.pushButton_103.setText(_translate("MainWindow", "103"))
        self.pushButton_104.setText(_translate("MainWindow", "104"))
        self.pushButton_105.setText(_translate("MainWindow", "105"))
        self.pushButton_106.setText(_translate("MainWindow", "106"))
        self.pushButton_107.setText(_translate("MainWindow", "107"))
        self.pushButton_108.setText(_translate("MainWindow", "108"))
        self.pushButton_109.setText(_translate("MainWindow", "109"))
        self.pushButton_110.setText(_translate("MainWindow", "110"))
        self.pushButton_111.setText(_translate("MainWindow", "111"))
        self.pushButton_112.setText(_translate("MainWindow", "112"))
        self.pushButton_113.setText(_translate("MainWindow", "113"))
        self.pushButton_114.setText(_translate("MainWindow", "114"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Дебаг"))
        self.label.setText(_translate("MainWindow", "<body><p>Бот для фарма корон в Clash Royale</p><p>BugReport: t.me/leninka20</p></body>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "О программе"))

    def debugButton(self):
        self.pushButton_5.clicked.connect(lambda: self.bot.bot.openChest(1))
        self.pushButton_6.clicked.connect(lambda: self.bot.bot.openChest(2))
        self.pushButton_7.clicked.connect(lambda: self.bot.bot.openChest(3))
        self.pushButton_8.clicked.connect(lambda: self.bot.bot.openChest(4))
        self.pushButton_9.clicked.connect(lambda: self.bot.bot.returnHome())
        self.pushButton_10.clicked.connect(lambda: self.bot.bot.goToClanChat())
        self.pushButton_11.clicked.connect(lambda: self.bot.bot.openCloseClanChat())
        self.pushButton_12.clicked.connect(lambda: self.bot.bot.goToDeck())
        self.pushButton_13.clicked.connect(lambda: self.bot.bot.goToShop())
        self.pushButton_14.clicked.connect(lambda: self.bot.bot.setEnglishLanguage())
        self.pushButton_15.clicked.connect(lambda: self.bot.bot.reboot())
        self.pushButton_16.clicked.connect(lambda: self.bot.bot.openCR())
        self.pushButton_17.clicked.connect(lambda: self.bot.bot.closeCR())
        self.pushButton_18.clicked.connect(lambda: self.bot.bot.swipeRequestCard())
        self.pushButton_19.clicked.connect(lambda: self.bot.bot.requestCard())
        self.pushButton_20.clicked.connect(lambda: self.bot.bot.rewardLimit())
        self.pushButton_21.clicked.connect(lambda: self.bot.bot.runBattleGlobal())
        self.pushButton_22.clicked.connect(lambda: self.bot.bot.runBattleMode(1))
        self.pushButton_23.clicked.connect(lambda: self.bot.bot.runBattleMode(2))

    def startStopFarm(self):
        _translate = QtCore.QCoreApplication.translate
        if self.farm:
            self.farm = False
            self.pushButton.setText(_translate("MainWindow", "Старт"))
            self.thread.start()
        else:
            self.farm = True
            self.pushButton.setText(_translate("MainWindow", "Стоп"))
            self.thread.run()

    def getTrigger(self):
        x = ImageTriggers().getTriggerDEBUG(self.bot.bot.getScreen())
        s = ''
        for i in x:
            for j in i:
                s += str(j)
            s += '\n'
        self._textBrowser_3 += 'Получен тригер: ' + s + '\n'
        self.textBrowser_3.setText(self._textBrowser_3)

    def reboot(self):
        self.bot.bot.reboot()

    def logCrown(self, crown):
        self.textBrowser_2.setText(crown)

    def logEvent(self, event):
        self.textBrowser_3.setText(event)

    def logStatistic(self, stata):
        self.textBrowser.setText(stata)
