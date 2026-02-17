import requests

def test_create_user(base_url):
    payload = {
        "name": "Test User",
        "email": "testuser@gmail.com",
        "password": "1234"
    }

    response = requests.post(f"{base_url}/api/v1/users/register", json=payload)

    assert response.status_code == 201
