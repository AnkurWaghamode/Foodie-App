import pytest

BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture
def base_url():
    return BASE_URL
