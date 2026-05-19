class Usuario:
    def __init__(self, nome, senha, salario):
        self.nome = nome
        self.senha = senha
        self.salario = salario
        self.cartao = None

        if self.salario >= 800:
            self.tem_direito_cartao = True
        else:
            self.tem_direito_cartao = False

    def solicitar_cartao(self):
        if self.tem_direito_cartao:
            limite = self.salario / 2
            self.cartao = Cartao(self.nome, limite)
            print(f'{self.nome} seu cartão foi aprovado')
        else:
            print(f'{self.nome} não é possivel solicitar um cartão')

class Cartao:
    def __init__(self, titular, limite):
        self.titular = titular
        self.limite = limite

    def comprar(self, valor):
        if valor <= self.limite:
            self.limite -= valor
            print(f"{self.titular} Compra aprovada! Limite restante: {self.limite}")
            return True
        else:
            print(f'{self.titular} seu saldo é insuficiente')
            return False

teste = Usuario("Daniel", 123, 2500)
teste2 = Usuario("Bob", 222, 100)

teste.solicitar_cartao()
teste2.solicitar_cartao()

teste.cartao.comprar(50)