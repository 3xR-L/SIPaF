from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileSystemModel
from controlador.CGestionarEDT import CGestionarEDT
from controlador.CProy import CProy
from modelo.EspacioDeTrabajo import EspacioDeTrabajo
from vista.VEDT import Ui_VEDT

from PyQt5 import QtWidgets as qtw


class CEDT(qtw.QMainWindow):
    def __init__(self):
        self.CGEDT = CGestionarEDT()
        self.CProy = None
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
        # Open VGestionarEDT when the action cambiar on the menu EDT if nuevo, guardar, eliminar or cambiar is clicked
        # on the EDT menu
        self.VEDT.EDT_nuevo.triggered.connect(self.openVCGestionarEDT)
        self.VEDT.EDT_cambiar.triggered.connect(self.openVCGestionarEDT)
        self.VEDT.EDT_eliminar.triggered.connect(self.openVCGestionarEDT)

        # Gestionar proyectos
        self.VEDT.proyecto_nuevo.triggered.connect(self.openVCProy)
        self.VEDT.pb_crear_proyecto.clicked.connect(self.openVCProy)

    def loadProjects(self):
        # set the model for the tree view
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        self.VEDT.vista_arbol_proyectos.setModel(self.model)
        self.VEDT.vista_arbol_proyectos.setRootIndex(
            self.model.index(self.CGEDT.mEDT.direccion + '/' + self.CGEDT.mEDT.nombreEDT))
        self.VEDT.vista_arbol_proyectos.setSortingEnabled(True)
        self.VEDT.vista_arbol_proyectos.setColumnWidth(0, 120)
        self.VEDT.vista_arbol_proyectos.setColumnWidth(1, 80)
        self.VEDT.vista_arbol_proyectos.setColumnWidth(2, 80)

    def openVCGestionarEDT(self):
        last_model = self.CGEDT.mEDT
        self.CGEDT.openVGEDT()
        # check if the model has been changed
        if last_model is not self.CGEDT.mEDT:
            self.loadProjects()

    def openVCProy(self):
        if self.CProy is None:
            self.CProy = CProy()
        self.CProy.openVProy()
