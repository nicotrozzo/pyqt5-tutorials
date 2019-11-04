""" Creacion de una ventana integrando el backend de Matplotlib!
"""

# PyQt5 Modules
from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import pyqtSlot

# Matplotlib Modules
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Project Modules
from ui.matplotlib import Ui_Form

# Python Modules
from numpy import *
from time import *
from random import *


class MatplotlibWidget(QWidget, Ui_Form):
    """ Creamos nuestra clase MatplotlibWidget, heredo de QWidget porque asi lo defino en QtDesigner,
        y luego heredo la forma compilada que tenemos en la carpeta /ui
    """

    def __init__(self):
        super(MatplotlibWidget, self).__init__()        # Llamamos al constructor de los padres
        self.setupUi(self)                              # Necesitamos usar esto para hacer el build de los componentes
        seed(time())                                    # Random seed para generacion aleatoria

        # Tenemos que utilizar el backend que provee Matplotlib para PyQt y crear un FigureCanvas,
        # son las entidades encargadas de proveer el soporte grafico necesario para dibujar en pantalla
        # y basicamente hacen la magica.
        #
        # Asi como FigureCanvas es el control del entorno grafico donde dibujamos, Figure
        # corresponde al espacio utilizado para dibujar y despues sobre el se agregan pares de ejes.
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # A partir de aca es lo mismo que con pyplot, solo que el manejo no es automatico, sino
        # que lo hace uno con criterio, entonces creamos un par de ejes
        self.axes = self.figure.add_subplot()

        canvas_index = self.plotter_container.addWidget(self.canvas)
        self.plotter_container.setCurrentIndex(canvas_index)

        # Algo mas emocionante, cambiemos el contenido con un callback al boton de pantalla!
        self.update_button.clicked.connect(self.on_plot_update)

    @pyqtSlot()
    def on_plot_update(self):
        """ Slot/Callback usado para actualizar datos en el Axes """

        # Creamos un puntos para el eje x y para el eje y!
        x_axis = linspace(0, 2 * pi, num=1000)
        y_axis = sin(x_axis * randint(1, 5))

        # Limpiamos el axes, agregamos los puntos, y actualizamos el canvas
        # IMPORTANTE! Te invito a comentar para que veas la importancia del .clear() y .draw()
        self.axes.clear()
        self.axes.plot(x_axis, y_axis, label="Señal")   # Nuevo, podemos agregarle un label y activar con .legend()

        # Configuramos los ejes para que tengan un label
        self.axes.set_xlabel("Time [s]")
        self.axes.set_ylabel("Voltage [V]")

        self.axes_configuration()

        self.figure.legend()
        self.canvas.draw()

    def axes_configuration(self):
        """ Agrego una configuracion al axes, no hace falta un metodo nuevo, simplemente separacion
            para mayor claridad del ejemplo! """

        # Podemos agregar una grilla
        self.axes.minorticks_on()                           # Necesitamos esto para usar los ticks menores!
        self.axes.grid(b=True, which="both", axis="both")   # Podes elegir que eje y si es para ticks mayores/menores
