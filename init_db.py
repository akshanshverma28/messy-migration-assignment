import sqlite3
from werkzeug.security import generate_password_hash

# Connect to database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert hashed sample users
users = [
    ('John Doe', 'john@example.com', generate_password_hash('password123')),
    ('Jane Smith', 'jane@example.com', generate_password_hash('secret456')),
    ('Bob Johnson', 'bob@example.com', generate_password_hash('qwerty789')),
]

cursor.executemany("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", users)

# Commit and close
conn.commit()
conn.close()

print("Database initialized with hashed sample data")
