from pydantic import BaseModel


class ConductorCreate(BaseModel):
    nombre: str
    correo: str
    numeroLicencia: str
