from app.database import get_connection

def get_all_precios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM precio_cacao ORDER BY fecha DESC")
    precios = cursor.fetchall()
    cursor.close()
    conn.close()
    return precios

def get_ultimo_precio():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM precio_cacao ORDER BY fecha DESC LIMIT 1")
    precio = cursor.fetchone()
    cursor.close()
    conn.close()
    return precio

def create_precio(precio, unidad, fecha, fuente=None, region=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO precio_cacao (precio, unidad, fecha, fuente, region) VALUES (%s, %s, %s, %s, %s) RETURNING *",
        (precio, unidad, fecha, fuente, region)
    )
    nuevo = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return nuevo

def update_precio(id, precio, unidad, fecha, fuente=None, region=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE precio_cacao SET precio=%s, unidad=%s, fecha=%s, fuente=%s, region=%s WHERE id=%s RETURNING *",
        (precio, unidad, fecha, fuente, region, id)
    )
    actualizado = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return actualizado

def delete_precio(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM precio_cacao WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()