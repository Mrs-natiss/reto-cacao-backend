from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app import crud, schemas
from app.models import crear_tabla
from typing import List

app = FastAPI(title="Sistema de Precios de Cacao")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    crear_tabla()

@app.get("/")
def root():
    return {"mensaje": "API de precios de cacao funcionando"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/precios", response_model=List[schemas.PrecioResponse])
def listar_precios():
    precios = crud.get_all_precios()
    return [{"id": p[0], "precio": p[1], "unidad": p[2], "fecha": p[3], "creado_en": p[4]} for p in precios]

@app.get("/precios/ultimo", response_model=schemas.PrecioResponse)
def ultimo_precio():
    precio = crud.get_ultimo_precio()
    if not precio:
        raise HTTPException(status_code=404, detail="No hay precios registrados")
    return {"id": precio[0], "precio": precio[1], "unidad": precio[2], "fecha": precio[3], "creado_en": precio[4]}

@app.post("/precios", response_model=schemas.PrecioResponse)
def crear_precio(datos: schemas.PrecioCreate):
    nuevo = crud.create_precio(datos.precio, datos.unidad, datos.fecha)
    return {"id": nuevo[0], "precio": nuevo[1], "unidad": nuevo[2], "fecha": nuevo[3], "creado_en": nuevo[4]}

@app.put("/precios/{id}", response_model=schemas.PrecioResponse)
def actualizar_precio(id: int, datos: schemas.PrecioCreate):
    actualizado = crud.update_precio(id, datos.precio, datos.unidad, datos.fecha)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    return {"id": actualizado[0], "precio": actualizado[1], "unidad": actualizado[2], "fecha": actualizado[3], "creado_en": actualizado[4]}

@app.delete("/precios/{id}")
def eliminar_precio(id: int):
    crud.delete_precio(id)
    return {"mensaje": "Precio eliminado correctamente"}