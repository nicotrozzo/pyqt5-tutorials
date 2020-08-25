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

    designer_qrc_files = []
    designer_ui_files = []
    custom_files = []
    good = False

    # [1] Proceso de verificacion de las carpetas correspondientes a la estructura de proyecto asumida
    if os.path.exists(os.path.join(CURRENT_PATH, DESIGNER_PATH)):
        if os.path.exists(os.path.join(CURRENT_PATH, RESOURCES_PATH)):
            if os.path.exists(os.path.join(CURRENT_PATH, DESIGNER_COMPILED_PATH)):
                if os.path.exists(os.path.join(CURRENT_PATH, RESOURCES_COMPILED_PATH)):
                    log('Estructura de proyecto reconocida correctamente.')
                    good = True
                else:
                    log('¡Error! Estructura de proyecto - No se encontro la carpeta /src/resources')
            else:
                log('¡Error! Estructura de proyecto - No se encontro la carpeta /src/ui')
        else:
            log('¡Error! Estructura de proyecto - No se encontro la carpeta /resources')
    else:
        log('¡Error! Estructura de proyecto - No se encontro la carpeta /designer')

    if good:

        # [2] Compilando cada archivo *.ui detectado en la carpeta /designer y registrandolo
        _files = os.listdir(os.path.join(CURRENT_PATH, DESIGNER_PATH))
        for _file in _files:
            _filename, _ext = os.path.splitext(_file)
            if _ext == '.ui':
                designer_ui_files.append(_filename)
                log(f'Compilando "{_filename}.ui"')
                os.system(f'pyuic5 -x {os.path.join(DESIGNER_PATH, f"{_filename}.ui")} -o {os.path.join(DESIGNER_COMPILED_PATH, f"{_filename}.py")}')
        log(f'Se compilaron {len(designer_ui_files)} archivos *.ui')

        # [3] Compilando cada archivo *.qrc detectado en la carpeta /resources y registrandolo
        _files = os.listdir(os.path.join(CURRENT_PATH, RESOURCES_PATH))
        for _file in _files:
            _filename, _ext = os.path.splitext(_file)
            if _ext == '.qrc':
                designer_qrc_files.append(_filename)
                log(f'Compilando "{resource_file}.qrc"')
                os.system(f'pyrcc5 {os.path.join(RESOURCES_PATH, f"{_filename}.qrc")} -o {os.path.join(RESOURCES_COMPILED_PATH, f"{_filename}_rc.py")}')
        log(f'Se compilaron {len(designer_qrc_files)} archivos *.qrc')

        # [4] Busco archivos Widget personalizados en /src
        _files = os.listdir(os.path.join(CURRENT_PATH, 'src'))
        for _file in _files:
            _filename, _ext = os.path.splitext(_file)
            if _ext == '.py':
                if _filename not in designer_ui_files:
                    if _filename not in ['app', 'mainwindow', '__init__']:
                        custom_files.append(_filename)

        # [5] Corrección de direcciones relativas para importar módulos desde QtDesigner
        for designer_ui_file in designer_ui_files:
            filename = os.path.join(CURRENT_PATH, DESIGNER_COMPILED_PATH, f"{designer_ui_file}.py")
            content = ""
            rewrite = False

            file = open(filename, 'r')
            for line in file:
                replaced = False

                if '\n' in line:
                    line = line[:-1]

                if 'import' in line and 'PyQt5' not in line:
                    # [5.a] Posible import de un recurso
                    for designer_qrc_file in designer_qrc_files:
                        target = f'import {designer_qrc_file}_rc'
                        if line == target:
                            content += f'from src.resources import {designer_qrc_file}_rc\n'
                            if not rewrite:
                                rewrite = True
                            replaced = True
                            break

                    # [5.b] Posible import de un widget promovido
                    for ui_file in designer_ui_files + custom_files:
                        if ui_file != designer_ui_file:
                            target = f'from {ui_file} import {ui_file}'
                            if line == target:
                                content += f'from src.{ui_file} import {ui_file}\n'
                                if not rewrite:
                                    rewrite = True
                                replaced = True
                                break
                    
                    # [5.c] Posible import no corregido
                    if not replaced:
                        if '_rc' in line:
                            log(f'\t¡Advertencia! Módulo "{line}" - Posible .qrc faltante o no detectado, pero usado en QtDesigner, y no se pudo corregir el import.')
                        else:
                            log(f'\t¡Advertencia! Módulo "{line}" - Posible archivo widget faltante en src/ui usado en QtDesigner como Promovido, no se pudo corregir el import.\n \t\tEn caso de ser módulo nativo de Python, ignorar, no soy muy inteligente aún.')
                
                if not replaced:
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