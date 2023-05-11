import xlsxwriter
import pandas as pd
import bdCSV
import csv

data_frame = pd.read_csv(r'C:\Users\T1091565\Selenium\myFile0.csv')

for index, row in data_frame.iterrows():
    nome = (str(row['firstname']))
    sobrenome = (str(row['lastname']))
    primeiro_email = (str(row['email']))
    segundo_email = (str(row['email2']))
    profissao = (str(row['profession']))

    C = bdCSV.CSV()
    C.Nome = nome
    C.Sobrenome = sobrenome
    C.Email = primeiro_email
    C.Email2 = segundo_email
    C.Profissao = profissao

    bdCSV.session.add(C)
    bdCSV.session.commit()
'''
    print(C.Nome)
    print(C.Sobrenome)
    print(C.Email)
    print(C.Email2)
    print(C.Profissao)
'''
'''
    
    C = bdCotacao.Amazon()
    C.Data = data
    C.Valor = valor

    bdCotacao.session.add(C)
    bdCotacao.session.commit()

    driver.implicitly_wait(3)
    '''