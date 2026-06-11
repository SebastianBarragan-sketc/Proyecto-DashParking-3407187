class Cupo:

    def __init__(
        self,
        idEspacio: int,
        piso: int,
        estado: str
    ):
        self.__idEspacio = idEspacio
        self.__piso = piso
        self.__estado = estado

    @property
    def idEspacio(self):
        return self.__idEspacio

    @property
    def piso(self):
        return self.__piso

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor
