import sqlite3


def init_db():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT
        )
    """)
    connection.commit()
    connection.close()


if __name__ == "__main__":
    init_db()
