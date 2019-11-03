# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/input_fetch.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(178, 215)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.capacity_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.capacity_bar.setGeometry(QtCore.QRect(40, 80, 111, 23))
        self.capacity_bar.setProperty("value", 24)
        self.capacity_bar.setObjectName("capacity_bar")
        self.msg_cap = QtWidgets.QLabel(self.centralwidget)
        self.msg_cap.setGeometry(QtCore.QRect(20, 60, 141, 16))
        self.msg_cap.setObjectName("msg_cap")
        self.msg_horas = QtWidgets.QLabel(self.centralwidget)
        self.msg_horas.setGeometry(QtCore.QRect(20, 10, 141, 16))
        self.msg_horas.setObjectName("msg_horas")
        self.input_line = QtWidgets.QLineEdit(self.centralwidget)
        self.input_line.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.input_line.setText("")
        self.input_line.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_line.setClearButtonEnabled(False)
        self.input_line.setObjectName("input_line")
        self.msg_oculto = QtWidgets.QTextBrowser(self.centralwidget)
        self.msg_oculto.setGeometry(QtCore.QRect(10, 110, 161, 61))
        self.msg_oculto.setObjectName("msg_oculto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 178, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.msg_cap.setText(_translate("MainWindow", "Capacidad neuronal restante"))
        self.msg_horas.setText(_translate("MainWindow", "Cuantas horas cursaste hoy?"))


from ejemplos.input_fetching.src.input_fetch import *


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
