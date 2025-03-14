from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def publicar_anuncio_shopee(produto):
    # Configurações do Selenium
    driver = webdriver.Chrome()  # Ou o driver do seu navegador
    driver.get('https://seller.shopee.com.br')

    # Login na Shopee
    time.sleep(5)
    driver.find_element(By.NAME, 'username').send_keys('seu_usuario')
    driver.find_element(By.NAME, 'password').send_keys('sua_senha')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Navegar até a página de publicação de anúncios
    time.sleep(5)
    driver.get('https://seller.shopee.com.br/product/add')

    # Preencher formulário de anúncio
    driver.find_element(By.NAME, 'product_name').send_keys(produto['nome'])
    driver.find_element(By.NAME, 'price').send_keys(str(produto['preco']))
    driver.find_element(By.NAME, 'stock').send_keys(str(produto['estoque']))
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Fechar navegador
    time.sleep(5)
    driver.quit()

# Exemplo de uso
if __name__ == "__main__":
    produto = {
        'nome': 'Produto de Exemplo',
        'preco': 100,
        'estoque': 10
    }
    publicar_anuncio_shopee(produto)