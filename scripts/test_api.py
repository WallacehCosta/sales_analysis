import requests

# URL base da API
BASE_URL = "http://localhost:8000/api"

# Função para testar o endpoint de login
def test_login():
    url = f"{BASE_URL}/auth/login"
    payload = {"email": "user@example.com", "password": "password123"}
    response = requests.post(url, json=payload)
    print("Teste de login:", response.status_code, response.json())

# Função para testar o endpoint de vendas
def test_sales():
    url = f"{BASE_URL}/sales"
    response = requests.get(url)
    print("Teste de vendas:", response.status_code, response.json())

# Função para testar o endpoint de relatórios
def test_reports():
    url = f"{BASE_URL}/reports"
    response = requests.get(url)
    print("Teste de relatórios:", response.status_code, response.json())

if __name__ == "__main__":
    test_login()
    test_sales()
    test_reports()
    