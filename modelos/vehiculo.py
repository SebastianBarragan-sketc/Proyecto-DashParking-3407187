class Vehiculo:

    def __init__(
        self,
        placa: str,
        tipoVehiculo: str,
        modelo: str,
        idConductor: int
    ):
        self.__placa = placa
        self.__tipoVehiculo = tipoVehiculo
        self.__modelo = modelo
        self.__idConductor = idConductor

    @property
    def placa(self):
        return self.__placa

    @property
    def tipoVehiculo(self):
        return self.__tipoVehiculo

    @property
    def modelo(self):
        return self.__modelo

    @property
    def idConductor(self):
        return self.__idConductor
