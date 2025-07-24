# tests/test_routes.py
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"User Management System" in response.data

def test_get_all_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_login_success(client):
    payload = {
        "email": "john@example.com",
        "password": "password123"
    }
    response = client.post('/login', json=payload)
    assert response.status_code == 200
    assert response.json['status'] == 'success'

def test_login_failure(client):
    payload = {
        "email": "wrong@example.com",
        "password": "wrongpass"
    }
    response = client.post('/login', json=payload)
    assert response.status_code == 401
    assert response.json['status'] == 'failed'

def test_search_user(client):
    response = client.get('/search?name=John')
    assert response.status_code == 200
    assert any("John" in user['name'] for user in response.json)
