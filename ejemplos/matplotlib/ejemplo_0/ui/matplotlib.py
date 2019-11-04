# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matplotlib.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 344)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotter_container = QtWidgets.QStackedWidget(Form)
        self.plotter_container.setObjectName("plotter_container")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.plotter_container.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.plotter_container.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.plotter_container)
        self.update_button = QtWidgets.QPushButton(Form)
        self.update_button.setObjectName("update_button")
        self.verticalLayout.addWidget(self.update_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.update_button.setText(_translate("Form", "Actualizar!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

