import sqlite3

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