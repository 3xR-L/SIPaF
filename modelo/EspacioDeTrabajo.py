# Create a base class for the workspace

# Import the module to specify the types of the variables and the return
import time
from pathlib import Path
from typing import *
from dataclasses import dataclass

class EspacioDeTrabajo():
    def __init__(self, nombreEDT:AnyStr, fechaMod:time, direccion: Path, correoElectronico=None):
        self.nombreEDT = nombreEDT
        self.fechaModificacion:time = fechaMod
        self.direccion: Path = direccion
        self.correoElectronico: AnyStr = correoElectronico
