""" Ejemplo_0: Que importar, y como crear nuestro Widget para que se cargue
    con el FigureCanvas, y dibujar algo sencillo. Como limpiar el canvas,
    cargarle cosas nuevas y refrescarlo!
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
