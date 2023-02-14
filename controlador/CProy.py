# Controller for the Proyecto entity
# It will control VDatosProyecto, VDatosVuelo, and CCamara
from pathlib import Path
from typing import AnyStr, List

from modelo.Camara import Camara
from modelo.DIRECCION_VUELO import DIRECCION_VUELO
from vista.VDatosProyecto import Ui_VDatosProyecto
from controlador.CCamara import CCamara
from PyQt5 import QtWidgets as qtw


class CProy(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.Proy = None

    def openVProy(self):
        self.VProy = Ui_VDatosProyecto()
        self.VProy.setupUi(self)
        self.clicks()
        self.show()

    def clicks(self):
        # general
        self.VProy.pb_cancelar.clicked.connect(self.closeProy)

        # camaras
        self.VProy.pb_agregar_camara.clicked.connect(self.openCCamara)

    def openCCamara(self):
        self.CCamara = CCamara()
        self.CCamara.openVCamara()

    def crearProyecto(self):
        print("proyecto creado")

    def closeProy(self):
        self.close()