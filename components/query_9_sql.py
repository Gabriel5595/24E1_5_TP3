import sqlite3

def query_9_sql():
    print()
    print("*** QUERY 9 ***")
    print("Listar qual departamento possui o maior número de dependentes.")
    print()
    
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT DEPARTAMENTOS.NOME_DEPARTAMENTO, 
                            COUNT(*) AS NUMERO_DEPENDENTES
                        FROM DEPARTAMENTOS
                        JOIN FUNCIONARIOS ON DEPARTAMENTOS.DEPARTAMENTO_ID = FUNCIONARIOS.DEPARTAMENTO_ID
                        JOIN DEPENDENTES ON FUNCIONARIOS.DEPENDENTES_ID = DEPENDENTES.DEPENDENTES_ID
                        GROUP BY DEPARTAMENTOS.DEPARTAMENTO_ID
                        ORDER BY NUMERO_DEPENDENTES DESC
                        LIMIT 1;

                        """)
        results = cursor.fetchall()
        for line in results:
            print(line)