# tests/test_models.py
import pytest
from models.user_models import insert_user, fetch_user_by_id, delete_user_by_id


def test_insert_and_fetch_user(cursor, conn):
    cursor.execute("DELETE FROM users")  # optional: clean state
    conn.commit()
    
    insert_user(cursor, conn, 'Test User', 'test@example.com', 'testpass')
    user_id = cursor.lastrowid
    user = fetch_user_by_id(cursor, user_id)
    
    assert user is not None
    assert user['name'] == 'Test User'


def test_delete_user(cursor, conn):
    insert_user(cursor, conn, 'Delete Me', 'del@example.com', 'pass')
    user = fetch_user_by_id(cursor, 2)
    assert user is not None
    assert delete_user_by_id(cursor, conn, 2) is True
