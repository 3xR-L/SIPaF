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
        self.camarasNames = []

    def openVProy(self):
        self.VProy = Ui_VDatosProyecto()
        self.VProy.setupUi(self)
        self.loadCameras()
        self.clicks()
        self.show()

    def clicks(self):
        # general
        self.VProy.pb_cancelar.clicked.connect(self.closeProy)

        # camaras
        self.VProy.pb_agregar_camara.clicked.connect(self.openCCamara)
        self.VProy.cb_camara1

    def openCCamara(self):
        self.CCamaraV = CCamara()
        self.CCamaraV.openVCamara()
        self.loadCameras()

    def crearProyecto(self):
        print("proyecto creado")

    def closeProy(self):
        self.close()

    def loadCameras(self):
        print("load camaras")
        self.CCamara = CCamara()
        camarasNames = self.CCamara.camaras
        tipos = self.CCamara.tipos
        self.VProy.cb_camara1.clear()
        self.VProy.cb_camara2.clear()
        # make available each value on the combo box
        for each in zip(camarasNames, tipos):
            if each[1] == 'RGB':
                self.VProy.cb_camara1.addItem(each[0])
            else:
                self.VProy.cb_camara2.addItem(each[0])