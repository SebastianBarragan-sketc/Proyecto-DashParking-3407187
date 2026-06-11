class Pago:

    def __init__(
        self,
        idPago: int,
        monto: float,
        metodoPago: str,
        estadoPago: str,
        codigoQR: str
    ):
        self.__idPago = idPago
        self.__monto = monto
        self.__metodoPago = metodoPago
        self.__estadoPago = estadoPago
        self.__codigoQR = codigoQR

    @property
    def idPago(self):
        return self.__idPago

    @property
    def monto(self):
        return self.__monto

    @property
    def metodoPago(self):
        return self.__metodoPago

    @property
    def estadoPago(self):
        return self.__estadoPago

    @property
    def codigoQR(self):
        return self.__codigoQR
