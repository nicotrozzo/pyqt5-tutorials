"""
    Este ejemplo muestra como abrir una ventana de dialogo desde una ventana y como leer una checkBox
"""

# PyQt Modules
from ejemplos.qt_resources.src.ui.main_window import *
from PyQt5.QtWidgets import QMessageBox

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("")
        self.racing_check.setText("Soy hincha de Racing")
        self.racing_check.pressed.connect(self.open_dialog)
        self.dialog2 = QtWidgets.QMessageBox(QMessageBox.Warning, "Hincha de Racing!?",
                                             "Error. No se encontraron Copas Libertadores", QMessageBox.Ok)
        self.img.hide()


    def open_dialog(self):
        if not self.racing_check.isChecked():
            self.dialog2.show()
            self.resize(214, 301)
            self.racing_check.setChecked(True)
            self.img.show()
        else:
            self.dialog2.hide()
            self.resize(214, 74)
            self.racing_check.setChecked(False)
            self.img.hide()
