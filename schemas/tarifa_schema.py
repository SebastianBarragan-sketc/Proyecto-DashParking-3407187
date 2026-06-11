from pydantic import BaseModel


class TarifaCreate(BaseModel):
    tipoVehiculo: str
    valorMinuto: float
