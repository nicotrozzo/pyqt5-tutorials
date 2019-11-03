""" Ejemplos variados de otros Dialogs que pueden llegar a usarse, como el Progress, Input, Font, etc.
"""

# PyQt5 Modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QProgressDialog
from PyQt5.QtWidgets import QFontDialog

# Python Modules


if __name__ == "__main__":
    # Tipica creacion de la aplicacion que crea un contexto (eventos del sistema)
    app = QApplication([])

    # Igual de sencillo que QFileDialog y QColorDialog, simple llamada a metodo estatico
    # y se obtiene el resultado que es un QFont!
    font = QFontDialog.getFont()
    print(font)

    # Es una llamada un poco absurda, pero es el esquema general de uso como Dialog...
    # tambien se puede usar directo en la Ventana como widget!
    progress = QProgressDialog()
    progress.setValue(50)
    progress.show()

    # input = QInputDialog.getInt(widget, "Titulo del QDialog", "Mensaje del QDialog")
    # Este al igual que en el caso del QMessageBox necesita mas configuracion y se usa dentro
    # de otro Widget padre, ademas se puede configurar los rangos de validacion del Int a pedir

    # Ejecucion del loop para eventos
    app.exec()
