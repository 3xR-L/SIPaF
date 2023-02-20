from modelo.Ortofoto import Ortofoto

class COrtofoto:
    def __init__(self, dirEDT, ortofoto = None):
        self.dirIma = dirEDT+ '/Imagenes'
        self.dirEDT = dirEDT
        self.ortofoto = ortofoto

    def preprocesarFotos(self, dir_imagenes_originales, camara_visual= None, camara_infrarroja = None):
        pass