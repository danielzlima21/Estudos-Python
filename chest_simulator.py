#auto open, estatisticas, função, aumentar sorte, loja, aumentar inventario, capacidade de inventario

import random

player_coin = 10000
sorte = 1

#estatisticas
total_comuns_pegos = 0
total_epicos_pegos = 0
total_lendarios_pegos = 0
vendas_realizadas = 0
baus_abertos = 0
dinheiro_ganho = 0
mais_caro = 0

player_inventory = []

bau_de_madeira = [{'nome': 'papel', 'valor': 1, 'raridade': 'comun'},
                  {'nome': 'lapis', 'valor': 2, 'raridade': 'epico'},
                  {'nome': 'estojo', 'valor': 3, 'raridade': 'lendario'}]

bau_de_ouro = [{'nome': 'ferro', 'valor': 3, 'raridade': 'comun'},
                  {'nome': 'ouro', 'valor': 5, 'raridade': 'epico'},
                  {'nome': 'diamante', 'valor': 7, 'raridade': 'lendario'}]

bau_de_diamante = [{'nome': 'colar', 'valor': 7, 'raridade': 'comun'},
                  {'nome': 'joia', 'valor': 11, 'raridade': 'epico'},
                  {'nome': 'safira', 'valor': 15, 'raridade': 'lendario'}]

def checar_raridade(raridade):
    global total_comuns_pegos, total_epicos_pegos, total_lendarios_pegos

    if raridade == 'comun':
        total_comuns_pegos += 1
    elif raridade == 'epico':
        total_epicos_pegos += 1
    elif raridade == 'lendario':
        total_lendarios_pegos += 1

def checar_mais_caro():
    global mais_caro

    maior = 0
    for iten in player_inventory:
        if iten['valor'] > maior:
            mais_caro = iten

def abrir_bau(bau, valor):
    global player_coin, baus_abertos

    if player_coin < valor:
        print(f'moedas insuficientes, suas moedas: {player_coin}')
    else:
        player_coin -= valor
        baus_abertos += 1
        numero = random.randint(1, 100)
        if numero <= 10:
            raridade = 'lendario'
        elif numero <= 50:
            raridade = 'epico'
        elif numero <= 100:
            raridade = 'comun'
        print(f'debug:{numero, raridade}')
        
        for iten in(bau):
            if iten['raridade'] == raridade:
                print(f'debug:{iten}')
                itens.append(iten)
                iten = random.choice(itens)
                player_inventory.append(iten)
                checar_raridade(raridade)
                print(f'debug:{player_inventory}')

while True:
    print(f'Moedas: {player_coin}')
    print('~' * 30)
    print('1 - [10$] - bau de madeira')
    print('2 - [40$] - bau de ouro')
    print('3 - [80$] - bau de diamante')
    print('~' * 30)
    print('4 - ver inevtario')
    print('5 - vender tudo')
    print('~' * 30)
    print('6 - estatísticas')

    itens = []
    checar_mais_caro()

    menu = int(input('digite: '))

    if menu == 1:
        abrir_bau(bau_de_madeira, 10)

    elif menu == 2:
        abrir_bau(bau_de_ouro, 40)

    elif menu == 3:
        abrir_bau(bau_de_diamante, 80)

    elif menu == 4:
        print('=== INVENTÁRIO ===')
        if not player_inventory:
            print('inventário vazio')
        else:
            for iten in player_inventory:
                print(f"Nome: {iten['nome']} | Valor: {iten['valor']}$ | Raridade: {iten['raridade']}")
            total = sum(item['valor'] for item in player_inventory)
            print(f'{total}$ Acumulado')

    elif menu == 5:
        if not player_inventory:
            print('inventário vazio')
        else:
            print('=== VENDENDO ===')
            total = sum(item['valor'] for item in player_inventory)
            player_coin += total
            player_inventory.clear()
            vendas_realizadas += 1
            dinheiro_ganho += total
            print(f'você recebeu: {total}$ e ficou com: {player_coin}$')

    elif menu == 6:
        print('=== ESTATISTÍCAS ===')
        print(f'dinheiro atual: {player_coin}')
        print(f'dinheiro ganho ate agora: {dinheiro_ganho}')
        print(f'baús abertos: {baus_abertos}')
        print(f'vendas realizadas: {vendas_realizadas}')
        print(f'total de comuns: {total_comuns_pegos}')
        print(f'total de epicos: {total_epicos_pegos}')
        print(f'total de lendarios: {total_lendarios_pegos}')
        print(f'iten mais caro pego: {mais_caro}')