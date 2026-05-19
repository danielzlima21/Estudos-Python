transacoes = []

def cadastrar():
    try:
        transacao_nome = input("Digite o nome da transação: ")
        transacao_valor = int(input("Digite o valor da transação: "))
        transacao_categoria = input("Digite a categoria da transação: ")
        nova_transacao = {"nome": transacao_nome, "valor": transacao_valor, "categoria": transacao_categoria}
        transacoes.append(nova_transacao)
    except ValueError:
        print("Erro de digitação")

def ver_saldo():
    if len(transacoes) == 0:
        print("Nao ha transações")
    else:
        saldo = sum(transacao['valor'] for transacao in transacoes)
        for transacao in transacoes:
            if transacao['valor'] > 0:
                print(f"{transacao['nome']} | {transacao['valor']}$ | {transacao['categoria']}")
            elif transacao['valor'] <= 0:
                print(f"{transacao['nome']} | {transacao['valor']}$ | {transacao['categoria']} [!]")
        print(f"Seu saldo: {saldo}$")
        if saldo <= 0:
            print("Cuidado você està no vermelho")

def relatorio_por_categoria():
    if len(transacoes) == 0:
        print("Nao ha transações")
    else:
        try:
            categoria_alvo = input("Digite o nome da categoria: ").lower()
            encontrado = False
            total_gategoria = 0 #valor total da categoria
            print(f"Transações de: {categoria_alvo}")
            for transacao in transacoes:
                if transacao['categoria'].lower() == categoria_alvo.lower():
                    encontrado = True
                    total_gategoria = sum(transacao['valor'] for transacao in transacoes if transacao['categoria'].lower() == categoria_alvo)
                    print(f"{transacao['nome']} | {transacao['valor']} | {transacao['categoria']}")
            if encontrado == True:
                if total_gategoria <= 0:
                    print(f"O total de gastos da categoria: {categoria_alvo} é: {total_gategoria}$")
                else:
                    print("Nao há gastos nesta categoria")
            if encontrado == False:
                print("Categoria não encontrada")
        except ValueError:
            print("Erro de digitação")

def remover_transacao():
    if not transacoes:
        print("Não há transações")
    else:
        try:
            encontrado = False
            print("Todas as transações")
            for i, transacao in enumerate(transacoes):
                print(f"{i} - {transacao['nome']} - {transacao['valor']}")

            transacao_remover = int(input("Digite o numero para remover: "))
            for i, transacao in enumerate(transacoes):
                if transacao_remover == i:
                    encontrado = True
                    transacoes.pop(i)
                    print(f"{transacao['nome']} de {transacao['valor']}$ Removida")
                    break
            if encontrado == False:
                print("Transação nao encontrada")
        except ValueError:
            print("Erro de digitação")

def editar_transacao():
    if not transacoes:
        print("não há transações")
    else:
        for i, transacao in enumerate(transacoes):
            print(f"{i} - {transacao['nome']} - {transacao['valor']} - {transacao['categoria']}")

        transacao_editar = int(input("digite para editar: "))
        encontrado = False
        for i, transacao in enumerate(transacoes):
            if transacao_editar == i:
                encontrado = True
                print(f"{transacao['nome']} | {transacao['valor']} | {transacao['categoria']}")
                acao = int(input("o que deseja mudar | 1: nome . 2: valor . 3: categoria: "))
                while True:
                    if acao not in(1, 2 ,3):
                        print("acao invalida")
                    else:
                        if acao == 1:
                            novo_nome = input("digite o novo nome:")
                            transacao['nome'] = novo_nome
                        elif acao == 2:
                            while True:
                                novo_valor = int(input("digite o novo valor: "))
                                if novo_valor >= 0:
                                    break
                                else:
                                    print("valor invalido")
                            transacao['valor'] = novo_valor
                        elif acao == 3:
                            nova_categoria = input("digite a nova categoria: ")
                            transacao['categoria'] = nova_categoria
                        break
        if encontrado == False:
            print("transação não encontrada")

def salvar_dados():
    with open("banco_financeiro.txt", "w") as arquivo:
        for t in transacoes:
            linha = f"{t['nome']};{t['valor']};{t['categoria']}\n"
            arquivo.write(linha)
        print("Dados salvos com sucesso")

def carregar_dados():
    try:
        with open("banco_financeiro.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 3:
                    nome, valor, categoria = partes
                    dicionario = {
                        "nome": nome,
                        "valor": int(valor),
                        "categoria": categoria
                    }
                    transacoes.append(dicionario)
            print("Dados carregados da memória")
    except FileNotFoundError:
        print("Arquivo não encontrado")

carregar_dados()
while True:
    print("1 - Cadastrar")
    print("2 - Ver saldo")
    print("3 - Relatorio por categoria")
    print("4 - Remover transação")
    print("5 - Editar transação")
    print("6 - Sair")

    while True:
        try:
            menu = int(input("Digite: "))
            if menu in(1, 2, 3, 4, 5, 6):
                break
            else:
                print("Ação invalida")
        except ValueError:
            print("Erro de digitacão")

    if menu == 1:
        cadastrar()
    elif menu == 2:
        ver_saldo()
    elif menu == 3:
        relatorio_por_categoria()
    elif menu == 4:
        remover_transacao()
    elif menu == 5:
        editar_transacao()
    elif menu == 6:
        salvar_dados()
        print("Programa Finalizado")
        break