cartoes = []
usuarios = []

while True:
    print("1 - registrar usuario")
    print("2 - ver usuarios")
    print("3 - solicitar cartão")
    print("4 - ver cartões")

    while True:
        menu = int(input('digite: '))
        if menu in(1, 2, 3, 4):
            break
        else:
            print('ação inválida')

    if menu == 1:
        user_name = input('registre seu nome de usuario: ')
        user_password = input('registre sua senha: ')
        user_salary = float(input('registre seu salário: '))
        if user_salary >= 800:
            get_card = True
        else:
            get_card = False
        new_user = {'nome': user_name, 'senha': user_password, 'salario': user_salary, 'cartao_disponivel': get_card}
        usuarios.append(new_user)
        print(f'{user_name} Foi adicionado ao sistema')

    elif menu == 2:
        for user in usuarios:
            print(f'{user["nome"]} | {user["senha"]} | {user["salario"]}')
            if user["cartao_disponivel"] == True:
                credito_disponivel = user["salario"] / 2
                print(f'solicitação de cartao disponivel com {credito_disponivel}$ de credito')
            elif user["cartao_disponivel"] == False:
                print('cartão não disponivel')
            print('=' * 30)

    elif menu == 3:
        try_username = input('digite seu nome de usuario: ')
        try_password = input('digite sua senha de usuario: ')
        encontrado = False
        for usuario in usuarios:
            if usuario['nome'] == try_username and usuario['senha'] == try_password:
                encontrado = True
                if usuario['cartao_disponivel'] == True:
                    credito_disponivel = user["salario"] / 2
                    print(f'cartao adicionado no nome de: {usuario["nome"]} com: {credito_disponivel}$ de credito')
                    cartao = {'titular': usuario["nome"], 'senha': usuario["senha"], 'limite': credito_disponivel}
                    cartoes.append(cartao)
                elif usuario['cartao_disponivel'] == False:
                    print('ainda não é possivel solicitar um cartão')
                    break
            else:
                print('usuario ou senha incorretos')
                break
        if encontrado == False:
            print('algo deu errado')

    elif menu == 4:
        if not cartoes:
            print('não há cartões')
        else:
            for cartao in cartoes:
                print(f'Titular: {cartao["titular"]} | Senha: {cartao["senha"]} | Limite: {cartao["limite"]}')