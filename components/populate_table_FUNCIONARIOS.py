import sqlite3

from components.read_csv_file import read_csv_file

def populate_table_FUNCIONARIOS():
    
    file_name = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/funcionarios.csv"
    file_information = read_csv_file(file_name)
    
    with sqlite3.connect("database.db") as connection:
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