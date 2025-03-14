import requests

API_KEY = 'sua_chave_api'
URL_BASE = 'https://api.tiny.com.br/api/v3'

def buscar_produtos(offset=0, limit=100):
    endpoint = f'{URL_BASE}/produtos'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    params = {
        'offset': offset,
        'limit': limit
    }
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['produtos']
    else:
        print("Erro ao buscar produtos:", response.status_code, response.text)
        return None
    import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

def gerar_url_autorizacao():
    client_id = os.getenv('TINY_API_KEY')
    redirect_uri = os.getenv('TINY_REDIRECT_URI')
    url_autorizacao = (
        f"https://api.tiny.com.br/oauth/authorize?"
        f"response_type=code&"
        f"client_id={client_id}&"
        f"redirect_uri={redirect_uri}"
    )
    return url_autorizacao

# Exemplo de uso
if __name__ == "__main__":
    print("URL de Autorização:", gerar_url_autorizacao())
    
import requests

def obter_token_acesso(codigo_autorizacao):
    endpoint = "https://api.tiny.com.br/oauth/access_token"
    dados = {
        'grant_type': 'authorization_code',
        'client_id': os.getenv('TINY_API_KEY'),
        'client_secret': os.getenv('TINY_CLIENT_SECRET'),
        'code': codigo_autorizacao,
        'redirect_uri': os.getenv('TINY_REDIRECT_URI')
    }
    response = requests.post(endpoint, data=dados)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao obter token de acesso:", response.status_code, response.text)
        return None