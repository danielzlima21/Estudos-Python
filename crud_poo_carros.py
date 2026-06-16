import random
carros = []

class Carro:
    def __init__(self, nome, marca, placa, valor):
        self.nome = nome
        self.marca = marca
        self.placa = placa
        self.valor = valor

def adicionar_carro():
    nome = input('Digite o nome do carro: ')
    marca = input('Digite a marca do carro: ')

    while True:
        placa = input('Digite a placa: ')

        if any(carro.placa == placa for carro in carros):
            print('Esta placa já está em uso!')
        else:
            break

    valor = int(input('Digite o valor do carro: '))
    novo_carro = Carro(nome, marca, placa, valor)
    carros.append(novo_carro)

def listar_carros():
    if not carros:
        print('Não há carros!')
    else:
        for carro in carros:
            print(f'{carro.nome}')
            print(f'{carro.marca}')
            print(f'{carro.placa}')
            print(f'{carro.valor}$')
            print('=' * 32)

def atualizar_carro():
    if not carros:
        print('Não há carros!')
    else:
        placa_carro_editar = input('Digite a placa do carro: ')
        encontrado = False

        for carro in carros:
            if carro.placa == placa_carro_editar:
                encontrado = True
                novo_nome = input('Digite o nome do carro: ')
                nova_marca = input('Digite a marca do carro: ')

                while True:
                    nova_placa = input('Digite a placa: ')

                    if any(carro.placa == nova_placa for carro in carros):
                        print('Esta placa já está em uso!')
                    else:
                        break

                novo_valor = int(input('Digite o valor do carro: '))

                carro.nome = novo_nome
                carro.marca = nova_marca
                carro.placa = nova_placa
                carro.valor = novo_valor
                break
        if encontrado == False:
            print('Carro não encontrado!')

def deletar_carro():
    placa_carro_deletar = input('Digite a placa do carro: ')
    encontrado = False

    for carro in carros:
        if carro.placa == placa_carro_deletar:
            encontrado = True
            carros.remove(carro)
    if encontrado == False:
        print('Carro não encontrado!')
