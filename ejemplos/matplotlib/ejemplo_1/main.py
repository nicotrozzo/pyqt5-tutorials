""" Ejemplo_1: Retomamos el Ejemplo_0! Agregamos un poco de estilo al diseño
    de nuestro plotter!!!
"""

# PyQt5 Modules
from PyQt5.QtWidgets import QApplication

# Project Modules
from src.matplotlib import MatplotlibWidget

# Python Modules


if __name__ == "__main__":
    # Creamos como es usual la aplicacion, el contexto de eventos
    app = QApplication([])

    # Creamos la instancia del widget y la mostramos
    widget = MatplotlibWidget()
    widget.show()

    # Ejecutamos el loop de eventos
    app.exec()
