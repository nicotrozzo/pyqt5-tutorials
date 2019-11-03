""" Ejemplo de uso de QFileDialog.
"""

# PyQt5 Modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog

# Python Modules


if __name__ == "__main__":
    # Tipica creacion de la aplicacion que crea un contexto (eventos del sistema)
    app = QApplication([])

    # Podemos usar la forma de ejecucion a traves de sus metodos estaticos
    # IMPORTANTE! Revisar la configuracion del constructor para saber bien que devuelve,
    # asi como donde empieza la ventana de busqueda de archivos o carpetas, tambien
    # puede filtrar por extensiones!!!
    file_output = QFileDialog.getOpenFileName()
    print(file_output)

    # Filtrando por extensiones de archivos
    file_output = QFileDialog.getOpenFileName(filter="*.py")
    print(file_output)

    # Empezando en alguna direccion especifica, aca te va a mandar a la carpeta atras!
    file_output = QFileDialog.getOpenFileName(directory="..", filter="*.py")
    print(file_output)

    # Ejecucion del loop para eventos
    app.exec()
