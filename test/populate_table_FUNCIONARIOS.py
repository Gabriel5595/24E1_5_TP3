import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_csv_file import read_csv_file
from components.create_table_FUNCIONARIOS import create_table_FUNCIONARIOS

def populate_table_FUNCIONARIOS(file_information):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    
    cursor.executemany("""
INSERT INTO FUNCIONARIOS (NOME_FUNCIONARIO,
                            CARGO_ID,
                            DEPARTAMENTO_ID,
                            DEPENDENTES_ID,
                            SALARIO_REAL,
                            TIPO_CONTRATO) VALUES
                            
                            (:NOME_FUNCIONARIO,
                            :CARGO_ID,
                            :DEPARTAMENTO_ID,
                            :DEPENDENTES_ID,
                            :SALARIO_REAL,
                            :TIPO_CONTRATO)""",
[
    {"NOME_FUNCIONARIO": funcionario["NOME_FUNCIONARIO"],
    "CARGO_ID": funcionario["CARGO_ID"],
    "DEPARTAMENTO_ID": funcionario["DEPARTAMENTO_ID"],
    "DEPENDENTES_ID": funcionario["DEPENDENTES_ID"],
    "SALARIO_REAL": funcionario["SALARIO_REAL"],
    "TIPO_CONTRATO": funcionario["TIPO_CONTRATO"]}
    for funcionario in file_information
])
    
    print('')
    print('Values inserted successfully!')
    print('')
    
def main():
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/funcionarios.csv"
    file_information = read_csv_file(file_name)
    
    print("***FILE INFORMATION***")
    print(file_information)
    print("**********************")
    
    create_table_FUNCIONARIOS()
    
    populate_table_FUNCIONARIOS(file_information)

main()