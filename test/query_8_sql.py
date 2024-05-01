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

def query_8_sql():
    print()
    print("*** QUERY 8 ***")
    print("Listar o analista que tem o salário mais alto, e que ganhe entre 5000 e 9000.")
    print()
    
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT FUNCIONARIOS.NOME_FUNCIONARIO,
                            FUNCIONARIOS.SALARIO_REAL,
                            CARGOS.NIVEL_CARGO,
                            FUNCIONARIOS.SALARIO_REAL
                        FROM FUNCIONARIOS
                        JOIN CARGOS ON FUNCIONARIOS.CARGO_ID = CARGOS.CARGO_ID
                        WHERE CARGOS.NIVEL_CARGO = 'Analista'
                            AND FUNCIONARIOS.SALARIO_REAL BETWEEN 5000 AND 9000
                        ORDER BY FUNCIONARIOS.SALARIO_REAL DESC
                        LIMIT 1;
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
    
    query_8_sql()

main()