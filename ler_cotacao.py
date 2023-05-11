from time import sleep
from selenium import webdriver
import pandas as pd
import xlsxwriter
import selenium.webdriver
import bdCotacao


data_frame = pd.read_excel(r'C:\Users\T1091565\Selenium\Cotação.xlsx')
#C:\Users\T1091565\Selenium

driver = selenium.webdriver.Chrome(executable_path=r"C:\Users\T1091565\chromedriver.exe")

for index, row in data_frame.iterrows():
    data = (str(row['Data']))
    sleep(2)
    valor = (str(row['Valor']))

    C = bdCotacao.Amazon()
    C.Data = data
    C.Valor = valor

    bdCotacao.session.add(C)
    bdCotacao.session.commit()

    driver.implicitly_wait(3)