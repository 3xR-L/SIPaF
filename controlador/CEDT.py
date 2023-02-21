from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileSystemModel
from controlador.CGestionarEDT import CGestionarEDT
from controlador.CProy import CProy
from controlador.CProy import readProyData
from controlador.COrtofoto import COrtofoto
from modelo.EspacioDeTrabajo import EspacioDeTrabajo
from vista.VEDT import Ui_VEDT

from PyQt5 import QtWidgets as qtw, QtGui

import os
from shutil import rmtree
import PyQt5.QtGui as qtg


class CEDT(qtw.QMainWindow):
    def __init__(self):
        self.CGEDT = CGestionarEDT()
        self.CProy = None
        self.Proy = None
        if self.CGEDT.mEDT is None:
            pass
        else:
            super().__init__()
            self.VEDT = Ui_VEDT()
            self.VEDT.setupUi(self)
            self.loadProjects()
            self.clicks()
            self.proyNames = self.readProyNames()
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
        self.VEDT.proyecto_eliminar.triggered.connect(self.eliminateProy)
        self.VEDT.pb_iniciar_proceso.clicked.connect(self.crearCOrtofoto)
        self.VEDT.vista_arbol_proyectos.doubleClicked.connect(self.openProy)

        # search file on EDT tree view
        self.VEDT.pb_buscar.clicked.connect(self.searchFile)

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
        self.CProy = None
        self.CProy = CProy(self.proyNames, self.CGEDT.mEDT.direccion + '/' + self.CGEDT.mEDT.nombreEDT)
        self.CProy.openVProy()

    def readProyNames(self):
        # read all files in the EDT directory with the extension .SIPaF
        # and return a list with the names of the projects
        projects = []
        print(self.CGEDT.mEDT.direccion + '/' + self.CGEDT.mEDT.nombreEDT)
        for file in os.listdir(self.CGEDT.mEDT.direccion + '/' + self.CGEDT.mEDT.nombreEDT):
            projects.append(file)
        return projects

    def searchFile(self):
        # search for a file name in the EDT directory
        # show it in the tree view
        file = self.VEDT.le_buscar.text()
        if file != '':
            for root, dirs, files in os.walk(self.CGEDT.mEDT.direccion + '/' + self.CGEDT.mEDT.nombreEDT):
                # check if the text is within a file name or a directory name
                # even though it is not case sensitive
                # lowercase all the files and directories
                # even though it does not completely mathch the file name
                files = [f.lower() for f in files]
                dirs = [d.lower() for d in dirs]
                file = file.lower()
                for i in range(len(files)):
                    if file in files[i]:
                        # get the index of the file
                        index = self.model.index(root + '/' + files[i])
                        # select the file
                        self.VEDT.vista_arbol_proyectos.setCurrentIndex(index)
                        self.VEDT.vista_arbol_proyectos.scrollTo(index)
                        break
                for i in range(len(dirs)):
                    if file in dirs[i]:
                        # get the index of the file
                        index = self.model.index(root + '/' + dirs[i])
                        # select the file
                        self.VEDT.vista_arbol_proyectos.setCurrentIndex(index)
                        self.VEDT.vista_arbol_proyectos.scrollTo(index)
                        break

    def eliminateProy(self):
        # eliminate a project from the EDT
        # delete the project folder selected in the tree view
        # update the list of projects
        # update the tree view
        index = self.VEDT.vista_arbol_proyectos.currentIndex()
        name = self.model.fileName(index)
        if index.isValid():
            if name != self.CGEDT.mEDT.nombreEDT and name in self.proyNames:
                # eliminate the project folder from the EDT
                try:
                    # show a message box to confirm the elimination
                    msg = qtw.QMessageBox()
                    msg.setIcon(qtw.QMessageBox.Warning)
                    msg.setText("¿Está seguro que desea eliminar todo el proyecto?")
                    msg.setWindowTitle("Eliminar proyecto")
                    msg.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
                    # set icon for the message window
                    msg.setWindowIcon(qtg.QIcon("images/SIPaF.png"))
                    retval = msg.exec_()

                    if retval == qtw.QMessageBox.Ok:
                        rmtree(self.CGEDT.mEDT.direccion + '/' + self.CGEDT.mEDT.nombreEDT + '/' + name)
                except Exception as e:
                    print(e)
                self.proyNames = self.readProyNames()
                self.loadProjects()
        else:
            print('No file selected')

    def crearCOrtofoto(self):
        # create a new orthophoto
        # open a new window to select the parameters
        # create the orthophoto
        if self.Proy is not None:
            self.COrtof = None
            self.COrtof = COrtofoto(self.CGEDT.mEDT.direccion + '/' + self.CGEDT.mEDT.nombreEDT + '/' + self.Proy.nombreProyecto)
            self.COrtof.preprocesarImagenes(self.Proy.direccionImagenes, self.Proy.Camaras, self.Proy.alturaVuelo)

    def openProy(self):
        # open a project
        # open a new window to select the parameters
        # create the orthophoto
        index = self.VEDT.vista_arbol_proyectos.currentIndex()
        name = self.model.fileName(index)
        if name.endswith(".SIPaF"):
            self.Proy = readProyData(self.CGEDT.mEDT.direccion + '/' + self.CGEDT.mEDT.nombreEDT + '/', name)
