import sqlite3

def create_table_CARGOS():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CARGOS(
        CARGO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DESCRICAO VARCHAR(255) NOT NULL,
        SALARIO_BASE DECIMAL(10, 2) NOT NULL,
        NIVEL_CARGO VARCHAR(20) NOT NULL,
        IMPORTANCIA VARCHAR(10) NOT NULL
    )
""")
    
    print('')
    print("Table created sucessfully!")
    print('')