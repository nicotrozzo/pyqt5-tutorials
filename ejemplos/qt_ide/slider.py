""" Esta es una aplicacion simple que al mover un Slider actualiza el contenido
    de una display numerico en la pantalla. Simple conexion de dos eventos, pero tambien
    a traves del QtDesigner se puede hacer directo.
"""

# PyQt5 Modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot

# Python Modules

# Example Modules
from ui.slider import Ui_test_form


class SliderWidget(QWidget, Ui_test_form):
    """ SliderWidget ejemplo, siempre tenemos que heredar el padre original de lo que estamos implementando,
    y ademas la compilacion del QtDesigner. """

    # Creamos el constructor de la clase y luego con super() llamamos
    # al constructor del padre, con herencia multiple python lo maneja solo
    def __init__(self):
        super(SliderWidget, self).__init__()

        # Hacemos un build de la Widget
        self.setupUi(self)

        # Conexion signal (evento) con slot (callback)
        self.slider.valueChanged.connect(self.update_number)

    @pyqtSlot(int)
    def update_number(self, value: int):
        self.number.display(value)


if __name__ == "__main__":
    # Creando como es tipico la aplicacion/contexto
    app = QApplication([])

    # Instanciando el Widget a probar!
    widget = SliderWidget()
    widget.show()

    # Ejecutando loop de eventos
    app.exec()
