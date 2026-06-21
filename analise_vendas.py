vendas = [
    {"produto": "Mouse", "preco": 50},
    {"produto": "Teclado", "preco": 120},
    {"produto": "Mouse", "preco": 50},
    {"produto": "Monitor", "preco": 900},
    {"produto": "Mouse", "preco": 50},
    {"produto": "Teclado", "preco": 120},
]

def faturamento_total(vendas):
    total_faturamento = sum(item["preco"] for item in vendas)
    return(total_faturamento)

def total_vendas(vendas):
    total_vendas = len(vendas)
    return(total_vendas)

def mais_vendido(vendas):
    produtos = [item['produto'] for item in vendas]
    produto_mais_vendido = max(produtos, key=produtos.count)
    quantidade = produtos.count(produto_mais_vendido)
    return(produto_mais_vendido, quantidade)

def mais_caro(vendas):
    item_mais_caro = max(vendas, key=lambda item: item['preco'])
    preco = item_mais_caro['preco']
    nome = item_mais_caro['produto']
    return(nome, preco)

def calcula_media(vendas):
    media = faturamento_total(vendas) / total_vendas(vendas)
    return(media)
