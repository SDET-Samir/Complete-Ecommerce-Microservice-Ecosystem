import sqlite3
import pytest


def test_database_user_exists():
    """
    Directly inspect the SQL database layer to verify that the 
    seed user account 'samir' exists and has the correct credentials.
    """
    connection = sqlite3.connect("ecommerce.db")
    cursor = connection.cursor()

    cursor.execute("SELECT password FROM users WHERE username==?", ("samir",))
    record = cursor.fetchone()
    connection.close()

    assert record is not None, "Error: User 'samir' was not found in the database tables!"
    assert record[0] == "secure123", f"Error: password mismatch! Found {record[0]} "
