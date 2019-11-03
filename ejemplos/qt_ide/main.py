# PyQt5 Modules
from PyQt5.QtWidgets import QApplication


# Project Modules
from src.slider import SliderWidget


if __name__ == "__main__":
    # Creando como es tipico la aplicacion/contexto
    app = QApplication([])

    # Instanciando el Widget a probar!
    widget = SliderWidget()
    widget.show()

    # Ejecutando loop de eventos
    app.exec()
	