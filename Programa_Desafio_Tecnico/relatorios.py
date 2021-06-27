from datetime import date

def verifica_regiao(lista_pedidos):

    destino_sul = False

    for pedido in lista_pedidos:
        if pedido['Regiao de Origem'] == 'Sul' and pedido['Tipo do produto'] == 'Brinquedo':
            print('O Pacote '+ pedido['indice'] + 'um produto do tipo "Brinquedo"\n')
            destino_sul = True

    if not(destino_sul):
        print(30*'-',end='')
        print('Nenhum pacote com Região de Origem Sul possui tipo de produto "Brinquedos"',end='')
        print(30*'-','\n')
    destino_sul = False
    

def separa_pedidos(lista_pedido):

    pedidos_centro_oeste = list()
    pedidos_nordeste = list()
    pedidos_norte = list()
    pedidos_sudeste = list()
    pedidos_sul = list()

    pedidos_joias = list()
    pedidos_brinquedos = list()
    pedidos_livros = list()
    pedidos_eletronicos = list()
    pedidos_bebidas = list()

    for pacote in lista_pedido:
        if pacote['Regiao de Destino'] == 'Centro-oeste':
            pedidos_centro_oeste.append(pacote)
        elif pacote['Regiao de Destino'] == 'Nordeste':
            pedidos_nordeste.append(pacote)
        elif pacote['Regiao de Destino'] == 'Norte':
            pedidos_norte.append(pacote)
        elif pacote['Regiao de Destino'] == 'Sudeste':
            pedidos_sudeste.append(pacote)
        else:
            pedidos_sul.append(pacote)

    relatorio_regiao_destino(pedidos_centro_oeste,pedidos_nordeste,pedidos_norte,pedidos_sudeste,pedidos_sul)

    for pacote in lista_pedido:
        if pacote['Tipo do produto'] == 'Jóias':
            pedidos_joias.append(pacote)
        elif pacote['Tipo do produto'] == 'Brinquedos':
            pedidos_brinquedos.append(pacote)
        elif pacote['Tipo do produto'] == 'Eletrônicos':
            pedidos_eletronicos.append(pacote)
        elif pacote['Tipo do produto'] == 'Livros':
            pedidos_livros.append(pacote)
        else:
            pedidos_bebidas.append(pacote)

    relatorio_produto(pedidos_joias,pedidos_brinquedos,pedidos_eletronicos,pedidos_livros,pedidos_bebidas)

    
 
def relatorio_regiao_destino(pedidos_centro_oeste,pedidos_nordeste,pedidos_norte,pedidos_sudeste,pedidos_sul):
    
    data = date.today()
    relatorio = open(f'relatorio_por_regiao_{data}.txt','w')

    relatorio.write('[Relação de pacotes agrupadas por região de destino] \n\n')
    print('---[Lista de pacotes agrupadas por região de destino]--- \n')

    relatorio.write('---------[Lista de pacotes com destino - Centro-oeste]---------\n')
    print('---------Lista de pacotes com destino - Centro-oeste---------')


    for pacote in pedidos_centro_oeste:
        print('Pacote: ',pacote['indice'],'\n')
        relatorio.write(f'Pacote: {pacote["indice"]},\n')
        for chave,valor in pacote.items():
            if chave == 'indice':
                continue
            print(f'{chave} : {valor}\n')
            relatorio.write(f'{chave} : {valor}\n')
        print(30 * '-')
        print()
        relatorio.write('\n')


    relatorio.write('---------[Lista de pacotes com destino - Nordeste]---------\n')
    print('---------Lista de pacotes com destino - Nordeste---------')


    for pacote in pedidos_nordeste:
        print('Pacote: ',pacote['indice'],'\n')
        relatorio.write(f'Pacote: {pacote["indice"]},\n')
        for chave,valor in pacote.items():
            if chave == 'indice':
                continue
            print(f'{chave} : {valor}\n')
            relatorio.write(f'{chave} : {valor}\n')
        print()
        relatorio.write('\n')
    

    relatorio.write('---------[Lista de pacotes com destino - Norte]---------\n')
    print('---------Lista de pacotes com destino - Norte---------')



    for pacote in pedidos_norte:
        print('Pacote: ',pacote['indice'],'\n')
        relatorio.write(f'Pacote: {pacote["indice"]},\n')
        for chave,valor in pacote.items():
            if chave == 'indice':
                continue
            print(f'{chave} : {valor}\n')
            relatorio.write(f'{chave} : {valor}\n')
        print()
        relatorio.write('\n')

    relatorio.write('---------[Lista de pacotes com destino - Sudeste]---------\n')
    print('---------Lista de pacotes com destino - Sudeste---------')



    for pacote in pedidos_sudeste:
        print('Pacote: ',pacote['indice'],'\n')
        relatorio.write(f'Pacote: {pacote["indice"]},\n')
        for chave,valor in pacote.items():
            if chave == 'indice':
                continue
            print(f'{chave} : {valor}\n')
            relatorio.write(f'{chave} : {valor}\n')
        print()
        relatorio.write('\n')



    relatorio.write('---------[Lista de pacotes com destino - Sul]---------\n')
    print('---------Lista de pacotes com destino - Sul---------')


    for pacote in pedidos_sul:
        print('Pacote: ',pacote['indice'],'\n')
        relatorio.write(f'Pacote: {pacote["indice"]},\n')
        for chave,valor in pacote.items():
            if chave == 'indice':
                continue
            print(f'{chave} : {valor}\n')
            relatorio.write(f'{chave} : {valor}\n')
        print()
        relatorio.write('\n')

    relatorio.close()

def relatorio_produto(pedidos_joias,pedidos_brinquedos,pedidos_eletronicos,pedidos_livros,pedidos_bebidas):
    
    data_atual = date.today()
    relatorio = open(f'relatorio_por_produtos-{data_atual}.txt','w')

    relatorio.write('[Relação de pacotes agrupados por Tipo de produto]\n\n')
    relatorio.write('----------[Relação de Pacotes com - Jóias]---------- \n')
    for pacote in pedidos_joias:
        relatorio.write(f'Pacote: {pacote["indice"]},\n')
        for chave,valor in pacote.items():
            if chave == 'indice':
                continue
            relatorio.write(f'{chave} : {valor}\n')
        relatorio.write('\n')
    
    relatorio.write('----------[Relação de Pacotes com - Brinquedos]---------- \n')
    for pacote in pedidos_brinquedos:
        relatorio.write(f'Pacote: {pacote["indice"]},\n')
        for chave,valor in pacote.items():
            if chave == 'indice':
                continue
            relatorio.write(f'{chave} : {valor}\n')
        relatorio.write('\n')

    relatorio.write('----------[Relação de Pacotes com - Eletrônicos]---------- \n')
    for pacote in pedidos_eletronicos:
        relatorio.write(f'Pacote: {pacote["indice"]},\n')
        for chave,valor in pacote.items():
            if chave == 'indice':
                continue
            relatorio.write(f'{chave} : {valor}\n')
        relatorio.write('\n')

    relatorio.write('----------[Relação de Pacotes com - Livros]---------- \n')
    for pacote in pedidos_livros:
        relatorio.write(f'Pacote: {pacote["indice"]},\n')
        for chave,valor in pacote.items():
            if chave == 'indice':
                continue
            relatorio.write(f'{chave} : {valor}\n')
        relatorio.write('\n')

    relatorio.write('----------[Relação de Pacotes com - Bebidas]---------- \n')
    for pacote in pedidos_bebidas:
        relatorio.write(f'Pacote: {pacote["indice"]},\n')
        for chave,valor in pacote.items():
            if chave == 'indice':
                continue
            relatorio.write(f'{chave} : {valor}\n')
        relatorio.write('\n')

    relatorio.close()

def verifica_vendedor(lista_pedido):
    lista_vendedores = list()
    pacotes_por_vendedor = dict()
    qtd_pacotes = 0

    for pacote in lista_pedido:
        for chave,valor in pacote.items():
            if chave == 'Codigo do vendedor do produto':
                lista_vendedores.append(valor)

    for pacote in lista_pedido:
        for vendedor in lista_vendedores:
            for chave,valor in pacote.items():
                if valor == vendedor:
                    qtd_pacotes += 1
            pacotes_por_vendedor[vendedor] = qtd_pacotes
        qtd_pacotes = 0

    print(10 * '-',end='')
    print('[Lista de pacotes enviados por cada vendedor]',end='')
    print(10 * '-')
    for k,v in pacotes_por_vendedor.items():
        
        print(f'Código do Vendedor: {k} --- Quantidade de Pacotes: {v}')


def relatorio_pedidos(lista_pedido):
    
    verifica_regiao(lista_pedido)
    separa_pedidos(lista_pedido)
    verifica_vendedor(lista_pedido)
 



    