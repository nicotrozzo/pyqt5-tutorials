# PyQt Modules
from ejemplos.qt_resources.src.main_window import *

# Python Modules
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
