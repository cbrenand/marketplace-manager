from api.tiny import buscar_produtos

if __name__ == "__main__":
    produtos = buscar_produtos()
    if produtos:
        print(f"Total de produtos: {len(produtos)}")
        for produto in produtos[:5]:  # Exibe os 5 primeiros produtos
            print(produto['nome'], produto['preco'])
            
from api.mercado_livre import publicar_anuncio

if __name__ == "__main__":
    product_data = {
        'title': 'Produto de Exemplo',
        'price': 100,
        'available_quantity': 10,
        'description': 'Descrição do produto',
        'category_id': 'MLB1234'  # ID da categoria no Mercado Livre
    }
    publicar_anuncio(product_data)