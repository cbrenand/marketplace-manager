import os
import requests
from dotenv import load_dotenv

ACCESS_TOKEN = 'seu_token'
URL_BASE = 'https://api.mercadolibre.com'

def publicar_anuncio(product_data):
    endpoint = f'{URL_BASE}/items'
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.post(endpoint, json=product_data, headers=headers)
    if response.status_code == 201:
        print("Anúncio publicado com sucesso!")
        return response.json()
    else:
        print("Erro ao publicar anúncio:", response.status_code, response.text)
        return None
    import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

def obter_token_acesso(codigo_autorizacao):
    endpoint = "https://api.mercadolibre.com/oauth/token"
    dados = {
        'grant_type': 'authorization_code',
        'client_id': os.getenv('MERCADO_LIVRE_CLIENT_ID'),
        'client_secret': os.getenv('MERCADO_LIVRE_CLIENT_SECRET'),
        'code': codigo_autorizacao,
        'redirect_uri': os.getenv('MERCADO_LIVRE_REDIRECT_URI')
    }
    response = requests.post(endpoint, data=dados)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao obter token de acesso:", response.status_code, response.text)
        return None

# Exemplo de uso
if __name__ == "__main__":
    codigo_autorizacao = "TG-67d47de5c7a4760001ce0af1-81747013"  # Substitua pelo código recebido
    token_info = obter_token_acesso(codigo_autorizacao)
    if token_info:
        print("Token de acesso:", token_info['access_token'])