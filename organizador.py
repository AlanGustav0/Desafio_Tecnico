def organiza_pedido(lista_pedidos):
    lista_regioes = {111:'Centro-oeste',333:'Nordeste',555:'Norte',888:'Sudeste','000':'Sul'}
    lista_produtos = {'000':'Jóias',111:'Livros',333:'Eletrônicos',555:'Bebidas',888:'Brinquedos'}

    for pedidos in lista_pedidos:
        for c_regiao,v_regiao in lista_regioes.items():
            for c_produto,v_produto in pedidos.items():
                if c_regiao == v_produto and c_produto != 'Tipo do produto' and c_produto != 'Codigo Loggi' and c_produto != 'Codigo do vendedor do produto':
                    pedidos[c_produto] = v_regiao
        
        for c_produtos,v_produtos in lista_produtos.items():
            for c_produto,v_produto in pedidos.items():
                if c_produtos == v_produto and c_produto == 'Tipo do produto':
                    pedidos[c_produto] = v_produtos

    return lista_pedidos
