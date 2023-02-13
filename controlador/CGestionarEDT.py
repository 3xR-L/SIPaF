import os
import sys
import shutil

from modelo.EspacioDeTrabajo import EspacioDeTrabajo
from vista.VGestionarEDT import Ui_VGestionarEDT

from datetime import datetime
from PyQt5 import QtWidgets as qtw


class CGestionarEDT(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.mEDT = None
        self.edts = []
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
        self.updateComboBox()
        self.updatePath()
        self.clicks()
        self.show()
        self.exec_()

    def clicks(self):
        self.VGEDT.pb_crear.clicked.connect(self.addEDT)
        self.VGEDT.pb_eliminar.clicked.connect(self.confirmDeleteEDT)
        self.VGEDT.pb_cancelar.clicked.connect(self.closeEDT)

        self.VGEDT.pb_folder.clicked.connect(self.selectFolder)

        #check if an EDT of the combobox has been selected
        self.VGEDT.comboBox_EDT.currentIndexChanged.connect(self.updatePath)

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
                self.edts.append(EspacioDeTrabajo(nombreEDT, ultimaModificacion, direccion, correoElectronico))
                if lastMod is None or ultimaModificacion > lastMod:
                    lastMod = ultimaModificacion
                    self.mEDT = EspacioDeTrabajo(nombreEDT, ultimaModificacion, direccion, correoElectronico)
        if self.mEDT is None:
            self.openVGEDT()

    def addEDT(self):
        currentName = self.VGEDT.comboBox_EDT.currentText()
        if self.open_existingEDT(currentName):
            self.closeEDT()
            return

        # check the name has a character and a folder is selected
        if self.verifyEDTName(currentName):
            qtw.QMessageBox.critical(self, 'Error', 'Debe ingresar un nombre nuevo y seleccionar una carpeta')
            return
        # get data from VEDT
        nombre = self.VGEDT.comboBox_EDT.currentText()
        carpeta = self.VGEDT.label_carpeta.text()
        fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        # add the new EDT to SIPaF.EDT
        with open('SIPaF.EDT', 'a') as f:
            f.write(f'''<EDT>\n\t<NombreEDT>{nombre}</NombreEDT>\n\t<UltimaModificacion>{fecha}</UltimaModificacion>\n\t<Direccion>{carpeta}</Direccion>\n\t<CorreoElectronico>NA</CorreoElectronico>\n</EDT>\n''')
        self.mEDT = EspacioDeTrabajo(nombre, fecha, carpeta)
        # create the folder with the name of the EDT
        os.makedirs(carpeta + '/' + nombre)
        # wait until the folder is created
        while not os.path.exists(carpeta + '/' + nombre):
            pass

        self.edts.append(self.mEDT)

        # close the window
        self.close()

    def verifyEDTName(self, currentName=None):
        # verify if the EDT name already exists
        if currentName == 'Seleccione espacio o cree uno nuevo' or \
        not os.path.exists(self.VGEDT.label_carpeta.text()) or currentName == '' or \
            os.path.exists(self.VGEDT.label_carpeta.text() + '/' + currentName):
            return True

        return False

    def open_existingEDT(self, currentName):
        # open the edt that already exists
        for edt in self.edts:
            if edt.nombreEDT == currentName and edt.direccion == self.VGEDT.label_carpeta.text() and \
                    currentName != self.mEDT.nombreEDT:
                # open the edt that already exists
                self.mEDT = edt
                return True
        return False

    def closeEDT(self):
        self.close()

    def confirmDeleteEDT(self):
        # show a message to confirm the deletion
        msg = qtw.QMessageBox()
        msg.setIcon(qtw.QMessageBox.Warning)
        msg.setText('¿Está seguro que desea eliminar el espacio de trabajo?')
        msg.setWindowTitle('Eliminar espacio de trabajo')
        msg.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        msg.buttonClicked.connect(self.deleteEDT)
        msg.exec_()

    ### probar ###
    def deleteEDT(self):
        # delete the EDT from SIPaF.EDT
        nombre = self.VGEDT.comboBox_EDT.currentText()

        if nombre != 'Seleccione espacio o cree uno nuevo' and self.mEDT.nombreEDT != nombre:
            newFile = []
            # write the file without the EDT to delete
            with open('SIPaF.EDT', 'r+') as f:
                lines = f
                for line in lines:
                    print(line)
                    if '<NombreEDT>'+nombre+'</NombreEDT>' in line:
                        newFile.pop()
                        next(lines)
                        next(lines)
                        next(lines)
                        next(lines)
                    else:
                        newFile.append(line)
            # Eliminate edt from edts
            for edt in self.edts:
                if edt.nombreEDT == nombre:
                    dirRem = edt.direccion
                    self.edts.remove(edt)
                    break
            # write the new file
            with open('SIPaF.EDT', 'w+') as f:
                f.writelines(newFile)
            # delete the folder and its content
            shutil.rmtree(dirRem + '/' + nombre)
            # close the window
            self.close()

    def updateComboBox(self):
        # update the combobox
        self.VGEDT.comboBox_EDT.clear()
        #self.ui.comboBox_EDT.addItem('Seleccione espacio o cree uno nuevo')
        for edt in self.edts:
            self.VGEDT.comboBox_EDT.addItem(edt.nombreEDT)

    def updatePath(self):
        # update the path
        if self.mEDT is not None:
            self.VGEDT.label_carpeta.setText(self.mEDT.direccion)