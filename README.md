# Reto Cacao — Backend

API REST para el sistema de precios de cacao, construida con FastAPI y PostgreSQL.

## URL en producción

- **API:** https://reto-cacao-backend-production.up.railway.app
- **Documentación:** https://reto-cacao-backend-production.up.railway.app/docs
- **Health check:** https://reto-cacao-backend-production.up.railway.app/health

## Stack

- **FastAPI** — framework web
- **PostgreSQL** — base de datos
- **psycopg2** — conector de base de datos
- **uv** — gestor de paquetes y entornos virtuales
- **Docker** — contenedorización

## Correr localmente con uv

```bash
uv venv
source .venv/bin/activate
uv run uvicorn app.main:app --reload
```

## Correr localmente con Docker

```bash
docker build -t reto-cacao-backend .
docker run -p 8000:8000 --env-file .env reto-cacao-backend
```

## Variables de entorno

Crea un archivo `.env` basado en `.env.example`:

DB_HOST=localhost
DB_NAME=cacao_db
DB_USER=tu_usuario
DB_PASSWORD=tu_password
DB_PORT=5432

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | /health | Health check |
| GET | /precios | Retorna todos los precios |
| GET | /precios/ultimo | Retorna el precio más reciente |
| POST | /precios | Crea un nuevo precio |
| PUT | /precios/{id} | Actualiza un precio |
| DELETE | /precios/{id} | Elimina un precio |

## Modelo de datos

```sql
CREATE TABLE precio_cacao (
    id SERIAL PRIMARY KEY,
    precio NUMERIC(10, 2) NOT NULL,
    unidad VARCHAR(20) NOT NULL,
    fecha DATE NOT NULL,
    creado_en TIMESTAMP DEFAULT NOW()
);
```

## Decisiones técnicas

- Se usó **psycopg2** directamente para las consultas SQL en vez de SQLAlchemy, ya que el proyecto es simple y no requiere un ORM completo.
- La base de datos y el backend se desplegaron en el **mismo proyecto de Railway** para comunicarse usando el host interno.