# PyQt Modules
from ejemplos.qt_resources.src.main_window import *
from PyQt5 import QtWidgets

# Python Modules
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
