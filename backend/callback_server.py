from flask import Flask, request
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

app = Flask(__name__)

@app.route('/ml/callback')
def mercado_livre_callback():
    # Receber o código de autorização
    codigo_autorizacao = request.args.get('code')
    if codigo_autorizacao:
        print(f"Código de autorização recebido: {codigo_autorizacao}")
        # Aqui você pode chamar a função para obter o token de acesso
        return "Código de autorização recebido com sucesso!"
    else:
        return "Erro: Código de autorização não recebido.", 400

if __name__ == "__main__":
    app.run(port=5000, debug=True)
from flask import Flask, request
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

app = Flask(__name__)

@app.route('/auth')
def auth_callback():
    # Capturar o código de autorização
    codigo_autorizacao = request.args.get('code')
    if codigo_autorizacao:
        print(f"Código de autorização recebido: {codigo_autorizacao}")
        # Aqui você pode chamar a função para obter o token de acesso
        return "Código de autorização recebido com sucesso!"
    else:
        return "Erro: Código de autorização não recebido.", 400

if __name__ == "__main__":
    app.run(port=5000)
    