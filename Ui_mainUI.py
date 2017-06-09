# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cb/ericProject/wordYun/mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 831)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.open = QtWidgets.QPushButton(self.centralWidget)
        self.open.setGeometry(QtCore.QRect(210, 10, 85, 33))
        self.open.setObjectName("open")
        self.tuPicture = QtWidgets.QLabel(self.centralWidget)
        self.tuPicture.setGeometry(QtCore.QRect(9, 48, 491, 401))
        self.tuPicture.setStyleSheet("background-color: rgb(199, 237, 204);")
        self.tuPicture.setText("")
        self.tuPicture.setObjectName("tuPicture")
        self.cyPicture = QtWidgets.QLabel(self.centralWidget)
        self.cyPicture.setGeometry(QtCore.QRect(512, 48, 491, 401))
        self.cyPicture.setStyleSheet("background-color: rgb(199, 237, 204);")
        self.cyPicture.setText("")
        self.cyPicture.setObjectName("cyPicture")
        self.save = QtWidgets.QPushButton(self.centralWidget)
        self.save.setGeometry(QtCore.QRect(910, 10, 85, 33))
        self.save.setObjectName("save")
        self.ciyun = QtWidgets.QPushButton(self.centralWidget)
        self.ciyun.setGeometry(QtCore.QRect(640, 10, 99, 27))
        self.ciyun.setObjectName("ciyun")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open.setText(_translate("MainWindow", "打开"))
        self.save.setText(_translate("MainWindow", "保存"))
        self.ciyun.setText(_translate("MainWindow", "词云图"))



