import sys
import os

__REQUIREMENTS__ = """PyQt5"""

__MAINWINDOW__UI__ = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget"/>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

"""

__MAINWINDOW__ = """# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
"""

__MAIN__ = """# Project modules
from src.app import main

if __name__ == "__main__":
    main()
"""

__APP__ = """# PyQt5 modules
from PyQt5 import QtWidgets

# Python modules
import sys

# Main window ui import
from src.mainwindow import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
"""

def log(msg: str):
    """ Imprime un mensaje en consola.
        @param msg: Mensaje
    """
    print(f'[PyQt helper] {msg}')

def create_structure(tree):
    """ Crea la estructura de directorio del proyecto, recursivamente
        @param tree: El arbol de la estructura
    """
    # Buscando directorio actual
    curr_dir = os.getcwd()

    for key in tree.keys():
        if '.' in key:
            # Es un archivo
            log(f'Creando archivo {key}...')
            file = open(key, 'w')
            if tree[key] is not None:
                file.write(tree[key])
            file.close()
        else:
            # Es una carpeta
            log(f'Creando carpeta {key}...')
            os.mkdir(key)

            # Si tiene contenido, recursivamente sigo...
            if tree[key] is not None:
                os.chdir(curr_dir + f'/{key}')
                create_structure(tree[key])
                os.chdir(curr_dir)

def create_app(args):
    """ Ejecuta el comando de creación de una aplicación en el directorio actual.
        @param args: Parámetros de consola
    """
    # Buscando el nombre de la aplicación
    log(f'Comenzando creación de aplicación')

    # Creando el arbol de la estructura del proyecto
    app_structure = {
        'assets': None,
        'designer': {
            'mainwindow.ui': __MAINWINDOW__UI__
        },
        'resources': None,
        'tests': None,
        'src': {
            '__init__.py': None,
            'app.py': __APP__,
            'mainwindow.py': __MAINWINDOW__,
            'package': None,
            'ui': None,
            'resources': None
        },
        'main.py': __MAIN__,
        'requirements.txt': __REQUIREMENTS__
    }
    create_structure(app_structure)

    log('Proyecto creado!')
    log('Corriendo compilacion inicial...')
    compile(args)
    log('Ya podes ejecutar tu aplicación con Python, con main.py')

def compile(args):
    """ Busca los archivos .ui y .qrc y los compila y mueve automaticamente.
        @param args: Parámetros de consola
    """
    CURRENT_PATH = os.getcwd()
    DESIGNER_PATH = "designer"
    RESOURCES_PATH = "resources"
    DESIGNER_COMPILED_PATH = os.path.join("src", "ui")
    RESOURCES_COMPILED_PATH = os.path.join("src", "resources")

    # Verifico existencia del directorio designer
    if os.path.exists(os.path.join(CURRENT_PATH, DESIGNER_PATH)):
        # Compilando cada archivo .ui
        designer_files = os.listdir(os.path.join(CURRENT_PATH, DESIGNER_PATH))
        log(f'Se encontraron {len(designer_files)} archivos .ui en /designer')
        for designer_file in designer_files:
            log(f'Compilando "{designer_file}"...')
            os.system(f'pyuic5 -x {os.path.join(DESIGNER_PATH, designer_file)} -o {os.path.join(DESIGNER_COMPILED_PATH, f"{designer_file[:-3]}.py")}')
    else:
        log('No se pudo encontrar la carpeta /designer')
    
    # Verifico existencia del directorio resources
    if os.path.exists(os.path.join(CURRENT_PATH, RESOURCES_PATH)):
        # Compiling the .qrc files, getting their names and running the command ony by one
        resources_files = os.listdir(os.path.join(CURRENT_PATH, RESOURCES_PATH))
        compiled_resources = []
        log(f'Se encontraron {len(resources_files)} archivos .qrc en /resources')
        for resource_file in resources_files:
            log(f'Compilando "{resource_file}"...')
            compiled_resource = os.path.join(RESOURCES_COMPILED_PATH, f"{resource_file[:-4]}_rc.py")
            compiled_resources.append(f"{resource_file[:-4]}_rc.py")
            os.system(f'pyrcc5 {os.path.join(RESOURCES_PATH, resource_file)} -o {compiled_resource}')
    else:
        log('No se pudo encontrar la carpeta /resources')
    
    # Corrigiendo el problema del import del modulo de recursos desde un archivo designer
    # con un path incorrecto, generado automaticamente por QtDesigner
    log('Corrigiendo import de recursos en archivos compilados...')
    for designer_file in designer_files:
        filename = os.path.join(CURRENT_PATH, DESIGNER_COMPILED_PATH, f"{designer_file[:-3]}.py")
        content = ""
        rewrite = False

        file = open(filename, 'r')
        for line in file:
            if '\n' in line:
                line = line[:-1]

            for resource in compiled_resources:
                if line == f'import {resource[:-3]}':
                    content += f'from src.resources import {resource[:-3]}\n'
                    rewrite = True
                    break
            else:
                content += f'{line}\n'
        file.close()

        if rewrite:
            file = open(filename, 'w')
            file.write(content)
            file.close()
    
    # Termine!
    log('Compilación finalizada con éxito!')

def help(args):
    """ Muestra en consola un texto de ayuda.
    """
    msg = """ Comandos disponibles:

        + app: Crear un proyecto con su estructura de directorio.
            kt.py app

        + compile: Compilar .ui y .qrc dentro del proyecto estructurado.
            kt.py compile

        + build: Crea .exe distribuible con sus correspondientes .dll
            kt.py build
        
        + help: Menu de ayuda
            kt.py help
    """
    log(msg)

def build(arg):
    """ Crea una version distribuible .exe con sus librerias dinamicas.
    """
    os.system('pyinstaller main.py --noconfirm --noconsole --clean')

def main(args):
    # Filtrando directorio no deseado
    args = args[1:]

    # Verificando comandos en el PATH
    if len(args) > 0:
        # Parseando el comando y creando el dispatcher
        command = args[0]
        dispatcher = {
            'app': create_app,
            'compile': compile,
            'help': help,
            'build': build
        }
        
        # Dispatching requests...
        if command in dispatcher.keys():
            dispatcher[command](args)
        else:
            log('Comando no encontrado.')
            help(args)
    else:
        log('Se necesita un comando para ejecutar.')

if __name__ == '__main__':
    main(sys.argv)