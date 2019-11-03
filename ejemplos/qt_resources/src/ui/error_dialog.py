# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/error_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 119)
        Dialog.setStyleSheet("")
        self.message = QtWidgets.QLabel(Dialog)
        self.message.setGeometry(QtCore.QRect(170, 40, 221, 31))
        self.message.setText("")
        self.message.setObjectName("message")
        self.img_lbl = QtWidgets.QLabel(Dialog)
        self.img_lbl.setGeometry(QtCore.QRect(20, 20, 131, 91))
        self.img_lbl.setStyleSheet("border-image:url(:/err_prefix/error_icon.jpg)")
        self.img_lbl.setText("")
        self.img_lbl.setObjectName("img_lbl")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setGeometry(QtCore.QRect(270, 90, 75, 23))
        self.ok_button.setObjectName("ok_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok_button.setText(_translate("Dialog", "OK"))


from ejemplos.qt_resources.src.error_res import *


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
