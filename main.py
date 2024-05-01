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
from components.query_1_python import query_1_python
from components.query_2_python import query_2_python
from components.query_3_python import query_3_python
from components.query_4_sql import query_4_sql
from components.query_5_python import query_5_python
from components.query_6_sql import query_6_sql
from components.query_7_python import query_7_python
from components.query_8_sql import query_8_sql
from components.query_9_sql import query_9_sql
from components.query_10_sql import query_10_sql

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
    
    query_1_python()
    query_2_python()
    query_3_python()
    query_4_sql()
    query_5_python()
    query_6_sql()
    query_7_python()
    query_8_sql()
    query_9_sql()
    query_10_sql()

main()