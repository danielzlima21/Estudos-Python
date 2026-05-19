USUARIO_CORRETO = 'Admin123'
SENHA_CORRETA = '12345'
tentativas = 3

while tentativas > 0:
    usuario = input('digite o nome de usuario: ')
    senha = input('digite a senha: ')

    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        print('Acesso liberado')
        break
    else:
        tentativas -= 1
        print('Usuario ou senha incorretos!')
        print(f'Tentativas restantes: {tentativas}')
if tentativas == 0:
    print('Acesso bloqueado!')