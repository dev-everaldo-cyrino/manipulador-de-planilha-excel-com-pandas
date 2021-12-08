import pandas as pd
gerentes = pd.read_excel("Gerentes.xlsx")
vendas12 = pd.read_excel("Vendas -Dez.xlsx")
vendas = pd.read_excel("Vendas.xlsx")
while True:
    op = input('''
    ----- menu -----
    1 - print dados
    2- pegando 1 linha
    3- pegando linhas correspondente a uma condição
    4- pegando linhas correspondente a uma condição e colunas
    5- criando uma nova coluna
    6- adicionando linhas
    7- excluindo linhas ou colunas
    8- preencher os campos vazios com a media da coluna
    9- preenche com o ultimo valor
    10- calcular indicador simples
    11- calcular indicador composto
    12- mesclar DataFrame
    0 - sair''')
    if op ==1:
        pass
    elif op ==2:
        pass
    elif op ==3:
        pass
    elif op ==4:
        pass
    elif op ==5:
        pass
    elif op ==6:
        pass
    elif op ==7:
        pass
    elif op ==8:
        pass
    elif op ==9:
        pass
    elif op ==10:
        pass
    elif op ==11:
        pass
    elif op ==12:
        pass
    elif op ==0:
        break