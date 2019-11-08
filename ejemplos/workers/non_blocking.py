"""
    Este ejemplo muestra como solucionar el problema en 'motivation.py' utilizando Workers y ThreadPools
    Fuente: https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time


class Worker(QRunnable):

    @pyqtSlot()
    def run(self):
        print("Blocking start")
        time.sleep(5)
        print("Blocking complete")


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.threadpool = QThreadPool()
        print("Multiworking with maximum %d workers" % self.threadpool.maxThreadCount())

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)    # crea un timer que se llama al callback en cada evento
        self.timer.start()

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)

    """ metodo bloqueante, en vez de un sleep podria ser una funcion que tarde mucho en calcular algo por ejemplo"""
    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)   # le mandamos el trabajo al worker, que lo ejecutara de forma concurrente


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()





