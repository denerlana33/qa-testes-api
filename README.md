# qa-testes-api

Testes de API usando Python, Pytest e [Reqres](https://reqres.in).

## 🚀 Como rodar os testes

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Executar os testes
```bash
pytest -v
```

### ✅ Resultado esperado
- test_list_users → deve retornar 200 e lista de usuários
- test_single_user → deve retornar 200 e usuário id=2
- test_user_not_found → deve retornar 404
