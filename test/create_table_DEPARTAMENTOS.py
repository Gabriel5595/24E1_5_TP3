import sqlite3
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_table_DEPARTAMENTOS():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DEPARTAMENTOS (
        DEPARTAMENTO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME_DEPARTAMENTO VARCHAR(20) NOT NULL,
        FUNCIONARIO_GEN_ID INTEGER,
        ANDAR INTEGER NOT NULL,
        LOCAL_DEPARTAMENTO VARCHAR(20) NOT NULL,
        FOREIGN KEY (FUNCIONARIO_GEN_ID) REFERENCES DEPARTAMENTOS (FUNCIONARIO_ID)
        )
""")
    
    print('')
    print("Table created sucessfully!")
    print('')

def main():
    create_table_DEPARTAMENTOS()

main()