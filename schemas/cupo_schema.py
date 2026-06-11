from pydantic import BaseModel


class CupoCreate(BaseModel):
    piso: int
    estado: str
