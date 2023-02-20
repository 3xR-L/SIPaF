from typing import *

from modelo.TIPO_ESPECTRO import TIPO_ESPECTRO

class Camara:
    '''
    Clase que representa una cámara para el archivo SIPaF.CAM
    <CAMARA>
        <NombreCamara>ZenmuseXT2</NombreCamara>
        <AnchoSensor>7.4 (mm)</AnchoSensor>
        <AlturaSensor>5.55 (mm)</AlturaSensor>
        <AnchoPixeles>4000 (pixeles)</AnchoPixeles>
        <AlturaPixeles>3000 (pixeles)</AlturaPixeles>
        <LargoFocal>8 (mm)</LargoFocal>
        <TipoEspectro>RGB</TipoEspectro>
    </CAMARA>
    '''
    def __init__(self, nombreCamara: AnyStr, anchoSensor: float, alturaSensor: float, anchoPixeles: int,
                 alturaPixeles: int, largoFocal: float, tipo: TIPO_ESPECTRO):
        self.nombreCamara = nombreCamara
        self.anchoSensor = anchoSensor
        self.alturaSensor = alturaSensor
        self.anchoPixeles = anchoPixeles
        self.alturaPixeles = alturaPixeles
        self.largoFocal = largoFocal
        self.tipo = tipo
