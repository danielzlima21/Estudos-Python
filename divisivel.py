def analisar(numero):
    qtd_par = 0
    qtd_impar = 0
    for i in range(numero + 1):
        if i % 2 == 0:
            print(f'o número {i} é par')
            qtd_par += 1
        else:
            print(f'o número {i} é impar')
            qtd_impar += 1
    print(f'Quantidade de números pares: {qtd_par}')
    print(f'Quantidade de números impares: {qtd_impar}')

analisar(359)