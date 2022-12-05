# Create a base class for the workspace

# Import the module to specify the types of the variables and the return
import datetime
from pathlib import Path
from typing import *


class EspacioDeTrabajo():
    def __init__(self, nombreEDT: AnyStr, fechaMod: datetime, direccion: Path, correoElectronico=None):
        self.nombreEDT = nombreEDT
        self.fechaModificacion: datetime = fechaMod
        self.direccion: Path = direccion
        self.correoElectronico: AnyStr = correoElectronico
