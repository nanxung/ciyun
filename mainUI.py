# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from Ui_mainUI import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QListWidgetItem
from cy import ciyun

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.file_dialog=QtWidgets.QFileDialog()
        self.center()

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
    
    @pyqtSlot()
    def on_open_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            self.my_file_path = self.file_dialog.getOpenFileName(parent=self, caption=u'打开文件', directory='/')
            self.tuPicture.setPixmap(QPixmap(self.my_file_path[0]))
            print(self.my_file_path[0])
        except Exception:
            print('open_error')
        print('open')
    
    @pyqtSlot()
    def on_save_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            my_file = QtWidgets.QFileDialog.getSaveFileName(parent=self, caption=u'保存为')
            print(my_file)



        except Exception:
            print('save_error')
        print('save')
    
    @pyqtSlot()
    def on_ciyun_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        ciyun(self.my_file_path[0])
        self.cyPicture.setPixmap(QPixmap('cy.png'))
        print('ciyun')
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()

    ui.show()
    sys.exit(app.exec_())
