import pyodbc 
import pandas as pd
import numpy as np

server = 'JORGE'
database = 'BDBrasil_IFSP'
username = 'teste'
password = 'teste'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
#cursor.execute("SELECT NomeCidade as cidade FROM TBCidade")
# row = cursor.fetchone()

# while row:
#    print (row)
#    row = cursor.fetchone()


print("**************************")
print("******* Bem vindo! *******")
print("**************************")

nome = input("Nome Completo: ")
CPF = input("CPF: ")
endereco = input("Endereço: ")

cursor.execute(f"""
        
        INSERT INTO CLITESTE VALUES('{nome}','{CPF}','{endereco}')

""")
cnxn.commit()
