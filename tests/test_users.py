import pytest
import requests

headers = {
    "x-api-key": "reqres-free-v1"
}

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

def test_list_users(base_url):
    response = requests.get(f"{base_url}/users?page=2", headers=headers)
    print("LIST USERS STATUS:", response.status_code)
    print("BODY:", response.text)
    assert response.status_code == 200
    assert "data" in response.json()

def test_single_user(base_url):
    response = requests.get(f"{base_url}/users/2", headers=headers)
    print("SINGLE USER STATUS:", response.status_code)
    print("BODY:", response.text)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def test_create_user(base_url):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    print("CREATE USER STATUS:", response.status_code)
    print("BODY:", response.text)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "morpheus"
    assert data["job"] == "leader"
    assert "id" in data
    assert "createdAt" in data
