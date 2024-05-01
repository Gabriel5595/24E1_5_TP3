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

def query_10_sql():
    print()
    print("*** QUERY 10 ***")
    print("Listar a média de salário por departamento em ordem decrescente.")
    print()
    
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT DEPARTAMENTOS.NOME_DEPARTAMENTO,
                            ROUND(AVG(FUNCIONARIOS.SALARIO_REAL)) AS MEDIA_SALARIO
                        FROM FUNCIONARIOS
                        JOIN DEPARTAMENTOS ON FUNCIONARIOS.DEPARTAMENTO_ID = DEPARTAMENTOS.DEPARTAMENTO_ID
                        GROUP BY DEPARTAMENTOS.NOME_DEPARTAMENTO
                        ORDER BY MEDIA_SALARIO DESC;
                        """)
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
    
    query_10_sql()

main()