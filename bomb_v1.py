#desarme a bomba randomnum. dicas impar ou par, n de dígitos, está entre +15 e +15
#Menu que mostra os jogadores e as vitórias mostra modo até acertar
#e com tentativas e adicionar jogador. Jogar de novo. Se escrever dica gasta uma cada jogador tem 5 

import random, time
par = False
impar = False
tentativas = 5

print('descubra o codigo da bomba e desarme-a')
print('voce tem 5 tentativas')
CODIGO = random.randint(1, 50)
print(CODIGO)

#dica de par ou impar
if CODIGO % 2 == 0:
    par = True
else:
    impar = True

#dica de digitos
digitos = str(CODIGO)
digitos = len(digitos)

#dica de mais ou menos
mais = random.randint(1, 15)
menos = random.randint(1, 15)
mais = CODIGO + mais
menos = CODIGO - menos


while tentativas > 0:
    adivinhe = int(input('adivinhe o codigo: '))
    if adivinhe == CODIGO:
        print('parabens voce desarmou a bomba!!!!!!')
        break
    else:
        if adivinhe > CODIGO:
            print('chute mais baixo')
        else:
            print('chute mais alto')
        time.sleep(1)
        tentativas -= 1
        print(f'numero de tentativas: {tentativas}')
        if tentativas == 3:
            if par:
                print('DICA: o numero e par')
            else:
                print('DICA: o numero e impar')
        elif tentativas == 2:
            print(f'DICA: numero de digitos: {digitos}')
        elif tentativas == 1:
            print (f'DICA: o codigo esta entre: {menos} e {mais}')
if tentativas == 0:
    print(F'BOMMMMMMMMMM, o codigo era: {CODIGO}')