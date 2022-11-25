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
        self.ui.vistaArbolProyectos.setModel(model)
        self.ui.vistaArbolProyectos.setRootIndex(model.index(self.CGEDT.mEDT.direccion+'/'+self.CGEDT.mEDT.nombreEDT))

    def clicks(self):
        # Open VGestionarEDT when the action cambiaar on the menu EDT
        self.ui.menubar.triggered.connect(self.openVCGestionarEDT)

    def openVCGestionarEDT(self):
        self.CGEDT.openVGestionarEDT()
        print('openVGestionarEDT')