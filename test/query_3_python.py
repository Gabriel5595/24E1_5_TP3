from tabulate import tabulate
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_csv_file import read_csv_file

def query_3_python():
    print()
    print("*** QUERY 3 ***")
    print("Listar os funcionários que tiveram aumento salarial nos últimos 3 meses.")
    print()
    
    funcionarios_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/funcionarios.csv"
    historico_salarios_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/historico_salarios.csv"
    
    funcionarios = read_csv_file(funcionarios_csv)
    historico_salarios = read_csv_file(historico_salarios_csv)

    dados = []
    
    for funcionario in funcionarios:
        dado_selecionado = {}
        registro_salarios = []
        for registro in historico_salarios:
            if int(registro["FUNCIONARIO_ID"]) == funcionarios.index(funcionario)+1:
                registro_salarios.append(registro["SALARIO"])

        if registro_salarios[-1] > registro_salarios[-2]:
            dado_selecionado["Nome do Funcionario"] = funcionario["NOME_FUNCIONARIO"]
            dados.append(dado_selecionado)
        elif registro_salarios[-2] > registro_salarios[-3]:
            dado_selecionado["Nome do Funcionario"] = funcionario["NOME_FUNCIONARIO"]
            dados.append(dado_selecionado)
    
    print(tabulate(dados, headers="keys", tablefmt="grid"))

def main():
    query_3_python()

main()