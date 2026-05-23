#mensagem de error caso a caixa de mensagens esteja vazia, mensagem e enviada mas mostra erro

usuarios = []

def criar_conta():
    u_nome = input('Digite o nome de usuario: ')
    u_senha = input('Digite sua senha: ')
    novo_usuario = {'nome': u_nome, 'senha': u_senha, 'caixa': []}
    usuarios.append(novo_usuario)

def logar():
    verificar_nome = input('Digite seu nome de usuario: ')
    verificar_senha = input('Digite sua senha: ')
    usuario_logado = False
    for u in usuarios:
        if verificar_nome == u['nome'] and verificar_senha == u['senha']:
            usuario_logado = True
            print(f'=== Olá, {u["nome"]} ===')
            print('1 - enviar email')
            print('2 - ver caixa')
            print('3 - logout')

            while True:

                while True:
                    menu = int(input('Digite: '))
                    if menu in (1, 2 ,3):
                        break
                    else:
                        print('Ação inválida!')
                
                if menu == 1:
                    enviar_para = input('digite o nome do remetente: ')
                    usuario_encontrado = False
                    for u_receber in usuarios:
                        if u_receber['nome'] == enviar_para and u_receber['nome'] != u['nome']:
                            usuario_encontrado = True
                            mensagem = input('Digite a mensagem: ')
                            u_receber['caixa'].append(mensagem)
                        else:
                            print('usuario não encontrado ou nao é possivel enviar mensagem a si mesmo')
                            break
                    if usuario_encontrado == False:
                        print('Usuario não encontrado!')
                        
                elif menu == 2:
                    print(f'=== CAIXA DE MENSAGEMS DE {u["nome"]} ===')
                    for mensagem in u['caixa']:
                        print(mensagem)
                        print()

                elif menu == 3:
                    print('=== FAZENDO LOGOUT ===')
                    break                     
        else:
            print('Nome ou senha incorretos')
    if usuario_logado == False:
        print('Usuario não encontrado')

def mostrar_menu():
    while True:
        print('1 - Criar conta')
        print('2 - Logar')
        print('3 - Sair')

        while True:
            menu = int(input('Digite: '))
            if menu in (1, 2, 3):
                break
            else:
                print('Acção inválida')
        
        if menu == 1:
            criar_conta()
        elif menu == 2:
            logar()
        elif menu == 3:
            print('PROGRAMA FINALIZADO')
            break

mostrar_menu()