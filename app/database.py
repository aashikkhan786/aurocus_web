"""Database module using Python's built-in sqlite3."""

import sqlite3
from app.config import settings


def get_db_path() -> str:
    """Return the database path configured in settings."""
    return settings.DATABASE_URL


def get_db_connection() -> sqlite3.Connection:
    """Create and return a database connection with Row factory."""
    conn = sqlite3.connect(settings.DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn


def close_db(conn: sqlite3.Connection) -> None:
    """Close a database connection safely."""
    if conn:
        conn.close()


def init_db() -> None:
    """Initialize the database and create tables if they don't exist."""
    conn = get_db_connection()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS contact_inquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                business_email TEXT NOT NULL,
                company_name TEXT NOT NULL,
                country TEXT NOT NULL,
                service_interested TEXT NOT NULL,
                project_details TEXT NOT NULL,
                ip_address TEXT,
                user_agent TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
    finally:
        close_db(conn)
