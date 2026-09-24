import sqlite3
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
