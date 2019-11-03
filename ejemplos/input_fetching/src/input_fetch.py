"""
    Este ejemplo muestra como leer input del usuario y que la GUI responda a ese input
"""

# PyQt Modules
from src.ui.input_fetch import *


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("InputFetching")
        self.input_line.textChanged.connect(self.update_bar)
        """ El QIntValidator no deja que ingresen nada mas que numeros enteros.
            Mas info sobre validators: 
            https://doc.qt.io/qtforpython/PySide2/QtGui/QRegExpValidator.html#qregexpvalidator """
        self.input_line.setValidator(QtGui.QIntValidator(1, 12, self))
        self.capacity_bar.setValue(100)
        self.msg_oculto.hide()

    def update_bar(self):
        text = self.input_line.text()
        if text:
            """ Puedo castear directo porque el validator solo permite que ingresen numeros enteros """
            input = int(self.input_line.text())
            if input:
                self.capacity_bar.setValue(1/input**2*100)
                if self.capacity_bar.value() == 0:
                    self.msg_oculto.show()
                    self.msg_oculto.setText("Tenes la misma capacidad neuronal que yo cuando escribi esto :)")
                else:
                    self.msg_oculto.hide()
        else:
            self.capacity_bar.setValue(100)
