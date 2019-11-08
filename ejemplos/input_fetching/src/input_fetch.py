"""
    Este ejemplo muestra como leer input del usuario y como hacer para que la GUI responda a dicho input
"""

# PyQt Modules
from src.ui.input_fetch import *


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)	# como siempre, inicializamos todo
		
        self.setWindowTitle("InputFetching")	# titulo de la ventana
        self.input_line.textChanged.connect(self.update_bar)	# CADA VEZ que cambie el texto se llamara al callback
        """ El QIntValidator no deja que ingresen nada mas que numeros enteros.
            Mas info sobre validators: 
            https://doc.qt.io/qtforpython/PySide2/QtGui/QRegExpValidator.html#qregexpvalidator """
        self.input_line.setValidator(QtGui.QIntValidator(1, 12, self))
        self.capacity_bar.setValue(100)	# valor inicial de la barra de capacidad
        self.msg_oculto.hide()	# oculto lo que voy a mostrar mas adelante

    def update_bar(self):
        text = self.input_line.text()	# levanto entrada que acaban de ingresar
        if text:	# si hay algo escrito
            """ Puedo castear directo a int porque el validator solo permite que ingresen numeros enteros """
            input = int(self.input_line.text())	
            if input:	# si el valor ingresado es 0 no hago nada
                self.capacity_bar.setValue(1/input**2*100)	# cambia la barra de capacidad en funcion de la entrada
                if self.capacity_bar.value() == 0:	# si llego a cero, muestro el mensaje oculto
                    self.msg_oculto.setText("Tenes la misma capacidad neuronal que yo cuando escribi esto :)")
					self.msg_oculto.show()
                else:
                    self.msg_oculto.hide()
        else:	# si no ingresaron nada seteo 100%
            self.capacity_bar.setValue(100)
