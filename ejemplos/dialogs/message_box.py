""" Ejemplo de uso de QMessageBox, un dialogo ya existente para mostrar mensajes de error, o preguntas Si/No.
"""

# PyQt Modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

# Python Modules

if __name__ == "__main__":
    # Tipica creacion de la aplicacion que crea un contexto (eventos del sistema)
    app = QApplication([])

    # Creamos instancia del QMessageBox editada por nosotros a nuestro antojo!
    widget = QMessageBox(
        QMessageBox.Warning,                    # Podemos agregar un icono al dialogo
        "Informacion",                          # El titulo del dialogo emergente
        "Este es un ejemplo de QMessageBox",    # Mensaje del QMessageBox
        QMessageBox.Yes | QMessageBox.No        # Podemos elegir que botones poner, indica mas de uno con |
    )
    widget.show()

    # Estas en apuro y queres crear un pop-up con mensajes rapido!
    # QMessageBox.information(widget, "Informacion", "Esto muestra un mensaje rapidamente con informacion!")
    # QMessageBox.warning(widget, "Precaucion", "Ojo, puede que la estes cagando...")
    # QMessageBox.critical(widget, "Critico", "Estoy a punto de trular")
    #
    # IMPORTANTE! esto esta comentado porque asi como esta no funcionaria, puede usarse asi directo,
    # pero es necesario que en "widget" le pases un Parent, digamos que creas tu propia QMainWindow o un QWidget,
    # y no este main escueto, entonces ahi pondrias "self".

    # Ejecucion del loop para eventos
    app.exec()
