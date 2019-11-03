"""
    Este ejemplo muestra como abrir una ventana de dialogo desde una ventana y como leer una checkBox
"""

# PyQt Modules
from ejemplos.qt_resources.src.ui.main_window import *
from ejemplos.qt_resources.src.error_dialog import ErrorDialog


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("")
        self.racing_check.setText("Soy hincha de Racing")
        self.dialog = ErrorDialog()     # instanciamos el cuadro de dialogo a abrir
        self.racing_check.pressed.connect(self.open_dialog)

    def open_dialog(self):
        if not self.racing_check.isChecked():
            self.dialog.show()
        else:
            self.dialog.hide()
