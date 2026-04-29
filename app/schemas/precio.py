from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class PrecioBase(BaseModel):
    precio: float
    unidad: str
    fecha: date
    fuente: Optional[str] = None
    region: Optional[str] = None

class PrecioCreate(PrecioBase):
    pass

class PrecioResponse(PrecioBase):
    id: int
    creado_en: Optional[datetime] = None

    class Config:
        from_attributes = True