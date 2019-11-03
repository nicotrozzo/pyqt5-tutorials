"""
    Este ejemplo muestra como leer input del usuario y que la GUI responda a ese input
"""

# PyQt Modules
from ejemplos.input_fetching.src.ui.input_fetch import *


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("InputFetching")
        self.input_line.textChanged.connect(self.update_bar)
        self.input_line.setValidator(QtGui.QIntValidator(1, 12))
        self.capacity_bar.setValue(100)
        self.msg_oculto.hide()

    def update_bar(self):
        text = self.input_line.text()
        if text:
            input = int(self.input_line.text())  # puedo castear directo porque el validator solo permite que ingresen numeros enteros
            self.capacity_bar.setValue(1/input**2*100)
            if self.capacity_bar.value() == 0:
                self.msg_oculto.show()
                self.msg_oculto.setText("Tenes la misma capacidad neuronal que yo cuando escribi esto :)")
            else:
                self.msg_oculto.hide()
        else:
            self.capacity_bar.setValue(100)
