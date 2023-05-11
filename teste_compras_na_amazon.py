import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
import bdAmazon


driver = selenium.webdriver.Chrome(executable_path=r"C:\Users\T1091565\chromedriver.exe")

driver.get("https://www.amazon.com.br/")

driver.implicitly_wait(3)

driver.maximize_window()

sleep(2)

driver.find_element(By.CSS_SELECTOR, "#nav-xshop > a:nth-child(3)").click()

sleep(2)

driver.find_element(By.CLASS_NAME, "a-link-normal").click()

#/html/body/div[1]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div[1]

links = []

for produto in driver.find_elements(By.CLASS_NAME, "zg-grid-general-faceout"):
        linkAtual = produto.find_element(By.TAG_NAME, "a")
        links.append(linkAtual.get_attribute("href"))

sleep(2)

for linkAtual in links:
    driver.get(linkAtual)
    driver.implicitly_wait(3)
    nome_do_produto = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[1]/div/h1/span").text
    valor = driver.find_element(By.CSS_SELECTOR, "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay").text

    C = bdAmazon.Amazon()
    C.titulo = nome_do_produto
    C.preco = valor
    print(nome_do_produto)
    print(valor)

    bdAmazon.session.add(C)
    bdAmazon.session.commit()

    driver.implicitly_wait(3)
'''
for produtoAtual in driver.find_elements(By.CLASS_NAME, "item_box"):
        link = produtoAtual.find_element(By.TAG_NAME, "a")
        listaLinks.append(link.get_attribute("href"))

        for linkAtual in listaLinks:
        driver.get(linkAtual)
        driver.implicitly_wait(3) # seconds
        nomeProduto = driver.find_element(By.CSS_SELECTOR, ".detail_name").text
        preco = driver.find_element(By.ID, "cur_price").find_element(By.TAG_NAME, "span").text
'''