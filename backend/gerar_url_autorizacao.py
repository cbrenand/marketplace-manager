import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

def gerar_url_autorizacao():
    client_id = os.getenv('MERCADO_LIVRE_CLIENT_ID')
    redirect_uri = os.getenv('MERCADO_LIVRE_REDIRECT_URI')
    url_autorizacao = (
        f"https://auth.mercadolivre.com.br/authorization?"
        f"response_type=code&"
        f"client_id={client_id}&"
        f"redirect_uri={redirect_uri}"
    )
    return url_autorizacao

# Exemplo de uso
if __name__ == "__main__":
    print("URL de Autorização:", gerar_url_autorizacao())