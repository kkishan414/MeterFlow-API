import sqlite3
from collections.abc import Generator
from app.core.config import settings 

def get_connection()-> Generator[sqlite3.Connection, None, None]:
    conn = sqlite3.connect(settings.DB_PATH)
    conn.row_factory = sqlite3.Row 
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        yield conn 
        conn.commit()
    except Exception:
        conn.rollback()
    finally:
        conn.close()

def init_db() -> None:
    gen = get_connection()
    conn = next(gen) 
    try: 
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS organizations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            plan TEXT NOT NULL DEFAULT 'FREE',
            credits_balance INTEGER NOT NULL DEFAULT 100,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password hash TEXT NOT NULL,
            organization_id INTEGER NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (organization_id) REFERENCES organizations(id)
            );
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS usage_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            organizantion_id INTEGER NOT NULL,
            feature_name TEXT NOT NULL,
            credits_used INTERGER NOT NULL,
            idempotency_key TEXT NOT NULL UNIQUE,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (organization_id) REFERENCES organizations(id)
            );
            """

        )
        conn.commit()
    except Exception:
        conn.rollback()
    finally:
        conn.close()


