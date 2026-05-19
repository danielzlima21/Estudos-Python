class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"Venda realizada: {quantidade}x {self.nome}")
        else:
            print("Estoque insuficiente")

    def repor(self, quantidade):
        self.estoque += quantidade


class Loja:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for p in self.produtos:
            print(f"{p.nome} - R${p.preco} - Estoque: {p.estoque}")

    def buscar_produto(self, nome):
        for p in self.produtos:
            if p.nome == nome:
                return p
        return None


loja = Loja()

while True:
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Sair")

    opcao = int(input("Digite: "))

    if opcao == 1:
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        loja.adicionar_produto(Produto(nome, preco, estoque))

    elif opcao == 2:
        loja.listar_produtos()

    elif opcao == 3:
        nome = input("Digite o nome do produto: ")
        produto = loja.buscar_produto(nome)

        if produto:
            qtd = int(input("Quantidade: "))
            produto.vender(qtd)
        else:
            print("Produto não encontrado")

    elif opcao == 4:
        break