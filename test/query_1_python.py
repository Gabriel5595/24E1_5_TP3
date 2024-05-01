from tabulate import tabulate
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_csv_file import read_csv_file

def query_1_python():
    print()
    print("*** QUERY 1 ***")
    print("Listar individualmente as tabelas de: Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes em ordem crescente.")
    print()
    
    funcionarios_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/funcionarios.csv"
    dependentes_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/dependentes.csv"
    departamentos_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/departamentos.csv"
    cargos_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/cargos.csv"
    historico_salarios_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/historico_salarios.csv"
    
    funcionarios = read_csv_file(funcionarios_csv)
    dependentes = read_csv_file(dependentes_csv)
    departamentos = read_csv_file(departamentos_csv)
    cargos = read_csv_file(cargos_csv)
    historico_salarios = read_csv_file(historico_salarios_csv)
    
    print("*** TABELA DEPARTAMENTOS ***")
    print(tabulate(departamentos, headers="keys", tablefmt="grid"))
    print()
    
    print("*** TABELA FUNCIONÁRIOS ***")
    print(tabulate(funcionarios, headers="keys", tablefmt="grid"))
    print()
    
    print("*** TABELA DEPENDENTES ***")
    print(tabulate(dependentes, headers="keys", tablefmt="grid"))
    print()
    
    print("*** TABELA CARGOS ***")
    print(tabulate(cargos, headers="keys", tablefmt="grid"))
    print()
    
    print("*** TABELA HISTÓRICO DE SALÁRIOS ***")
    print(tabulate(historico_salarios, headers="keys", tablefmt="grid"))
    print()
    
def main():
    query_1_python()

main()