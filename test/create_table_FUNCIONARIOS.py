import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_table_FUNCIONARIOS():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FUNCIONARIOS (
        FUNCIONARIO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME_FUNCIONARIO VARCHAR(50) NOT NULL,
        CARGO_ID INTEGER,
        DEPARTAMENTO_ID INTEGER,
        DEPENDENTES_ID INTEGER,
        SALARIO_REAL DECIMAL(10, 2) NOT NULL,
        TIPO_CONTRATO VARCHAR(3) NOT NULL,
        FOREIGN KEY (CARGO_ID) REFERENCES CARGOS (CARGO_ID),
        FOREIGN KEY (DEPARTAMENTO_ID) REFERENCES DEPARTAMENTOS (DEPARTAMENTO_ID),
        FOREIGN KEY (DEPENDENTES_ID) REFERENCES DEPENDENTES (DEPENDENTES_ID)
        )
""")
    
    print('')
    print("Table created sucessfully!")
    print('')

def main():
    create_table_FUNCIONARIOS()

main()