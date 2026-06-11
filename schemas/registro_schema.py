from datetime import date
from datetime import time

from pydantic import BaseModel


class RegistroCreate(BaseModel):
    fecha: date
    horaEntrada: time
    horaSalida: time
    placaVehiculo: str
    idEspacio: int
    idTarifa: int
