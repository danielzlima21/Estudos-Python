class Carro:
    def __init__(self, nome, gasolina_atual, gasolina_maxima):
        self.nome = nome
        self.gasolina_atual = gasolina_atual
        self.gasolina_maxima = gasolina_maxima

    def dirigir(self, destino, destino_km):# a cada 2km gasta 1 gasolina
        gasto = destino_km / 2
        if self.gasolina_atual < destino_km:
            print('gasolina insuficiente')
        else:
            self.gasolina_atual -= gasto
            print(f'o {self.nome} está indo para {destino}')

    def abastecer(self, quantidade):
        self.gasolina_atual += quantidade
        if self.gasolina_atual >= self.gasolina_maxima:
            self.gasolina_atual = self.gasolina_maxima
            print('tanque cheio')
            print(f'{self.nome} abastecido')

    def status(self):
        print(f'Carro: {self.nome}')
        print(f'Combustível: {self.gasolina_atual}/{self.gasolina_maxima}')

carro1 = Carro('Zentorno', 10, 30)

while True:
    carro1.status()
    print('1 - dirigir')
    print('2 - abastecer')

    while True:
        menu = int(input('digite: '))
        if menu in (1, 2):
            break
        else:
            print('opção inválida')

    if menu == 1:
        destino = input('digite o local: ')
        destino_km = int(input('digite a distancia: '))
        carro1.dirigir(destino, destino_km)
    elif menu == 2:
        quantidade = int(input('digite a quantidade: '))
        carro1.abastecer(quantidade)