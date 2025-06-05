# database/db_manager.py
import sqlite3

def get_connection():
    return sqlite3.connect("store.db")

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                categoria TEXT,
                stock INTEGER,
                precio REAL
            )
        """)
        conn.commit()
