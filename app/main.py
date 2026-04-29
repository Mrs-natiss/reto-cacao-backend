from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.precio import crear_tabla
from app.routers import precios

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

app.include_router(precios.router)