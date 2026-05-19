def tabuada(numero):
    if numero <= 1:
        print('o numero precisa ser maior que 1')
    else:
        n_atual = 1
        while numero >= 1:
            print(f'TABUADA DO: {n_atual}')
            for i in range(1, 11):
                print(f'{n_atual} X {i} = {n_atual * i}')
            print()
            n_atual += 1
            numero -= 1

tabuada(7)

def tabuada(numero):

    for i in range(numero + 1):
        print(f'tabuada do {i}')
        for x in range(10 + 1):
            print(f'{i} X {x}= {i * x}')

tabuada(100)