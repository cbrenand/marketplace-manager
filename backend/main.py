from api.tiny import buscar_produtos

if __name__ == "__main__":
    produtos = buscar_produtos()
    print(f"Total de produtos: {len(produtos)}")