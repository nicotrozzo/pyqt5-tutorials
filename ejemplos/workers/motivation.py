"""
    NO USAR ESTE EJEMPLO EN TUS PROYECTOS: Este es un ejemplo de por que puede ser necesario trabajar con workers.
    Al correrlo, notar que la GUI deja de trabajar al apretar el boton porque esta ocupada en un una funcion bloqueante
    Fuente: https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0	# inicializamos contador

        layout = QVBoxLayout()	# para crear un layout desde el codigo en vez de QtDesigner

        self.l = QLabel("Start")	
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)	# callback del boton

        layout.addWidget(self.l)	# agregamos el label y el boton al layout
        layout.addWidget(b)

        w = QWidget()			# creamos un widget y le insertamos el layout que creamos
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)    # crea un timer que llama al callback en cada evento
        self.timer.start()

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)

    """ metodo bloqueante, en vez de un sleep podria ser una funcion que tarde mucho en calcular algo por ejemplo"""
    @staticmethod
    def oh_no():
        time.sleep(5)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()