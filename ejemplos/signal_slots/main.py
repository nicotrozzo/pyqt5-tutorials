# Python Modules
import sys

# PyQt Modules
from ejemplos.signal_slots.src.signal_slots import *

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
