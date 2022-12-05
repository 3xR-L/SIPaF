from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileSystemModel
from controlador.CGestionarEDT import CGestionarEDT
from modelo.EspacioDeTrabajo import EspacioDeTrabajo
from vista.VEDT import Ui_VEDT

from PyQt5 import QtWidgets as qtw
import sys

class CEDT(qtw.QMainWindow):
    def __init__(self, start = False):
        super().__init__()
        self.CGEDT = CGestionarEDT(start=True)
        self.ui = Ui_VEDT()
        self.ui.setupUi(self)
        self.loadProjects()
        self.clicks()

    def loadProjects(self):
        print(self.CGEDT.mEDT.direccion)
        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())
        self.ui.vista_arbol_proyectos.setModel(model)
        self.ui.vista_arbol_proyectos.setRootIndex(model.index(self.CGEDT.mEDT.direccion+'/'+self.CGEDT.mEDT.nombreEDT))

    def clicks(self):
        # Open VGestionarEDT when the action cambiar on the menu EDT if nuevo, guardar, eliminar or cambiar is clicked
        # on the EDT menu
        self.ui.EDT_nuevo.triggered.connect(self.openVCGestionarEDT)
        self.ui.EDT_cambiar.triggered.connect(self.openVCGestionarEDT)
        self.ui.EDT_eliminar.triggered.connect(self.openVCGestionarEDT)

        #self.ui.menubar.triggered.connect(self.openVCGestionarEDT)

        # Open VDatos Princiaples del proyecto
    def openVCGestionarEDT(self):
        self.CGEDT.openVGestionarEDT()
        print('openVGestionarEDT')