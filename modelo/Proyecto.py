from modelo import DIRECCION_VUELO
from modelo import Camara
from modelo import Ortofoto
from modelo import Reporte

from pathlib import Path
from typing import *
import datetime


class Proyecto:
    """
    Esta clase es la encrgada de crear los nuevos proyectos, los cuales se guardan en la carpeta del EDT
    Para crear un proyecto se necesita:
    - Nombre del proyecto
    - Ancho cubierto por el vuelo en metros
    - Largo cubierto por el vuelo en metros
    - Overlap vertical entre las imágenes tomadas
    - Overlap horizontal entre las imágenes tomadas
    - Altura de vuelo en metros
    - Fecha de vuelo en formato datetime
    - Lista con los nombres de las cámaras utilizadas
    - Dirección de las imágenes tomadas
    - Checkpoint del vuelo
    - Lista de ortofotos generadas
    - Reporte del vuelo
    """

    def __init__(self, nombreProyecto: AnyStr, anchoCubierto: int, largoCubierto: int, overlapHorizontal: int,
                 overlapVertical: int, alturaVuelo: int, orientacion: DIRECCION_VUELO,
                 fechaVuelo: datetime, Camaras: list[Camara], direccionImagenes: str, checkpoint: int = 0,
                 Ortofotos: list[Ortofoto] = [], Reporte: Reporte = None):
        self.nombreProyecto = nombreProyecto
        self.anchoCubierto = anchoCubierto
        self.largoCubierto = largoCubierto
        self.overlapVertical = overlapVertical
        self.overlapHorizontal = overlapHorizontal
        self.alturaVuelo = alturaVuelo
        self.orientacion = orientacion
        self.fechaVuelo = fechaVuelo
        self.Camaras = Camaras
        self.direccionImagenes = direccionImagenes
        self.checkpoint = checkpoint
        self.Ortofotos = Ortofotos
        self.Reporte = Reporte
