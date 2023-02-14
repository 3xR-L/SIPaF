# Controller for the Proyecto entity
# It will control VDatosProyecto, VDatosVuelo, and CCamara
from pathlib import Path
from typing import AnyStr, List

from modelo.Camara import Camara
from modelo.DIRECCION_VUELO import DIRECCION_VUELO
from vista.VDatosProyecto import Ui_VDatosProyecto
from vista.VDatosVuelos import Ui_VDatosVuelo
from controlador.CCamara import CCamara
from PyQt5 import QtWidgets as qtw


class CProy(qtw.QWidget):
    def __init__(self, proyNames):
        super().__init__()
        self.Proy = None
        self.camarasNames = []
        self.proyectNames = proyNames

    def openVProy(self):
        self.VProy = Ui_VDatosProyecto()
        self.VProy.setupUi(self)
        self.loadCameras()
        self.clicks()
        self.show()

    def clicks(self):
        # general
        self.VProy.pb_cancelar.clicked.connect(self.closeProy)
        self.VProy.pb_siguiente.clicked.connect(self.checkVProy)
        self.VProy.pb_direccion.clicked.connect(self.selectDir)

        # camaras
        self.VProy.pb_agregar_camara.clicked.connect(self.openCCamara)

    def openCCamara(self):
        self.CCamaraV = CCamara()
        self.CCamaraV.openVCamara()
        self.loadCameras()

    def crearProyecto(self):
        print("proyecto creado")

    def closeProy(self):
        self.close()

    def loadCameras(self):
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

    def selectDir(self):
        self.VProy.le_direccion_imagenes.setText(qtw.QFileDialog.getExistingDirectory(self, 'Seleccionar carpeta'))

    def checkVProy(self):
        # check if the directory selected exists
        print("dir imagenes= ", self.VProy.le_direccion_imagenes.text())
        if not (Path(self.VProy.le_direccion_imagenes.text()).exists()) or self.VProy.le_direccion_imagenes.text() == '':
            qtw.QMessageBox.warning(self, 'Error', 'Por favor seleccione una carpeta')
        # check if the name of the project has characters doesnt starts with a blank space and has characters
        elif not self.VProy.le_nombre_proyecto.text().strip():
            qtw.QMessageBox.warning(self, 'Error', 'Por favor ingrese un nombre de proyecto')
        # check if at least one camera is selected
        elif not self.VProy.cb_camara1.currentText() and not self.VProy.cb_camara2.currentText():
            qtw.QMessageBox.warning(self, 'Error', 'Por favor seleccione al menos una cámara')
        # check if the name of the project is not already used
        elif self.VProy.le_nombre_proyecto.text() in self.proyectNames:
            qtw.QMessageBox.warning(self, 'Error', 'El nombre del proyecto ya está en uso')
        # check if the name of the project is not already used
        elif self.VProy.le_nombre_proyecto.text()+'.SIPaF' in self.proyectNames:
            qtw.QMessageBox.warning(self, 'Error', 'El nombre del proyecto ya está en uso.')
        else:
            self.openVDatosVuelos()

    def openVDatosVuelos(self):
        self.VDatosVuelos = Ui_VDatosVuelo()
        self.VDatosVuelos.setupUi(self)
        self.clicksVuelos()
        self.show()

