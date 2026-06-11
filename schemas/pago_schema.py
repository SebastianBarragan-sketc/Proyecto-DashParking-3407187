from pydantic import BaseModel


class PagoCreate(BaseModel):
    monto: float
    metodoPago: str
    estadoPago: str
