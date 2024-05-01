import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.drop_table import drop_tables
from components.create_table_CARGOS import create_table_CARGOS
from components.create_table_DEPARTAMENTOS import create_table_DEPARTAMENTOS
from components.create_table_FUNCIONARIOS import create_table_FUNCIONARIOS
from components.create_table_DEPENDENTES import create_table_DEPENDENTES
from components.create_table_HISTORICO_SALARIOS import create_table_HISTORICO_SALARIOS
from components.populate_table_CARGO import populate_table_CARGOS
from components.populate_table_DEPARTAMENTOS import populate_table_DEPARTAMENTOS
from components.populate_table_FUNCIONARIOS import populate_table_FUNCIONARIOS
from components.populate_table_DEPARTAMENTOS import populate_table_DEPARTAMENTOS
from components.populate_table_DEPENDENTES import populate_table_DEPENDENTES
from components.populate_table_HISTORICO_SALARIO import populate_table_HISTORICO_SALARIOS

def query_1_sql():
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        
        print()
        print("*** QUERY 1 ***")
        print("Listar individualmente as tabelas de: Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes em ordem crescente.")
        print()
        print("*** TABLE CARGOS ***")
        cursor.execute("""SELECT * FROM CARGOS
                        ORDER BY DESCRICAO ASC""")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** TABLE DEPARTAMENTOS ***")
        cursor.execute("""SELECT * FROM DEPARTAMENTOS
                        ORDER BY NOME_DEPARTAMENTO ASC""")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** TABLE DEPENDENTES ***")
        cursor.execute("""SELECT * FROM DEPENDENTES
                        ORDER BY DEPENDENTE_1 ASC""")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** TABLE FUNCIONARIOS ***")
        cursor.execute("""SELECT * FROM FUNCIONARIOS
                        ORDER BY NOME_FUNCIONARIO ASC""")
        results = cursor.fetchall()
        for line in results:
            print(line)
        
        print()
        print("*** TABLE HISTORICO_SALARIOS ***")
        cursor.execute("""SELECT * FROM HISTORICO_SALARIOS
                        ORDER BY SALARIO ASC""")
        results = cursor.fetchall()
        for line in results:
            print(line)

def main():
    drop_tables()
    
    create_table_CARGOS()
    create_table_DEPENDENTES()
    create_table_DEPARTAMENTOS()
    create_table_FUNCIONARIOS()
    create_table_HISTORICO_SALARIOS()
    
    populate_table_CARGOS()
    populate_table_DEPARTAMENTOS()
    populate_table_FUNCIONARIOS()
    populate_table_DEPENDENTES()
    populate_table_HISTORICO_SALARIOS()
    
    query_1_sql()

main()