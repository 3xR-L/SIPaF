import os
import sys

from modelo.EspacioDeTrabajo import EspacioDeTrabajo
from vista.VGestionarEDT import Ui_VGestionarEDT

from datetime import datetime
from PyQt5 import QtWidgets as qtw


class CGestionarEDT(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.mEDT = None
        # read or create file SIPaF.EDT
        try:
            with open('SIPaF.EDT', 'r+') as f:
                self.fileEDT = f
                self.searchLastEDT()

        except FileNotFoundError:
            with open('SIPaF.EDT', 'w') as f:
                self.fileEDT = f.write('')
                self.openVGEDT()

    def openVGEDT(self):
        self.VGEDT = Ui_VGestionarEDT()
        self.VGEDT.setupUi(self)
        self.clicks()
        self.show()
        self.exec_()

    def clicks(self):
        self.VGEDT.pb_crear.clicked.connect(self.addEDT)
        self.VGEDT.pb_eliminar.clicked.connect(self.eliminarEDT)
        self.VGEDT.pb_cancelar.clicked.connect(self.closeEDT)

        self.VGEDT.pb_folder.clicked.connect(self.selectFolder)

    def selectFolder(self):
        self.VGEDT.label_carpeta.setText(qtw.QFileDialog.getExistingDirectory(self, 'Seleccionar carpeta'))

    def searchLastEDT(self):
        lastMod = None
        # read the file line by line
        for line in self.fileEDT:
            if '<NombreEDT>' in line:
                nombreEDT = line.split('<NombreEDT>')[1].split('</NombreEDT>')[0]
                # read next line
                nextLine = next(self.fileEDT)
                ultimaModificacion = nextLine.split('<UltimaModificacion>')[1].split('</UltimaModificacion>')[0]
                ultimaModificacion = datetime.strptime(ultimaModificacion, '%d/%m/%Y %H:%M:%S')
                nextLine = next(self.fileEDT)
                direccion = nextLine.split('<Direccion>')[1].split('</Direccion>')[0]
                nextLine = next(self.fileEDT)
                correoElectronico = nextLine.split('<CorreoElectronico>')[1].split('</CorreoElectronico>')[0]
                if lastMod is None or ultimaModificacion > lastMod:
                    lastMod = ultimaModificacion
                    self.mEDT = EspacioDeTrabajo(nombreEDT, ultimaModificacion, direccion, correoElectronico)
        if self.mEDT is None:
            self.openVGEDT()

    def addEDT(self):
        # check the name has a character and a folder is selected
        if self.VGEDT.comboBox_EDT.currentText() == 'Seleccione espacio o cree uno nuevo' or \
                self.VGEDT.label_carpeta.text() == 'Elegir carpeta' or self.VGEDT.comboBox_EDT.currentText() == '':
            qtw.QMessageBox.critical(self, 'Error', 'Debe ingresar un nombre y seleccionar una carpeta')
            return
        # get data from VEDT
        nombre = self.VGEDT.comboBox_EDT.currentText()
        carpeta = self.VGEDT.label_carpeta.text()
        fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        # add the new EDT to SIPaF.EDT
        with open('SIPaF.EDT', 'a') as f:
            f.write(f'''<EDT>\n\t<NombreEDT>{nombre}</NombreEDT>\n\t<UltimaModificacion>{fecha}</UltimaModificacion>\n\t<Direccion>{carpeta}</Direccion>\n\t<CorreoElectronico>NA</CorreoElectronico>\n</EDT>\n''')
        self.mEDT = EspacioDeTrabajo(nombre, carpeta, fecha)
        # create the folder with the name of the EDT
        os.makedirs(carpeta + '/' + nombre)



        # close the window
        self.close()

    def closeEDT(self):
        self.close()

    ### probar ###
    def eliminarEDT(self):
        pass

    def updateComboBox(self):
        # update the combobox
        self.ui.comboBox_EDT.clear()
        self.ui.comboBox_EDT.addItem('Seleccione espacio o cree uno nuevo')
        for edt in self.edts:
            self.ui.comboBox_EDT.addItem(edt.nombreEDT)