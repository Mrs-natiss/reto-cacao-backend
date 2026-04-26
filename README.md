# Reto Cacao — Backend

API REST para el sistema de precios de cacao, construida con FastAPI y PostgreSQL.

## Endpoints

### GET /precios
Retorna todos los precios históricos.

**Response:**
```json
[
  {
    "id": 1,
    "precio": 3500.00,
    "unidad": "USD/ton",
    "fecha": "2026-04-23",
    "creado_en": "2026-04-23T20:33:14"
  }
]
```

### GET /precios/ultimo
Retorna el precio más reciente.

**Response:**
```json
{
  "id": 1,
  "precio": 3500.00,
  "unidad": "USD/ton",
  "fecha": "2026-04-23",
  "creado_en": "2026-04-23T20:33:14"
}
```

### POST /precios
Crea un nuevo precio.

**Payload:**
```json
{
  "precio": 3500.00,
  "unidad": "USD/ton",
  "fecha": "2026-04-23"
}
```

### PUT /precios/{id}
Actualiza un precio existente.

**Payload:**
```json
{
  "precio": 3600.00,
  "unidad": "USD/ton",
  "fecha": "2026-04-24"
}
```

### DELETE /precios/{id}
Elimina un precio.

**Response:**
```json
{
  "mensaje": "Precio eliminado correctamente"
}
```

## Correr localmente

```bash
uv venv
source .venv/bin/activate
uv run uvicorn app.main:app --reload
```