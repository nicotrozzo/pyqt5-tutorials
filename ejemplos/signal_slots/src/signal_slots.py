"""
    Este ejemplo muestra como asociar un callback a un evento
"""

# PyQt Modules
from ejemplos.signal_slots.src.ui.signal_slots import *


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("signal-slots 101")         # cambiamos el titulo de la ventana
        self.press_button.setText("Don't press me")     # texto inicial del boton
        """ACA ESTA LA MAGIA: Asociamos el evento click del boton con el metodo button_pressed"""
        self.press_button.clicked.connect(self.button_pressed)
        self.pressed = False

    def button_pressed(self):
        self.pressed = not self.pressed     # togglea el estado y muestra el texto correspondiente
        if self.pressed:
            self.press_button.setText("Press me")
        else:
            self.press_button.setText("Don't press me")
