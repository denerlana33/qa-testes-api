# qa-testes-api

Testes de API usando Python, Pytest e [Reqres](https://reqres.in).

---

## 🚀 Objetivo

Automatizar testes de API REST simulando requisições reais contra o serviço público Reqres.

---

## 🧪 Testes implementados

- `GET /users?page=2` → deve retornar status **200** e uma lista de usuários.
- `GET /users/2` → deve retornar status **200** e usuário com ID 2.
- `GET /users/23` → deve retornar status **404** (usuário não encontrado).

---

## 🛠 Como rodar os testes

### 1. Instalar dependências
```bash
pip install -r requirements.txt
