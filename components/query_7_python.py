from tabulate import tabulate

from components.read_csv_file import read_csv_file

def query_7_python():
    print()
    print("*** QUERY 7 ***")
    print("Listar o analista que é pai de 2 (duas) meninas.")
    print()
    
    funcionarios_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/funcionarios.csv"
    dependentes_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/dependentes.csv"
    
    funcionarios = read_csv_file(funcionarios_csv)
    dependentes = read_csv_file(dependentes_csv)
    
    dados = []
    
    for funcionario in funcionarios:
        dado_selecionado = {}
        
        if funcionario["DEPENDENTES_ID"] == "NULL":
            pass
        else:
            for dependente in dependentes:
                if (dependentes.index(dependente)+1) == int(funcionario["DEPENDENTES_ID"]):
                    if dependente["PARENTESCO_DEPENDENTE_1"] == "filha" and dependente["PARENTESCO_DEPENDENTE_2"] == "filha":
                        dado_selecionado["Nome do Funcionario"] = funcionario["NOME_FUNCIONARIO"]
                        dado_selecionado["Dependente 1"] = dependente["DEPENDENTE_1"]
                        dado_selecionado["Parentesco 1"] = dependente["PARENTESCO_DEPENDENTE_1"]
                        dado_selecionado["Dependente 2"] = dependente["DEPENDENTE_2"]
                        dado_selecionado["Parentesco 2"] = dependente["PARENTESCO_DEPENDENTE_2"]
        
                        dados.append(dado_selecionado)
    
    print(tabulate(dados, headers="keys", tablefmt="grid"))