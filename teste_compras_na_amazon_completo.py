import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
#import bdAmazonCompleto


driver = selenium.webdriver.Firefox(executable_path=r"C:\Users\T1091565\geckodriver.exe")

driver.get("https://www.amazon.com.br/")

driver.implicitly_wait(3)

driver.maximize_window()

sleep(2)

driver.find_element(By.CSS_SELECTOR, "#nav-xshop > a:nth-child(3)").click()

sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[1]/div/a").click()

#/html/body/div[1]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div[1]

links = []

for produto in driver.find_elements(By.CLASS_NAME, "zg-grid-general-faceout"):
        linkAtual = produto.find_element(By.TAG_NAME, "a")
        links.append(linkAtual.get_attribute("href"))

sleep(2)

for linkAtual in links:
    driver.get(linkAtual)
    driver.implicitly_wait(3)
    nome_do_produto = driver.find_element(By.ID, "productTitle").text
    try:
        valor = driver.find_element(By.CSS_SELECTOR, "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay").text
    except:
        valor = "Não encontrado"
    try:
        marca = driver.find_element(By.CSS_SELECTOR, "tr.a-spacing-small:nth-child(1) > td:nth-child(2) > span:nth-child(1)").text
    except:
        marca = driver.find_element(By.CSS_SELECTOR, "#bylineInfo")
    try:
        material = driver.find_element(By.CSS_SELECTOR, "tr.a-spacing-small:nth-child(3) > td:nth-child(2) > span:nth-child(1)").text
    except:
        marca = "Não especificado"
"""
    C = bdAmazonCompleto.Amazon()
    C.Produto = nome_do_produto
    C.Valor = valor
    C.Marca = marca
    C.MaterialOuCor = material

    bdAmazonCompleto.session.add(C)
    bdAmazonCompleto.session.commit()

    driver.implicitly_wait(3)
"""
    #integrar com o BD