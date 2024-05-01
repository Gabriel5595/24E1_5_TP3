import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.read_csv_file import read_csv_file

def query_5_python():
    print()
    print("*** QUERY 5 ***")
    print("Listar qual estagiário possui filho.")
    print()
    
    funcionarios_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/funcionarios.csv"
    dependentes_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/dependentes.csv"
    
    funcionarios = read_csv_file(funcionarios_csv)
    dependentes = read_csv_file(dependentes_csv)
    
    for funcionario in funcionarios:
        if funcionario["CARGO_ID"] == "1":
            if dependentes[funcionarios.index(funcionario)]["PARENTESCO_DEPENDENTE_1"] == "filha":
                print(f"""Funcionario: {funcionario["NOME_FUNCIONARIO"]} | Dependente: {dependentes[funcionarios.index(funcionario)]["DEPENDENTE_1"]} | Parentesco: {dependentes[funcionarios.index(funcionario)]["PARENTESCO_DEPENDENTE_1"]}""")
            if dependentes[funcionarios.index(funcionario)]["PARENTESCO_DEPENDENTE_1"] == "filho":
                print(f"""Funcionario: {funcionario["NOME_FUNCIONARIO"]} | Dependente: {dependentes[funcionarios.index(funcionario)]["DEPENDENTE_1"]} | Parentesco: {dependentes[funcionarios.index(funcionario)]["PARENTESCO_DEPENDENTE_1"]}""")
            if dependentes[funcionarios.index(funcionario)]["PARENTESCO_DEPENDENTE_2"] == "filha":
                print(f"""Funcionario: {funcionario["NOME_FUNCIONARIO"]} | Dependente: {dependentes[funcionarios.index(funcionario)]["DEPENDENTE_2"]} | Parentesco: {dependentes[funcionarios.index(funcionario)]["PARENTESCO_DEPENDENTE_2"]}""")
            if dependentes[funcionarios.index(funcionario)]["PARENTESCO_DEPENDENTE_2"] == "filho":
                print(f"""Funcionario: {funcionario["NOME_FUNCIONARIO"]} | Dependente: {dependentes[funcionarios.index(funcionario)]["DEPENDENTE_2"]} | Parentesco: {dependentes[funcionarios.index(funcionario)]["PARENTESCO_DEPENDENTE_2"]}""")
    
def main():
    query_5_python()

main()