from pydantic import BaseModel
from datetime import date

class PrecioBase(BaseModel):
    precio: float
    unidad: str
    fecha: date

class PrecioCreate(PrecioBase):
    pass

class PrecioResponse(PrecioBase):
    id: int
    
    class Config:
        from_attributes = True