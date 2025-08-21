import requests

def test_response_body():
    url = "http://127.0.0.1:8000/users/1"
    response = requests.get(url)
    data = response.json()
    assert "name" in data
    assert "email" in data
    assert data["name"] == "João"

def test_internal_server_error():
    url = "http://127.0.0.1:8000/simulate-error"
    response = requests.get(url)
    assert response.status_code == 500
    assert response.json()["detail"] == "Erro Interno Simulado"

def test_response_time():
    url = "http://127.0.0.1:8000/delay"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 3  # pode ajustar se quiser limitar mais
