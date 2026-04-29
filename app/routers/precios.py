from fastapi import APIRouter, HTTPException
from app.schemas.precio import PrecioCreate, PrecioResponse
from app.crud import precio as crud
from typing import List

router = APIRouter(prefix="/precios", tags=["precios"])

@router.get("", response_model=List[PrecioResponse])
def listar_precios():
    precios = crud.get_all_precios()
    return [{"id": p[0], "precio": p[1], "unidad": p[2], "fecha": p[3], "creado_en": p[4], "fuente": p[5], "region": p[6]} for p in precios]

@router.get("/ultimo", response_model=PrecioResponse)
def ultimo_precio():
    precio = crud.get_ultimo_precio()
    if not precio:
        raise HTTPException(status_code=404, detail="No hay precios registrados")
    return {"id": precio[0], "precio": precio[1], "unidad": precio[2], "fecha": precio[3], "creado_en": precio[4], "fuente": precio[5], "region": precio[6]}

@router.post("", response_model=PrecioResponse)
def crear_precio(datos: PrecioCreate):
    nuevo = crud.create_precio(datos.precio, datos.unidad, datos.fecha, datos.fuente, datos.region)
    return {"id": nuevo[0], "precio": nuevo[1], "unidad": nuevo[2], "fecha": nuevo[3], "creado_en": nuevo[4], "fuente": nuevo[5], "region": nuevo[6]}

@router.put("/{id}", response_model=PrecioResponse)
def actualizar_precio(id: int, datos: PrecioCreate):
    actualizado = crud.update_precio(id, datos.precio, datos.unidad, datos.fecha, datos.fuente, datos.region)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    return {"id": actualizado[0], "precio": actualizado[1], "unidad": actualizado[2], "fecha": actualizado[3], "creado_en": actualizado[4], "fuente": actualizado[5], "region": actualizado[6]}

@router.delete("/{id}")
def eliminar_precio(id: int):
    crud.delete_precio(id)
    return {"mensaje": "Precio eliminado correctamente"}