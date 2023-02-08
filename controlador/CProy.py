# Controller for the Proyecto entity
# It will control VDatosProyecto, VDatosVuelo, and CCamara
import datetime
from pathlib import Path
from typing import AnyStr, List

from modelo.Camara import Camara
from modelo.DIRECCION_VUELO import DIRECCION_VUELO
from modelo.Ortofoto import Ortofoto
from modelo.Reporte import Reporte


class CProy():
    def __init__(self, inicar: bool = False):
        self.iniciar = inicar
        print("hola_proyect")

    def crearProyecto(self):
        print("proyecto creado")
        pass