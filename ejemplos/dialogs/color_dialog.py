""" Ejemplo de uso de QColorDialog.
"""

# PyQt5 Modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QColorDialog

# Python Modules


if __name__ == "__main__":
    # Tipica creacion de la aplicacion que crea un contexto (eventos del sistema)
    app = QApplication([])

    # Podemos usar la forma de ejecucion a traves de sus metodos estaticos
    # es importante que lo que devuelve es un QColor... pero se puede leer
    # sus atributos directamente sin problemas
    color = QColorDialog.getColor()
    print("Elegiste el color: {}".format(color.getRgb()))

    # Ejecucion del loop para eventos
    app.exec()
