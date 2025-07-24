# tests/conftest.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import pytest
import sqlite3
from src.app import app as flask_app  # ✅ Import your Flask app from src

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True
    })
    return flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    yield connection
    connection.close()

@pytest.fixture
def cursor(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Optional: seed test data
    cursor.execute("INSERT INTO users (name, email, password) VALUES ('John Doe', 'john@example.com', 'password123')")
    conn.commit()
    return cursor
