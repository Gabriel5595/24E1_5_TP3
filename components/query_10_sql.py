import sqlite3

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