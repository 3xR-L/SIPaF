import os
import sys

from vista.VGestionarEDT import Ui_VGestionarEDT
from modelo.EspacioDeTrabajo import EspacioDeTrabajo

from datetime import datetime
from PyQt5 import QtWidgets as qtw


class CGestionarEDT(qtw.QDialog):
    def __init__(self, start=False, fileEDT=None):
        super().__init__()
        self.start = start
        try:
            # read the file and create a list of lines
            with open('SIPaF.EDT', 'r+') as file:
                self.file = True
                self.fileEDT = file
                # search for the EDTs
                self.searchEDTs()
        except FileNotFoundError:
            print(self.start)
            self.file = False
            # Open VGestionarEDT
            self.openVGestionarEDT()

    def createSIPafEDTFile(self, nombre):
        EDTfle = open('SIPaF.EDT', 'a')
        EDTfle.write('<EDT>\n')
        EDTfle.write('\t<NombreEDT>' + nombre + '</NombreEDT>\n')
        EDTfle.write(
            '\t<UltimaModificacion>' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '</UltimaModificacion>\n')
        EDTfle.write('\t<CorreoElectronico>NA</CorreoElectronico>\n')
        EDTfle.write('\t<Direccion>' + self.ui.label_carpeta.text() + '</Direccion>\n')
        EDTfle.write('</EDT>\n')
        EDTfle.close()

    def searchEDTs(self):
        self.edts = list()
        lastMod = None
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
                    ultimoEDT = list()
                    ultimoEDT = [nombreEDT, ultimaModificacion, direccion, correoElectronico]

        # check if there are any EDTs
        if lastMod != None:
            # pass the edt to VGestionarEDT
            self.mEDT = EspacioDeTrabajo(ultimoEDT[0], ultimoEDT[1], ultimoEDT[2], ultimoEDT[3])
        else:
            self.openVGestionarEDT()

    # open VGestionarEDT
    def openVGestionarEDT(self):
        if self.file:
            print('file')
            # open VGestionarEDT
            self.ui = Ui_VGestionarEDT()
            self.ui.setupUi(self)
            self.updateComboBox()
            self.clicks()
            self.show()
            # wait for the window to close
            self.exec_()
        else:
            # open VGestionarEDT
            self.ui = Ui_VGestionarEDT()
            self.ui.setupUi(self)
            self.clicks()
            self.show()
            # wait for the window to close
            self.exec_()

    def updateComboBox(self):
        # update the combobox
        self.ui.comboBox_EDT.clear()
        self.ui.comboBox_EDT.addItem('Seleccione espacio o cree uno nuevo')
        for edt in self.edts:
            self.ui.comboBox_EDT.addItem(edt.nombreEDT)

    def clicks(self):
        self.ui.pb_abrir_crear.clicked.connect(self.create_openEDT)
        self.ui.pb_cancelar.clicked.connect(self.close)
        self.ui.pb_eliminar.clicked.connect(self.deleteEDT)
        self.ui.pb_folder.clicked.connect(self.openFolder)
        # Add action if enter is pressed in the combobox
        self.ui.comboBox_EDT.lineEdit().returnPressed.connect(self.create_openEDT)

    def openFolder(self):
        # open a window to choose a path in the system
        path = qtw.QFileDialog.getExistingDirectory(self, 'Seleccione la carpeta donde se guardaran los proyectos')
        self.ui.label_carpeta.setText(path)

    def deleteEDT(self):
        nombre = self.ui.comboBox_EDT.currentText().strip()
        if nombre != 'Seleccione espacio o cree uno nuevo':
            # delete an EDT from the file
            with open('SIPaF.EDT', 'w') as file:
                file = file.readlines()
                newfile = []
                append = True
                for line in self.fileEDT:
                    if append and nombre not in line:
                        newfile.append(line)
                    else:
                        newfile.pop()
                        append = False
                        if '<EDT>' in line:
                            append = True
                    print(newfile)
                    file.writeLines(newfile)
                file.close()

    def create_openEDT(self):
        if self.file:
            print("open")
            if self.ui.comboBox_EDT.currentText().strip() != 'Seleccione espacio o cree uno nuevo':
                nombre = self.ui.le_nombre.text().strip()
                # check if nombre has no spaces at the beginning or end
                if nombre != '':
                    # check if the EDT already exists
                    if  nombre in self.edts:
                        # create a
                        self.openVEDT(nombre)
                        self.close()
                    else:
                        # add the EDT to the file
                        direccion = self.ui.label_carpeta.text().strip()
                        if direccion != '':
                            tiempo = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                            self.addEDT(nombre, direccion, tiempo)
                            self.mEDT = EspacioDeTrabajo(nombre, tiempo, direccion, 'NA')
                            self.close()
                else:
                    qtw.QMessageBox.warning(self, 'Error', 'Ingrese un nombre para el EDT')
        else:
            # set nombre and eliminate end spaces
            nombre = self.ui.comboBox_EDT.currentText().strip()
            direccion = self.ui.label_carpeta.text().strip()
            if nombre != 'Seleccione espacio o cree uno nuevo':
                if direccion != 'Elegir carpeta':
                    # create a folder with the name of the EDT
                    os.mkdir(direccion + '/' + nombre)
                    tiempo = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    self.createEDTFile(nombre, tiempo, direccion)
                    self.mEDT = EspacioDeTrabajo(nombre, tiempo, direccion)
                    self.close()

    def createEDTFile(self, nombre, tiempo, direccion):
        EDTfle = open('SIPaF.EDT', 'w')
        EDTfle.write('<EDT>\n')
        EDTfle.write('\t<NombreEDT>' + nombre + '</NombreEDT>\n')
        EDTfle.write('\t<UltimaModificacion>' + tiempo + '</UltimaModificacion>\n')
        EDTfle.write('\t<Direccion>' + direccion + '</Direccion>\n')
        EDTfle.write('\t<CorreoElectronico>NA</CorreoElectronico>\n')
        EDTfle.write('</EDT>\n')
        EDTfle.close()
        self.file = True

    def addEdt(self, nombre, direccion, tiempo):
        # add the EDT to the file
        with open('SIPaF.EDT', 'a') as file:
            file.write('<EDT>\n')
            file.write('\t<NombreEDT>' + nombre + '</NombreEDT>\n')
            file.write('\t<UltimaModificacion>' + tiempo + '</UltimaModificacion>\n')
            file.write('\t<Direccion>' + direccion + '</Direccion>\n')
            file.write('\t<CorreoElectronico>NA</CorreoElectronico>\n')
            file.write('</EDT>\n')
            file.close()