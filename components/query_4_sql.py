import sqlite3

def query_4_sql():
    print()
    print("*** QUERY 4 ***")
    print("Listar a média de idade dos filhos dos funcionários por departamento.")
    print()
    
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
                        SELECT DEPARTAMENTOS.NOME_DEPARTAMENTO,
                        ROUND(
                            AVG(
                                COALESCE(
                                    CASE WHEN DEPENDENTES.PARENTESCO_DEPENDENTE_1 IN ('filho', 'filha') THEN DEPENDENTES.IDADE_DEPENDENTE_1 END, 0)
                                + COALESCE(
                                    CASE WHEN DEPENDENTES.PARENTESCO_DEPENDENTE_2 IN ('filho', 'filha') THEN DEPENDENTES.IDADE_DEPENDENTE_2 END, 0)
                            )
                        ) AS MEDIA_IDADE_DEPENDENTES
                        FROM FUNCIONARIOS
                        JOIN DEPARTAMENTOS ON FUNCIONARIOS.DEPARTAMENTO_ID = DEPARTAMENTOS.DEPARTAMENTO_ID
                        JOIN DEPENDENTES ON FUNCIONARIOS.DEPENDENTES_ID = DEPENDENTES.DEPENDENTES_ID
                        GROUP BY DEPARTAMENTOS.NOME_DEPARTAMENTO;
                        """)
        results = cursor.fetchall()
        for line in results:
            print(line)