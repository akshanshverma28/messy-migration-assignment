# tests/test_controllers.py
def test_create_user_with_missing_fields(client):
    response = client.post('/users', json={"name": "Incomplete"})
    assert response.status_code == 400
    assert b"Invalid data" in response.data

def test_update_user_invalid(client):
    response = client.put('/user/1', json={})
    assert response.status_code == 400

def test_delete_nonexistent_user(client):
    response = client.delete('/user/9999')
    assert response.status_code == 500  # Since we return server error on failure
