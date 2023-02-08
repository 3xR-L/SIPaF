from typing import *

from modelo.TIPO_ESPECTRO import TIPO_ESPECTRO

class Camara:
    def __init__(self, nombreCamara: AnyStr, anchoSensor: float, alturaSensor: float, anchoPixeles: int,
                 alturaPixeles: int, largoFocal: float, tipo: TIPO_ESPECTRO):
        self.nombreCamara = nombreCamara
        self.anchoSensor = anchoSensor
        self.alturaSensor = alturaSensor
        self.anchoPixeles = anchoPixeles
        self.alturaPixeles = alturaPixeles
        self.largoFocal = largoFocal
        self.tipo = tipo
