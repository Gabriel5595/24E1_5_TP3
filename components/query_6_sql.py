import sqlite3

def query_6_sql():
    print()
    print("*** QUERY 6 ***")
    print("Listar o funcionário que teve o salário médio mais alto.")
    print()
    
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT FUNCIONARIOS.NOME_FUNCIONARIO,
                            AVG(HISTORICO_SALARIOS.SALARIO) AS SALARIO_MEDIO
                        FROM FUNCIONARIOS
                        JOIN HISTORICO_SALARIOS ON FUNCIONARIOS.FUNCIONARIO_ID = HISTORICO_SALARIOS.FUNCIONARIO_ID
                        GROUP BY FUNCIONARIOS.FUNCIONARIO_ID, FUNCIONARIOS.NOME_FUNCIONARIO
                        ORDER BY SALARIO_MEDIO DESC
                        LIMIT 1;""")
        results = cursor.fetchall()
        for line in results:
            print(line)