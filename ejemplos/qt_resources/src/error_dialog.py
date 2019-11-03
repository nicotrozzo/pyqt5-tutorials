from ejemplos.qt_resources.src.ui.error_dialog import *


class ErrorDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Error")
        self.message.setText("Error. No se encontraron Copas Libertadores")
        self.ok_button.clicked.connect(self.hide)   # conectamos el metodo hide(), propio de PyQt, al OK.
