# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slider.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_test_form(object):
    def setupUi(self, test_form):
        test_form.setObjectName("test_form")
        test_form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(test_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.number = QtWidgets.QLCDNumber(test_form)
        self.number.setObjectName("number")
        self.verticalLayout.addWidget(self.number)
        self.slider = QtWidgets.QSlider(test_form)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.verticalLayout.addWidget(self.slider)

        self.retranslateUi(test_form)
        QtCore.QMetaObject.connectSlotsByName(test_form)

    def retranslateUi(self, test_form):
        _translate = QtCore.QCoreApplication.translate
        test_form.setWindowTitle(_translate("test_form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test_form = QtWidgets.QWidget()
    ui = Ui_test_form()
    ui.setupUi(test_form)
    test_form.show()
    sys.exit(app.exec_())

