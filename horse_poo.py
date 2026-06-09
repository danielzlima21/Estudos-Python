class Cavalo:
    def __init__(self, nome, confianca, confianca_max, domar):
        self.nome = nome
        self.confianca = confianca
        self.confianca_max = confianca_max
        self.domar = domar

    def domesticar(self):
        if self.confianca < self.confianca_max:
            self.confianca += 1
            print(f'confiança atual ({self.confianca}/{self.confianca_max})')
        else:
            print('confiança maxima')

    def montar(self):
        if self.confianca >= self.domar:
            print(f'você montou no {self.nome}')
        else:
            print(f'{self.nome} rejeitou')

cavalo1 = Cavalo('Cartaz', 0, 10, 7)

while True:
    print('1 - alimentar' \
    '2 - montar' \
    '3 - sair')

    while True:
        menu = int(input('digite: '))

        if menu in (1, 2, 3):
            break
        else:
            print('opção inválida')

    if menu == 1:
        cavalo1.domesticar()
    elif menu == 2:
        cavalo1.montar()
    elif menu == 3:
        print('saindo')
        break