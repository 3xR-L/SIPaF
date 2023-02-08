from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileSystemModel
from controlador.CGestionarEDT import CGestionarEDT
from controlador.CProy import CProy
from modelo.EspacioDeTrabajo import EspacioDeTrabajo
from vista.VEDT import Ui_VEDT

from PyQt5 import QtWidgets as qtw
import sys

class CEDT(qtw.QMainWindow):
    def __init__(self):
        self.CGEDT = CGestionarEDT()
        if self.CGEDT.mEDT is None:
            pass
        else:
            super().__init__()
            self.VEDT = Ui_VEDT()
            self.VEDT.setupUi(self)
            self.loadProjects()
            self.clicks()
            self.show()


    def clicks(self):
        pass

    def loadProjects(self):
        # set the model for the tree view
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        self.VEDT.vista_arbol_proyectos.setModel(self.model)
        self.VEDT.vista_arbol_proyectos.setRootIndex(self.model.index(self.CGEDT.mEDT.direccion))
        self.VEDT.vista_arbol_proyectos.setSortingEnabled(True)
        self.VEDT.vista_arbol_proyectos.setColumnWidth(0, 120)
        self.VEDT.vista_arbol_proyectos.setColumnWidth(1, 80)
        self.VEDT.vista_arbol_proyectos.setColumnWidth(2, 80)