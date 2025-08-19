import requests

def test_list_users(base_url):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200
    assert "data" in response.json()

def test_single_user(base_url):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

#def test_user_not_found(base_url):
    #response = requests.get(f"{base_url}/users/23")
   # print(response.status_code)
 #   print(response.text)
   # assert response.status_code == 404

