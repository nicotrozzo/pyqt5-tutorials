# PyQt Modules
from src.main_window import *
from PyQt5 import QtWidgets

# Python Modules
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
