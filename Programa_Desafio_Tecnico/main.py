import organizador,trata_pedidos,relatorios


def valida_pedidos(lista_pedido):

    lista_pedidos_validos = list()
    lista_pedidos_invalidos = list()

    tipos_de_produto = ['000',111,333,555,888]

    for pedido in lista_pedido:
        if not(pedido['Tipo do produto'] in tipos_de_produto):
            lista_pedidos_invalidos.append(pedido)
        elif pedido['Tipo do produto'] == '000' and pedido['Regiao de Origem'] == 111:
            lista_pedidos_invalidos.append(pedido)
        elif pedido['Codigo do vendedor do produto'] == 584:
            lista_pedidos_invalidos.append(pedido)
        else:
            lista_pedidos_validos.append(pedido)

    
    return lista_pedidos_validos


arquivo = open('pedidos.txt','r')

lista_pedido = trata_pedidos.trata_pedido(arquivo)

pedidos_validos = valida_pedidos(lista_pedido)
pedido_organizado = organizador.organiza_pedido(pedidos_validos)
relatorios.relatorio_pedidos(pedido_organizado)


arquivo.close()






