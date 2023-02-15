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
    def __init__(self, proyNames, dirEDT):
        super().__init__()
        self.dirEDT = dirEDT
        self.Proy = None
        self.camarasNames = []
        self.proyectNames = proyNames
        self.nombreProyecto = None
        self.anchoCubierto = None
        self.largoCubierto = None
        self.overlapVertical = None
        self.overlapHorizontal = None
        self.alturaVuelo = None
        self.orientacion = None
        self.fechaVuelo = None
        self.Camaras = None
        self.direccionImagenes = None
        self.checkpoint = None

        self.CVDatosVuelo = None

    def openVProy(self):
        self.VProy = Ui_VDatosProyecto()
        self.VProy.setupUi(self)
        self.loadCameras()
        self.clicksDatos()
        self.show()

    def clicksDatos(self):
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

    def createProy(self):
        # create the project folder, subfolders and file
        Path(self.dirEDT + '/' + self.nombreProyecto).mkdir(parents=True, exist_ok=True)
        Path(self.dirEDT + '/' + self.nombreProyecto + '/Imagenes').mkdir(parents=True, exist_ok=True)
        Path(self.dirEDT + '/' + self.nombreProyecto + '/Imagenes/RGB').mkdir(parents=True, exist_ok=True)
        Path(self.dirEDT + '/' + self.nombreProyecto + '/Imagenes/IR').mkdir(parents=True, exist_ok=True)
        Path(self.dirEDT + '/' + self.nombreProyecto + '/Imagenes/RGB/originales').mkdir(parents=True, exist_ok=True)
        Path(self.dirEDT + '/' + self.nombreProyecto + '/Imagenes/RGB/segmentadas').mkdir(parents=True, exist_ok=True)
        Path(self.dirEDT + '/' + self.nombreProyecto + '/Imagenes/IR/originales').mkdir(parents=True, exist_ok=True)
        Path(self.dirEDT + '/' + self.nombreProyecto + '/Imagenes/IR/segmentadas').mkdir(parents=True, exist_ok=True)
        Path(self.dirEDT + '/' + self.nombreProyecto + '/Reporte').mkdir(parents=True, exist_ok=True)

        # create the project file
        with open(self.dirEDT + '/' + self.nombreProyecto + '/' + self.nombreProyecto + '.SIPaF', 'w') as file:
            file.write('<Proyecto>\n')
            file.write('\t<Nombre>' + self.nombreProyecto + '</Nombre>\n')
            file.write('\t<AnchoCubierto>' + str(self.anchoCubierto) + '</AnchoCubierto>\n')
            file.write('\t<LargoCubierto>' + str(self.largoCubierto) + '</LargoCubierto>\n')
            file.write('\t<OverlapHorizontal>' + str(self.overlapHorizontal) + '</OverlapHorizontal>\n')
            file.write('\t<OverlapVertical>' + str(self.overlapVertical) + '</OverlapVertical>\n')
            file.write('\t<AlturaVuelo>' + str(self.alturaVuelo) + '</AlturaVuelo>\n')
            file.write('\t<Orientacion>' + self.orientacion + '</Orientacion>\n')
            file.write('\t<FechaVuelo>' + self.fechaVuelo + '</FechaVuelo>\n')
            for each in self.Camaras:
                file.write('\t<Camara>\n')
                file.write('\t\t<NombreCamara>' + each.nombreCamara + '</NombreCamara>\n')
                file.write('\t\t<AnchoSensor>' + str(each.anchoSensor) + '</AnchoSensor>\n')
                file.write('\t\t<AlturaSensor>' + str(each.alturaSensor) + '</AlturaSensor>\n')
                file.write('\t\t<AnchoPixeles>' + str(each.anchoPixeles) + '</AnchoPixeles>\n')
                file.write('\t\t<AlturaPixeles>' + str(each.alturaPixeles) + '</AlturaPixeles>\n')
                file.write('\t\t<LargoFocal>' + str(each.largoFocal) + '</LargoFocal>\n')
                file.write('\t\t<TipoEspectro>' + each.tipo + '</TipoEspectro>\n')
                file.write('\t</Camara>\n')
            file.write('\t<DireccionImagenes>' + self.direccionImagenes + '</DireccionImagenes>\n')
            file.write('\t<Checkpoint>' + str(self.checkpoint) + '</Checkpoint>\n')
            file.write('\t<Reporte>\n')
            file.write('\t</Reporte>\n')
            file.write('\t<Ortofotos>\n')
            file.write('\t</Ortofotos>\n')
            file.write('</Proyecto>')

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
        if not (
                Path(
                    self.VProy.le_direccion_imagenes.text()).exists()) or self.VProy.le_direccion_imagenes.text() == '':
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
        elif self.VProy.le_nombre_proyecto.text() + '.SIPaF' in self.proyectNames:
            qtw.QMessageBox.warning(self, 'Error', 'El nombre del proyecto ya está en uso.')
        else:
            self.nombreProyecto = self.VProy.le_nombre_proyecto.text()
            self.direccionImagenes = self.VProy.le_direccion_imagenes.text()
            camaraRGB = self.getCamaraData(self.VProy.cb_camara1.currentText())
            camaraRGB = Camara(camaraRGB[0], camaraRGB[1], camaraRGB[2], camaraRGB[3], camaraRGB[4], camaraRGB[5], camaraRGB[6])
            camaraIR = self.getCamaraData(self.VProy.cb_camara2.currentText())
            camaraIR = Camara(camaraIR[0], camaraIR[1], camaraIR[2], camaraIR[3], camaraIR[4], camaraIR[5], camaraIR[6])
            self.Camaras = [camaraRGB, camaraIR]
            self.hide()
            self.CVDatosVuelo = CVDatosVuelos()
            self.clicksDatosVuelo()

    def clicksDatosVuelo(self):
        self.CVDatosVuelo.VDatosVuelos.pb_guardar.clicked.connect(self.verifyVDatosVuelo)
        self.CVDatosVuelo.VDatosVuelos.pb_atras.clicked.connect(self.getBack)
        self.CVDatosVuelo.VDatosVuelos.pb_cancelar.clicked.connect(self.closeVDatosVuelos)

    def getBack(self):
        self.closeVDatosVuelos()
        self.show()

    def closeVDatosVuelos(self):
        self.CVDatosVuelo.close()

    def verifyVDatosVuelo(self):
        if self.CVDatosVuelo.verifyEntryData():
            self.readVDatosVuelo()
            self.createProy()
            self.closeVDatosVuelos()
            self.closeProy()

    def readVDatosVuelo(self):
        self.anchoCubierto = self.CVDatosVuelo.VDatosVuelos.le_ancho_cubierto.text()
        self.largoCubierto = self.CVDatosVuelo.VDatosVuelos.le_largo_cubierto.text()
        self.overlapHorizontal = self.CVDatosVuelo.VDatosVuelos.le_overlap_horizontal.text()
        self.overlapVertical = self.CVDatosVuelo.VDatosVuelos.le_overlap_vertical.text()
        self.alturaVuelo = self.CVDatosVuelo.VDatosVuelos.le_altura_vuelo.text()
        self.orientacion = self.CVDatosVuelo.VDatosVuelos.cb_orientacion.currentText()
        self.fechaVuelo = self.CVDatosVuelo.VDatosVuelos.dTE_fecha_vuelo.text()

    def getCamaraData(self, nombreCamara):
        # read SIPaF.CAM file and get the data of the camera selected
        with open('SIPaF.CAM', 'r+') as file:
            data = file
            for each in data:
                if '<NombreCamara>' + nombreCamara + '</NombreCamara>' in each:
                    nextline = next(data)
                    # read next line to get ancho sensor by splitting the string
                    ancho_sensor = nextline.split('<AnchoSensor>')[1].split('</AnchoSensor>')[0]
                    nextline = next(data)
                    # read next line to get largo sensor by splitting the string
                    altura_sensor = nextline.split('<AlturaSensor>')[1].split('</AlturaSensor>')[0]
                    nextline = next(data)
                    # read next line to get ancho pixel by splitting the string
                    ancho_pixeles = nextline.split('<AnchoPixeles>')[1].split('</AnchoPixeles>')[0]
                    nextline = next(data)
                    # read next line to get largo pixel by splitting the string
                    altura_pixeles = nextline.split('<AlturaPixeles>')[1].split('</AlturaPixeles>')[0]
                    nextline = next(data)
                    # read next line to get focal by splitting the string
                    largo_focal = nextline.split('<LargoFocal>')[1].split('</LargoFocal>')[0]
                    nextline = next(data)
                    # read next line to get tipo by splitting the string
                    tipo = nextline.split('<TipoEspectro>')[1].split('</TipoEspectro>')[0]
                    return nombreCamara, ancho_sensor, altura_sensor, ancho_pixeles, altura_pixeles, largo_focal, tipo
        return None

class CVDatosVuelos(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.VDatosVuelos = Ui_VDatosVuelo()
        self.VDatosVuelos.setupUi(self)
        # self.clicksVuelos()
        self.show()

    def verifyEntryData(self):
        ancho = self.VDatosVuelos.le_ancho_cubierto.text()
        largo = self.VDatosVuelos.le_largo_cubierto.text()
        overlapHoriontal = self.VDatosVuelos.le_overlap_horizontal.text()
        overlapVertical = self.VDatosVuelos.le_overlap_vertical.text()
        altura = self.VDatosVuelos.le_altura_vuelo.text()
        fecha = self.VDatosVuelos.dTE_fecha_vuelo.text()

        # check if the entry data is not empty
        if not ancho or not largo or not overlapHoriontal or not overlapVertical or not altura or not fecha:
            qtw.QMessageBox.warning(self, 'Error', 'Por favor ingrese todos los datos')
            return False
        # check if the entry data is a float number
        else:
            try:
                float(ancho)
                float(largo)
                float(overlapHoriontal)
                float(overlapVertical)
                float(altura)
            except ValueError:
                qtw.QMessageBox.warning(self, 'Error', 'Por favor ingrese solo números')
                return False
        return True
