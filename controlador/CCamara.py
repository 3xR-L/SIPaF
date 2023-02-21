# Describe how to create a new document with the camara information.
from PyQt5 import QtWidgets as qtw

from vista.VCamara import Ui_VCamara
from modelo.TIPO_ESPECTRO import TIPO_ESPECTRO


class CCamara(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.VCamara = None
        try:
            with open('SIPaF.CAM', 'r') as f:
                self.fileCAM = f
                self.camaras, self.tipos = self.fillCamaraData()
        except FileNotFoundError:
            self.fileCAM = None
            self.camaras, self.tipos = self.fillCamaraData()

    def openVCamara(self):
        try:
            with open('SIPaF.CAM', 'r') as f:
                self.VCamara = Ui_VCamara()
                self.VCamara.setupUi(self)
                self.fileCAM = f
                self.camaras, _ = self.fillCamaraData()
                self.updateCamaraValues()
                self.loadCamaraTypes()
                self.clicks()
                self.show()
                self.exec_()
        except FileNotFoundError:
            pass

    def loadCamaraTypes(self):
        self.VCamara.cb_tipo_camaras.addItem("RGB", TIPO_ESPECTRO.RGB)
        self.VCamara.cb_tipo_camaras.addItem("TERMICA", TIPO_ESPECTRO.TERMICA)

    def clicks(self):
        self.VCamara.pb_cancelar_camara.clicked.connect(self.closeCamara)
        self.VCamara.pb_guardar_camara.clicked.connect(self.saveCamara)
        self.VCamara.pb_eliminarar_camara.clicked.connect(self.deleteCamara)

        # update values when the user changes the value of the combo box
        self.VCamara.cb_nombre_camara.currentIndexChanged.connect(self.updateCamaraValues)

    def fillCamaraData(self):
        # read the file line by line
        camaras = []
        tipos = []
        if self.fileCAM is not None:
            self.fileCAM.seek(0)
            for line in self.fileCAM:
                if '<NombreCamara>' in line:
                    nombreCamara = line.split('<NombreCamara>')[1].split('</NombreCamara>')[0]
                    if self.VCamara is not None:
                        self.VCamara.cb_nombre_camara.addItem(nombreCamara)
                    line = next(self.fileCAM)
                    line = next(self.fileCAM)
                    line = next(self.fileCAM)
                    line = next(self.fileCAM)
                    line = next(self.fileCAM)
                    line = next(self.fileCAM)
                    tipo_espectro = line.split('<TipoEspectro>')[1].split('</TipoEspectro>')[0]
                    camaras.append(nombreCamara)
                    tipos.append(tipo_espectro)
        return camaras, tipos

    def updateCamaraValues(self):
        # get the data from the file
        # update the values in the line edits
        self.fileCAM.seek(0)
        nombreCamara = self.VCamara.cb_nombre_camara.currentText()
        for line in self.fileCAM:
            if '<NombreCamara>'+nombreCamara in line:
                # read the next 6 lines
                for i in range(6):
                    line = next(self.fileCAM)
                    if '<AnchoSensor>' in line:
                        ancho_sensor = line.split('<AnchoSensor>')[1].split('</AnchoSensor>')[0]
                        self.VCamara.le_ancho_sensor.setText(ancho_sensor)
                    elif '<AlturaSensor>' in line:
                        altura_sensor = line.split('<AlturaSensor>')[1].split('</AlturaSensor>')[0]
                        self.VCamara.le_altura_sensor.setText(altura_sensor)
                    elif '<AnchoPixeles>' in line:
                        ancho_pixeles = line.split('<AnchoPixeles>')[1].split('</AnchoPixeles>')[0]
                        self.VCamara.le_ancho_pixeles.setText(ancho_pixeles)
                    elif '<AlturaPixeles>' in line:
                        altura_pixeles = line.split('<AlturaPixeles>')[1].split('</AlturaPixeles>')[0]
                        self.VCamara.le_altura_pixeles.setText(altura_pixeles)
                    elif '<LargoFocal>' in line:
                        largo_focal = line.split('<LargoFocal>')[1].split('</LargoFocal>')[0]
                        self.VCamara.le_largo_focal.setText(largo_focal)
                    elif '<TipoEspectro>' in line:
                        tipo_espectro = line.split('<TipoEspectro>')[1].split('</TipoEspectro>')[0]
                        self.VCamara.cb_tipo_camaras.setCurrentText(tipo_espectro)

    def closeCamara(self):
        self.close()

    def saveCamara(self):
        # search for a file named SIPaF.CAM
        # if it doesn't exist, create it
        # if it does exist, append the new camera information
        # close the window
        nombre = self.VCamara.cb_nombre_camara.currentText()
        ancho_sensor = self.VCamara.le_ancho_sensor.text()
        altura_sensor = self.VCamara.le_altura_sensor.text()
        ancho_pixeles = self.VCamara.le_ancho_pixeles.text()
        altura_pixeles = self.VCamara.le_altura_pixeles.text()
        largo_focal = self.VCamara.le_largo_focal.text()
        tipo = self.VCamara.cb_tipo_camaras.currentText()

        if self.verifyEntryData(nombre, ancho_sensor, altura_sensor, ancho_pixeles, altura_pixeles, largo_focal, tipo):
            with open('SIPaF.CAM', 'a+') as f:
                self.fileCAM = f
                self.addCamara(nombre, ancho_sensor, altura_sensor, ancho_pixeles, altura_pixeles, largo_focal, tipo)
            self.close()
        else:
            # show error message
            qtw.QMessageBox.critical(self, "Error", "Los datos ingresados no son válidos.")

    def verifyEntryData(self, nombre, ancho_sensor, altura_sensor, ancho_pixeles, altura_pixeles, largo_focal, tipo):
        # verify that all the fields have been filled
        # verify that the data is correct
        # return True if everything is correct, False otherwise
        if nombre == "" or ancho_sensor == "" or altura_sensor == "" or ancho_pixeles == "" or altura_pixeles == "" or \
                largo_focal == "" :
            print(nombre=="")
            print(ancho_sensor=="")
            print(altura_sensor=="")
            print(ancho_pixeles=="")
            print(altura_pixeles=="")
            print(largo_focal=="")
            return False
        # verify that the data is float or int
        try:
            float(ancho_sensor)
            float(altura_sensor)
            int(ancho_pixeles)
            int(altura_pixeles)
            float(largo_focal)
        except ValueError:
            return False

        if nombre in self.camaras:
            self.deleteCamara(True)
            return True
        return True

    def addCamara(self, nombre, ancho_sensor, altura_sensor, ancho_pixeles, altura_pixeles, largo_focal, tipo):
        self.fileCAM.write("<CAMARA>\n")
        self.fileCAM.write('\t<NombreCamara>' + nombre + '</NombreCamara>\n')
        self.fileCAM.write('\t<AnchoSensor>' + ancho_sensor + '</AnchoSensor>\n')
        self.fileCAM.write('\t<AlturaSensor>' + altura_sensor + '</AlturaSensor>\n')
        self.fileCAM.write('\t<AnchoPixeles>' + ancho_pixeles + '</AnchoPixeles>\n')
        self.fileCAM.write('\t<AlturaPixeles>' + altura_pixeles + '</AlturaPixeles>\n')
        self.fileCAM.write('\t<LargoFocal>' + largo_focal + '</LargoFocal>\n')
        self.fileCAM.write('\t<TipoEspectro>' + tipo + '</TipoEspectro>\n')
        self.fileCAM.write("</CAMARA>\n")

    def deleteCamara(self, continuar=False):
        # delete the camera from the file
        # close the window
        nombre = self.VCamara.cb_nombre_camara.currentText()
        newFile = []
        with open('SIPaF.CAM', 'r+') as f:
            for line in f:
                if '<NombreCamara>'+nombre in line:
                    newFile.pop()
                    next(f)
                    next(f)
                    next(f)
                    next(f)
                    next(f)
                    next(f)
                    next(f)
                else:
                    newFile.append(line)
                    # write the new file
        #Create a new file and write the new file
        with open('SIPaF.CAM', 'w+') as newF:
            newF.writelines(newFile)
        if not continuar:
            self.close()