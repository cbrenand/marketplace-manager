import os

# Estrutura de pastas e arquivos
estrutura = {
    "marketplace-manager": {
        "backend": {
            "api": {
                "tiny.py": "",
                "mercado_livre.py": "",
                "shopee.py": "",
            },
            "models": {},
            "utils": {},
            "main.py": "",
        },
        "frontend": {
            "public": {},
            "src": {
                "components": {},
                "pages": {},
                "services": {},
                "App.js": "",
            },
            "package.json": "",
        },
        "scripts": {},
        "database": {},
        ".gitignore": "",
        "README.md": "",
        "requirements.txt": "",
    }
}

# Função para criar a estrutura
def criar_estrutura(base_path, estrutura):
    for nome, conteudo in estrutura.items():
        caminho = os.path.join(base_path, nome)
        if isinstance(conteudo, dict):
            # Se for um dicionário, é uma pasta
            os.makedirs(caminho, exist_ok=True)
            criar_estrutura(caminho, conteudo)
        else:
            # Se não for um dicionário, é um arquivo
            with open(caminho, "w", encoding="utf-8") as arquivo:
                if conteudo:
                    arquivo.write(conteudo)

# Caminho onde a estrutura será criada (pode ser alterado)
caminho_base = os.path.join(os.getcwd(), "marketplace-manager")

# Criar a estrutura
criar_estrutura(caminho_base, estrutura)

print(f"Estrutura criada com sucesso em: {caminho_base}")