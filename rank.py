jogadores = [
    {"nome": "Ana", "pontos": 150},
    {"nome": "Carlos", "pontos": 300},
    {"nome": "João", "pontos": 120},
    {"nome": "Marina", "pontos": 450},
    {"nome": "Pedro", "pontos": 220}
]

def adicionar_jogador():
    try:
        jogador_nome = input('Digite o nome: ')
        jogador_pontos = int(input('Digite os pontos: '))
        novo_jogador = {'nome': jogador_nome, 'pontos': jogador_pontos}
        jogadores.append(novo_jogador)
    except ValueError:
        print('Erro de digitacao')

def listar_jogadores():
    if len (jogadores) == 0:
        print('Nenhum jogador cadastrado')
        return
    else:
        rank = 1
        jogadores_ordenados = sorted(jogadores, key=lambda x: x['pontos'], reverse=True)
        for jogador in jogadores_ordenados:
            print(f"{rank}° - Nome: {jogador['nome']} | Pontos: {jogador['pontos']}")
            rank += 1
        print("=" * 20)

while True:
    print('1 - Adicionar jogador')
    print('2 - Listar jogadores')
    print('3 - Sair')
    print("=" * 20)

    while True:
        try:
            menu = int(input('Digite: '))
            if menu in (1, 2, 3):
                break
            else:
                print('Opcao invalida')
        except ValueError:
            print('Erro de digitacao')

    if menu == 1:
        adicionar_jogador()
    elif menu == 2:
        listar_jogadores()
    elif menu == 3:
        print('Programa finalizado')
        break