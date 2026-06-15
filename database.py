import sqlite3


def create_database():

    conn = sqlite3.connect(
        "healthcare.db"
    )

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS prediction_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            date TEXT,

            symptoms TEXT,

            disease TEXT,

            confidence REAL,

            risk_level TEXT

        )

    """)

    conn.commit()
    conn.close()


def insert_prediction(
    username,
    date,
    symptoms,
    disease,
    confidence,
    risk_level
):

    conn = sqlite3.connect(
        "healthcare.db"
    )

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO prediction_history

        (
            username,
            date,
            symptoms,
            disease,
            confidence,
            risk_level
        )

        VALUES (?, ?, ?, ?, ?, ?)

    """,

    (
        username,
        date,
        symptoms,
        disease,
        confidence,
        risk_level
    ))

    conn.commit()
    conn.close()


def get_history(username):

    conn = sqlite3.connect(
        "healthcare.db"
    )

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM prediction_history

        WHERE username=?

        ORDER BY id DESC

    """,

    (username,))

    history = cursor.fetchall()

    conn.close()

    return history


create_database()