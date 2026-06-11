from abc import ABC, abstractmethod


class Usuario(ABC):

    def __init__(self, idUsuario: int, nombre: str, correo: str):
        self.__idUsuario = idUsuario
        self.__nombre = nombre
        self.__correo = correo

    @property
    def idUsuario(self):
        return self.__idUsuario

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        self.__correo = valor

    @abstractmethod
    def mostrarInformacion(self):
        pass
