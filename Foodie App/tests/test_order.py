import requests

def test_place_order(base_url):
    payload = {
        "user_id": 1,
        "restaurant_id": 1
    }

    response = requests.post(f"{base_url}/api/v1/orders", json=payload)

    assert response.status_code == 201
