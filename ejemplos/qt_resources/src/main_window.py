"""
    Este ejemplo muestra como abrir una ventana de dialogo desde una ventana y como leer una checkBox
"""

# PyQt Modules
from src.ui.main_window import *
from src.resources.error_res import *
from PyQt5.QtWidgets import QMessageBox


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Example")
        self.racing_check.setText("Soy hincha de Racing")
        self.racing_check.pressed.connect(self.open_dialog)  # seteamos el calback para cada vez que apreten la checkBox
        self.dialog = QtWidgets.QMessageBox(QMessageBox.Warning, "Hincha de Racing!?",
                                             "Error. No se encontraron Copas Libertadores", QMessageBox.Ok)  # ver ejemplo "dialogs"
        self.resize(214, 74)    # tamaño hardcodeado que me fije en QtDesigner
        self.img.hide()

    def open_dialog(self):
        if not self.racing_check.isChecked():
            self.dialog.show()      # muestro la ventana de error
            self.resize(214, 301)
            self.racing_check.setChecked(True)
            self.img.show()
            self.dialog.exec_()     # funcion bloqueante: espera que apreten Ok
            self.resize(214, 74)
            self.img.hide()
            self.racing_check.setChecked(False)

