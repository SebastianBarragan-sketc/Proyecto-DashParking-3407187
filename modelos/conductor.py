from modelos.usuario import Usuario


class Conductor(Usuario):

    def __init__(
        self,
        idUsuario: int,
        nombre: str,
        correo: str,
        numeroLicencia: str
    ):
        super().__init__(idUsuario, nombre, correo)
        self.__numeroLicencia = numeroLicencia

    @property
    def numeroLicencia(self):
        return self.__numeroLicencia

    @numeroLicencia.setter
    def numeroLicencia(self, valor):
        self.__numeroLicencia = valor

    def mostrarInformacion(self):
        return {
            "id": self.idUsuario,
            "nombre": self.nombre,
            "correo": self.correo,
            "licencia": self.numeroLicencia
        }
