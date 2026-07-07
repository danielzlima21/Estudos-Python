contas = []

class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depositado: {valor}, Saldo atual: R${self.saldo}')
            self.historico.append(f'Deposito de: {valor}')
        else:
            print('Valor não pode ser menor ou igual á zero!')
        
    def sacar(self, valor):
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            print(f'Saque realizado, Saldo: R${self.saldo}')
            self.historico.append(f'Saque de: R${valor}')
        else:
            print('Saldo insuficiente')
        
    def transferir(self, conta_destino, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f'{self.titular} depositou: {valor}$, para: {conta_destino.titular}')
            self.historico.append(f'Deposito de: R${valor} para: {conta_destino.titular}')
        else:
            print('Saldo insuficiente')

    def mostrar_saldo(self):
        print(f'Titular: {self.titular}, Conta: {self.numero_conta}, Saldo: R${self.saldo}')

    def mostrar_historico(self):
        if not self.historico:
            print('Histórico vazio')
        else:
            for i in self.historico:
                print(i)
                print()
    
def criar_conta():
    nome = input('digite seu nome: ')
    numero_conta  = int(input('digite o numero da sua conta: '))
    nova_conta = ContaBancaria(nome, numero_conta, 0)
    contas.append(nova_conta)

def listar_contas():
    if not contas:
        print('Não há contas!')
    else:
        for conta in contas:
            print(conta.titular)
            print(conta.numero_conta)
            print(conta.saldo)
            print()

def depositar():
    num_da_conta = int(input('Digite o numero da conta: '))
    encontrado = False
    for conta in contas:
        if conta.numero_conta == num_da_conta:
            encontrado = True
            valor = float(input('Digite o valor para depositar: '))
            conta.depositar(valor)
    if encontrado ==  False:
        print('Número não encontrado!')

def sacar():
    num_da_conta = int(input('Digite o numero da conta: '))
    encontrado = False
    for conta in contas:
        if conta.numero_conta == num_da_conta:
            encontrado = True
            valor = float(input('Digite o valor para sacar: '))
            conta.sacar(valor)
    if encontrado ==  False:
        print('Número não encontrado!')

def transferir():
    conta_origem = int(input('digite o numero da conta origem: '))
    valor = float(input('digite o valor: '))
    conta_destino = int(input('digite o numero da conta destino: '))
    origem_encontrado = False
    destino_encontrado = False
    for conta in contas:
        if conta.numero_conta == conta_origem:
            origem_encontrado = True
            conta_origem = conta
        if conta.numero_conta == conta_destino:
            destino_encontrado = True
            conta_destino = conta
        if origem_encontrado and destino_encontrado:
            conta_origem.transferir(conta_destino, valor)
            break
    if destino_encontrado == False:
        print('Conta destino não encontrada')
    if origem_encontrado == False:
        print('Conta origem não encontrada')

def ver_saldo():
    num_da_conta = int(input('Digite o numero da conta: '))
    encontrado = False
    for conta in contas:
        if conta.numero_conta == num_da_conta:
            encontrado = True
            conta.mostrar_saldo()
    if encontrado ==  False:
        print('Número não encontrado!')

def ver_historico():
    num_da_conta = int(input('Digite o numero da conta: '))
    encontrado = False
    for conta in contas:
        if conta.numero_conta == num_da_conta:
            encontrado = True
            conta.mostrar_historico()
    if encontrado ==  False:
        print('Número não encontrado!')
        

def mostrar_menu():
    while True:
        print('1 - Criar conta')
        print('2 - Listar contas')
        print('3 - Depositar')
        print('4 - Sacar')
        print('5 - Transferir')
        print('6 - Ver Saldo')
        print('7 - Ver historico')

        while True:
            menu = int(input('Digite: '))
            if menu in (1, 2, 3, 4, 5, 6, 7) :
                break
            else:
                print('Opção inválida')

        if menu == 1:
            criar_conta()
        elif menu == 2:
            listar_contas()
        elif menu == 3:
            depositar()
        elif menu == 4:
            sacar()
        elif menu == 5:
            transferir()
        elif menu == 6:
            ver_saldo()
        elif menu == 7:
            ver_historico()

def auto_play(bots):
    pass

mostrar_menu()