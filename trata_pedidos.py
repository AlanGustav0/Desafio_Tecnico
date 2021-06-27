def trata_pedido(arquivo):
    conteudo = 0
    indice = 1

    conteudo_pedido = dict()
    lista_dados = ['Codigo','Regiao de Origem','Regiao de Destino','Codigo Loggi','Codigo do vendedor do produto','Tipo do produto']
    pedidos = list()
    lista_de_pedidos = list()
    for linha in arquivo:
        pedido = linha.split(':')
        pedidos.append(pedido[1])


    for codigos in pedidos:
        
        conteudo_pedido['indice'] = indice
        conteudo_pedido[lista_dados[conteudo]] = codigos[:16]
        for i in range(1,len(codigos)-1,3):
            conteudo += 1
            codigo = codigos[i:i+3]
            conteudo_pedido[lista_dados[conteudo]] = '000' if codigo == '000' else int(codigo)

        lista_de_pedidos.append(conteudo_pedido.copy())
            
        conteudo = 0
        indice += 1
    
    return lista_de_pedidos