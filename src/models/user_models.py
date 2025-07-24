# models.py
from werkzeug.security import generate_password_hash, check_password_hash

def fetch_all_users(cursor):
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def fetch_user_by_id(cursor, user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def insert_user(cursor, conn, name, email, password):
    try:
        hashed_password = generate_password_hash(password)
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_password))
        conn.commit()
        return True
    except:
        return False

def update_user_by_id(cursor, conn, user_id, name, email):
    try:
        cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
        conn.commit()
        return True
    except:
        return False

def delete_user_by_id(cursor, conn, user_id):
    try:
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        return True
    except:
        return False

def search_users_by_name(cursor, name):
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", (f"%{name}%",))
    return cursor.fetchall()

def verify_user_login(cursor, email, password):
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    if user and check_password_hash(user[3], password):  # assuming password is at index 3
        return user
    return None
