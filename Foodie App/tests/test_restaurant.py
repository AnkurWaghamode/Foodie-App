import requests
import random

def test_create_restaurant(base_url):
    payload = {
        "name": f"Test Hotel {random.randint(1,10000)}",
        "category": "Indian",
        "location": "Hyderabad",
        "contact": "9999999999"
    }

    response = requests.post(f"{base_url}/api/v1/restaurants", json=payload)

    assert response.status_code == 201
