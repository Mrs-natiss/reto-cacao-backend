from app.database import get_connection

def crear_tabla():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS precio_cacao (
            id SERIAL PRIMARY KEY,
            precio NUMERIC(10, 2) NOT NULL,
            unidad VARCHAR(20) NOT NULL,
            fecha DATE NOT NULL,
            creado_en TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()