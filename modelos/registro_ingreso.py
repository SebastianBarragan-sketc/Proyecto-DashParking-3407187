from datetime import date
from datetime import time


class RegistroIngreso:

    def __init__(
        self,
        idRegistro: int,
        fecha: date,
        horaEntrada: time,
        horaSalida: time,
        valorCalculado: float,
        placaVehiculo: str,
        idEspacio: int,
        idTarifa: int
    ):
        self.__idRegistro = idRegistro
        self.__fecha = fecha
        self.__horaEntrada = horaEntrada
        self.__horaSalida = horaSalida
        self.__valorCalculado = valorCalculado
        self.__placaVehiculo = placaVehiculo
        self.__idEspacio = idEspacio
        self.__idTarifa = idTarifa

    @property
    def idRegistro(self):
        return self.__idRegistro

    @property
    def fecha(self):
        return self.__fecha

    @property
    def horaEntrada(self):
        return self.__horaEntrada

    @property
    def horaSalida(self):
        return self.__horaSalida

    @property
    def valorCalculado(self):
        return self.__valorCalculado

    @property
    def placaVehiculo(self):
        return self.__placaVehiculo

    @property
    def idEspacio(self):
        return self.__idEspacio

    @property
    def idTarifa(self):
        return self.__idTarifa
