import pandas as pd
while True:
    op = int(input('''
    ----- menu -----
    0 - escolha uma tabela
    1 - print dados
    2- pegando 1 linha
    3- pegando linhas correspondente a uma condição
    4- Resumo dos dados
    5- criando uma nova coluna
    6- adicionando linhas
    7- excluindo linhas ou colunas
    8- preencher os campos vazios com a media da coluna
    9- preenche com o ultimo valor
    10- calcular indicador simples
    11- calcular indicador composto
    12- mesclar DataFrame
    13 - sair
    :'''))
    if op == 0:
        op1 = int(input('''
        -----escolha uma tabela-----
        1- tabela gerentes
        2- tabela vendas de dezembro
        3- tabela total de vendas
        :'''))
        if op1 ==1:
            tb = pd.read_excel("Gerentes.xlsx")
        elif op1 ==2:
            tb = pd.read_excel("Vendas - Dez.xlsx")
        else:
            tb = pd.read_excel("Vendas.xlsx")
        print('----------------------------------------------')
        
    elif op ==1:
        print(tb)
    elif op ==2:
        linha = int(input('qual linha deseja pegar: '))
        try:
            print(tb.loc[linha])
        except:
            print('linha não encontrada')
        print('----------------------------------------------')     
    elif op ==3:
        coluna = input('nome da coluna:  ')
        linha = input('nome da linha(ex:loja de roupas):  ')
        try:
            print(tb.loc[tb[coluna] == linha])
        except:
            print('dado não encontrada')
        print('----------------------------------------------')
            
    elif op ==4:
        print(tb.describe())
    elif op ==5:
        coluna = input('nome da coluna: ')
        valor = float(input('dado da coluna nova: '))
        try:
            tb.loc[:,coluna] = valor
            print('coluna criada com sucesso')
        except:
            print('erro ao criar a coluna')
        print('----------------------------------------------')
        
    elif op ==6:
        linha = input('nome do arquivo que sera anexado: ')
        try:
            linha = pd.read_excel(linha)
            tb.append(linha)
            print('dados anexados com sucesso')
        except:
            print('erro ao tentar anexar os dados')
        print('----------------------------------------------')
            
    elif op ==7:
        op = int(input('''
        -----exluindo dados-----
        0 - exluir linha
        1 - exluir coluna'''))
        dado = input('nome do dado excluido: ')
        try:
            tb = tb.drop(dado,axis=op)
            print(tb)
            print('dados excluidos com sucesso')
        except:
            print('erro ao tentar excluir os dados')
        print('----------------------------------------------')
            
    elif op ==8:
        dado = input('nome do dado: ')
        try:
            tb[dado] = tb[dado].fillna(tb[dado].mean())
            print('dados preenchidos com sucesso')
        except:
            print('erro ao tentar preencher dados os dados')
        print('----------------------------------------------')
            
    elif op ==9:
        dado = input('nome do dado: ')
        try:
            tb.ffill()
            print('dados preenchidos com sucesso')
        except:
            print('erro ao tentar preencher os dados')
        print('----------------------------------------------')
            
    elif op ==10:
        dado = input('nome da coluna: ')
        try:
            print(tb[dado].value_counts())
        except:
            print('erro ao tentar caulcular indicadores de dados')
        print('----------------------------------------------')
            
    elif op ==11:
        op1 = int(input('''
        1- deseja ver a soma dos valores
        2- deseja ver a media dos valores
        :'''))
        
            
        lista= input('nome da coluna1: ') 
        lista2= input('nome da coluna2: ') 
        try:
            if op1 ==1:
                print(tb[[lista,lista2]].groupby(lista).sum())
            else:
                print(tb[[lista,lista2]].groupby(lista).mean())
        except:
            print('erro ao tentar caulcular indicadores de dados')
        print('----------------------------------------------')
            
    elif op ==12:
        nome = input('nome da tabela: ')
        try:
            tb2 = pd.read_excel(nome)
            tb = tb.merge(tb2)
            print(tb)
        except:
            print('ocorreu algum erro')
        print('----------------------------------------------')
    elif op ==13:
        break