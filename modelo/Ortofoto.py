from modelo.TIPO_ESPECTRO import TIPO_ESPECTRO

class Ortofoto:
    """ Clase que representa una ortofoto
    <ORTOFOTO>
        <TamanoOrtofoto>[ancho (cantidad de imagenes), alto (cantidad de imagenes)</TamanoOrtofoto>
        <CantidadImagenes>cantidad de imagenes totales</CantidadImagenes>
        <Ortofofoto>lista de imagenes</Ortofofoto>
        <TipoEspectro>RGB</TipoEspectro>
    """
    def __init__(self, tamanoOrtofoto: list, Ortofoto: list, tipo: TIPO_ESPECTRO):
        self.tamanoOrtofoto = tamanoOrtofoto
        self._cantidadIma = None
        self.Ortofoto = Ortofoto
        self.tipo = tipo
