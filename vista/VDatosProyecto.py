# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VDatosProyecto.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VDatosProyecto(object):
    def setupUi(self, VDatosProyecto):
        VDatosProyecto.setObjectName("VDatosProyecto")
        VDatosProyecto.setWindowModality(QtCore.Qt.ApplicationModal)
        VDatosProyecto.resize(735, 203)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VDatosProyecto.sizePolicy().hasHeightForWidth())
        VDatosProyecto.setSizePolicy(sizePolicy)
        VDatosProyecto.setMinimumSize(QtCore.QSize(735, 203))
        VDatosProyecto.setMaximumSize(QtCore.QSize(735, 203))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../PycharmProjects/SIPaF/images/SIPaF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VDatosProyecto.setWindowIcon(icon)
        VDatosProyecto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(VDatosProyecto)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_VDatosProyecto = QtWidgets.QFrame(VDatosProyecto)
        self.frame_VDatosProyecto.setStyleSheet("font: 14pt \"Arial Rounded MT Bold\";\n"
"\n"
"QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_VDatosProyecto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_VDatosProyecto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_VDatosProyecto.setObjectName("frame_VDatosProyecto")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_VDatosProyecto)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_VDatosProyecto_etiquetas = QtWidgets.QFrame(self.frame_VDatosProyecto)
        self.frame_VDatosProyecto_etiquetas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_VDatosProyecto_etiquetas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_VDatosProyecto_etiquetas.setObjectName("frame_VDatosProyecto_etiquetas")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_VDatosProyecto_etiquetas)
        self.verticalLayout.setContentsMargins(1, 2, 1, 1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_nombre_proyecto = QtWidgets.QLabel(self.frame_VDatosProyecto_etiquetas)
        self.lbl_nombre_proyecto.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_nombre_proyecto.setObjectName("lbl_nombre_proyecto")
        self.verticalLayout.addWidget(self.lbl_nombre_proyecto)
        self.lbl_direccion_imagenes = QtWidgets.QLabel(self.frame_VDatosProyecto_etiquetas)
        self.lbl_direccion_imagenes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_direccion_imagenes.setObjectName("lbl_direccion_imagenes")
        self.verticalLayout.addWidget(self.lbl_direccion_imagenes)
        self.lbl_camaras_utilizadas = QtWidgets.QLabel(self.frame_VDatosProyecto_etiquetas)
        self.lbl_camaras_utilizadas.setObjectName("lbl_camaras_utilizadas")
        self.verticalLayout.addWidget(self.lbl_camaras_utilizadas)
        self.frame_agregarCamara = QtWidgets.QFrame(self.frame_VDatosProyecto_etiquetas)
        self.frame_agregarCamara.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_agregarCamara.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_agregarCamara.setObjectName("frame_agregarCamara")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_agregarCamara)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pb_agregar_camara = QtWidgets.QPushButton(self.frame_agregarCamara)
        self.pb_agregar_camara.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.pb_agregar_camara.setObjectName("pb_agregar_camara")
        self.horizontalLayout_4.addWidget(self.pb_agregar_camara)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_agregarCamara)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.frame_VDatosProyecto_etiquetas)
        self.frame_VDatosProyecto_entradas = QtWidgets.QFrame(self.frame_VDatosProyecto)
        self.frame_VDatosProyecto_entradas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_VDatosProyecto_entradas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_VDatosProyecto_entradas.setObjectName("frame_VDatosProyecto_entradas")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_VDatosProyecto_entradas)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_nombre_proyecto = QtWidgets.QLineEdit(self.frame_VDatosProyecto_entradas)
        self.le_nombre_proyecto.setText("")
        self.le_nombre_proyecto.setObjectName("le_nombre_proyecto")
        self.verticalLayout_2.addWidget(self.le_nombre_proyecto)
        self.frame = QtWidgets.QFrame(self.frame_VDatosProyecto_entradas)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.le_direccion_imagenes = QtWidgets.QLineEdit(self.frame)
        self.le_direccion_imagenes.setText("")
        self.le_direccion_imagenes.setObjectName("le_direccion_imagenes")
        self.horizontalLayout_5.addWidget(self.le_direccion_imagenes)
        self.pb_direccion = QtWidgets.QPushButton(self.frame)
        self.pb_direccion.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.pb_direccion.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../PycharmProjects/SIPaF/images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_direccion.setIcon(icon1)
        self.pb_direccion.setObjectName("pb_direccion")
        self.horizontalLayout_5.addWidget(self.pb_direccion)
        self.verticalLayout_2.addWidget(self.frame)
        self.cb_camara1 = QtWidgets.QComboBox(self.frame_VDatosProyecto_entradas)
        self.cb_camara1.setObjectName("cb_camara1")
        self.verticalLayout_2.addWidget(self.cb_camara1)
        self.cb_camara2 = QtWidgets.QComboBox(self.frame_VDatosProyecto_entradas)
        self.cb_camara2.setObjectName("cb_camara2")
        self.verticalLayout_2.addWidget(self.cb_camara2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.frame_4 = QtWidgets.QFrame(self.frame_VDatosProyecto_entradas)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pb_siguiente = QtWidgets.QPushButton(self.frame_4)
        self.pb_siguiente.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.pb_siguiente.setObjectName("pb_siguiente")
        self.horizontalLayout_3.addWidget(self.pb_siguiente)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pb_cancelar = QtWidgets.QPushButton(self.frame_4)
        self.pb_cancelar.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.pb_cancelar.setObjectName("pb_cancelar")
        self.horizontalLayout_3.addWidget(self.pb_cancelar)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame_VDatosProyecto_entradas)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout.addWidget(self.frame_VDatosProyecto)

        self.retranslateUi(VDatosProyecto)
        QtCore.QMetaObject.connectSlotsByName(VDatosProyecto)

    def retranslateUi(self, VDatosProyecto):
        _translate = QtCore.QCoreApplication.translate
        VDatosProyecto.setWindowTitle(_translate("VDatosProyecto", "Datos del Proyecto"))
        self.lbl_nombre_proyecto.setText(_translate("VDatosProyecto", "Nombre del proyecto:"))
        self.lbl_direccion_imagenes.setToolTip(_translate("VDatosProyecto", "Lugar donde se encuentran las imagenes a procesar."))
        self.lbl_direccion_imagenes.setText(_translate("VDatosProyecto", "Dirección de las imagenes:"))
        self.lbl_camaras_utilizadas.setToolTip(_translate("VDatosProyecto", "Seleccionr las camaras utilizadas."))
        self.lbl_camaras_utilizadas.setText(_translate("VDatosProyecto", "Cámaras utilizadas:"))
        self.pb_agregar_camara.setText(_translate("VDatosProyecto", "Agregar cámara"))
        self.pb_siguiente.setText(_translate("VDatosProyecto", "Siguiente"))
        self.pb_cancelar.setText(_translate("VDatosProyecto", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VDatosProyecto = QtWidgets.QWidget()
    ui = Ui_VDatosProyecto()
    ui.setupUi(VDatosProyecto)
    VDatosProyecto.show()
    sys.exit(app.exec_())
