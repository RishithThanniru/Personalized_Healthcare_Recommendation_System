import sqlite3
import hashlib


def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def create_users_table():

    conn = sqlite3.connect(
        "healthcare.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    conn.commit()
    conn.close()


def register_user(username, password):

    conn = sqlite3.connect(
        "healthcare.db"
    )

    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users
            (username, password)
            VALUES (?, ?)
            """,
            (
                username,
                hash_password(password)
            )
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def login_user(username, password):

    conn = sqlite3.connect(
        "healthcare.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        AND password=?
        """,
        (
            username,
            hash_password(password)
        )
    )

    user = cursor.fetchone()

    conn.close()

    return user


create_users_table()