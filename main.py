from fastapi import FastAPI, HTTPException
import time
from random import randint

app = FastAPI()

fake_users = {
    1: {"name": "João", "email": "joao@example.com"},
    2: {"name": "Maria", "email": "maria@example.com"}
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = fake_users.get(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Not Found")

@app.get("/simulate-error")
def simulate_error():
    raise HTTPException(status_code=500, detail="Erro Interno Simulado")

@app.get("/delay")
def delayed_response():
    time.sleep(randint(1, 3))  # atraso aleatório entre 1 e 3 segundos
    return {"message": "Demorou mas chegou"}
