from pydantic import BaseModel


class VehiculoCreate(BaseModel):
    placa: str
    tipoVehiculo: str
    modelo: str
    idConductor: int
