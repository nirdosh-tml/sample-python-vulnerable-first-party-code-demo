import sqlite3
from typing import Optional, Tuple

def create_db():
    """Create the users table if it doesn't exist."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT UNIQUE, age INTEGER)")
    conn.commit()
    conn.close()

def add_user(name: str, age: int) -> None:
    """Add a new user to the database."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"User with name '{name}' already exists.")
    finally:
        conn.close()

def get_user_by_id(user_id: int) -> Optional[Tuple[int, str, int]]:
    """Get a user by their ID."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT id, name, age FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user

def get_db_connection():
    """Get a connection to the database."""
    return sqlite3.connect("users.db")