""""
    Este ejemplo muestra como trabajan de forma concurrente los workers
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time
import traceback, sys


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        no data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `str` string returned from processing

    progress
        `int` indicating % progress and # of work

    '''
    finished = pyqtSignal(int)
    error = pyqtSignal(tuple)
    result = pyqtSignal(str, int)
    progress = pyqtSignal(int, int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, n, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.n = n  # indica numero de worker

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

        self.kwargs['pos'] = self.n  # agrego la posicion como argumento para el callback

    @pyqtSlot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)	# llama a la funcion de progreso
        except:	# si hubo error
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result, self.n)  # devuelve resultado del procesamiento, ademas pasa numero de worker
        finally:
            self.signals.finished.emit(self.n)  # con self.n avisa qué worker terminó


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        self.layout = QVBoxLayout()

        self.free_wrk = [True, True, True, True]	# indica si cada worker esta libre o no

        self.wrk_labs = [QLabel(""), QLabel(""), QLabel(""), QLabel("")]	# creo labels de cada worker

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)


        self.layout.addWidget(self.l)
        self.layout.addWidget(b)

        for lab in self.wrk_labs:
            self.layout.addWidget(lab)

        w = QWidget()
        w.setLayout(self.layout)

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def progress_fn(self, n, pos):
        self.wrk_labs[pos].setText(f"Worker {pos + 1}: job {n}% done")

    def execute_this_fn(self, progress_callback, pos):
        for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(n * 100 / 4, pos)

        return "done."

    def print_output(self, s, n):
        self.wrk_labs[n].setText(f"Worker {n + 1}" + s)

    def thread_complete(self, n):
        self.wrk_labs[n].setText(f"Worker {n + 1} free")
        self.free_wrk[n] = True

    def oh_no(self):
        n = -1
        for i in range(len(self.free_wrk)):
            if self.free_wrk[i]:  # si esta libre
                n = i
                self.free_wrk[i] = False
                break
        if n < 0:
            n = 0  # si estan todos ocupados le asigno el primero, que sera el proximo en liberarse
        # Pass the function to execute
        worker = Worker(self.execute_this_fn, n)  # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()