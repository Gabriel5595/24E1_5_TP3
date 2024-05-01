from tabulate import tabulate

from components.read_csv_file import read_csv_file

def query_2_python():
    
    print()
    print("*** QUERY 2 ***")
    print("Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes.")
    print()
    
    funcionarios_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/funcionarios.csv"
    dependentes_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/dependentes.csv"
    departamentos_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/departamentos.csv"
    cargos_csv = "C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Projeto de Bloco - Fundamentos de Dados/TPs/TP3/resources/cargos.csv"
    
    funcionarios = read_csv_file(funcionarios_csv)
    dependentes = read_csv_file(dependentes_csv)
    departamentos = read_csv_file(departamentos_csv)
    cargos = read_csv_file(cargos_csv)
    
    dados = []
    
    for funcionario in funcionarios:
        dado_selecionado = {}
        
        if funcionario["CARGO_ID"] == "NULL":
            pass
        else:
            dado_selecionado["Nome do Funcionario"] = funcionario["NOME_FUNCIONARIO"]
            
            for cargo in cargos:
                if funcionario["CARGO_ID"] == "NULL":
                    pass
                elif (cargos.index(cargo)+1) == int(funcionario["CARGO_ID"]):
                    dado_selecionado["Cargo"] = cargo["NIVEL_CARGO"]
            
            for departamento in departamentos:
                if funcionario["DEPARTAMENTO_ID"] == "NULL":
                    pass
                if (departamentos.index(departamento)+1) == int(funcionario["DEPARTAMENTO_ID"]):
                    dado_selecionado["Departamento"] = departamento["NOME_DEPARTAMENTO"]
            
            for dependente in dependentes:
                if (dependentes.index(dependente)+1) == int(funcionario["DEPENDENTES_ID"]):
                    dado_selecionado["Nome Dependente 1"] = dependente["DEPENDENTE_1"]
                    dado_selecionado["Nome Dependente 2"] = dependente["DEPENDENTE_2"]
        
            dados.append(dado_selecionado)
    
    print(tabulate(dados, headers="keys", tablefmt="grid"))