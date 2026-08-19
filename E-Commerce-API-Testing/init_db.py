import sqlite3


def initialize_database():
    connection = sqlite3.connect("ecommerce.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    )
    """)
    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES(?, ?)",
            ("samir", "secure123")
        )
        connection.commit()
        print("Database intialized and user 'samir' created successfully! ")
    except sqlite3.IntegrityError:
        print("Database already exists. skipping user insertion")
    connection.close()


if __name__ == '__main__':
    initialize_database()
