from typing import *

from modelo.TIPO_ESPECTRO import TIPO_ESPECTRO

class Camara:
    '''
    Clase que representa una cámara para el archivo SIPaF.CAM
    <CAMARA>
        <NombreCamara>safwaerat</NombreCamara>
        <AnchoSensor>500</AnchoSensor>
        <AlturaSensor>456.1</AlturaSensor>
        <AnchoPixeles>456.564</AnchoPixeles>
        <AlturaPixeles>4678.78</AlturaPixeles>
        <LargoFocal>4567</LargoFocal>
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
