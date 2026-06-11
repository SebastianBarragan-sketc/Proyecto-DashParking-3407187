class Tarifa:

    def __init__(
        self,
        idTarifa: int,
        tipoVehiculo: str,
        valorMinuto: float
    ):
        self.__idTarifa = idTarifa
        self.__tipoVehiculo = tipoVehiculo
        self.__valorMinuto = valorMinuto

    @property
    def idTarifa(self):
        return self.__idTarifa

    @property
    def tipoVehiculo(self):
        return self.__tipoVehiculo

    @property
    def valorMinuto(self):
        return self.__valorMinuto
