#criar uma tela de login com tkinter que direciona para uma pagina
#onde voce  pode fazer post de texto e comentarios aleatorios apareceram
#as informações serão guardadas e armazenadas no banco de dados xamp
#um botao para deletar todo o feed ous posts # CRUD

def abstracao():
    USUARIO_CERTO = 'daniel'
    SENHA_CERTA = '123'

    usuario = input('digite o nome de usuario: ')
    senha = input('digite sua senha: ')
    
    if usuario == USUARIO_CERTO and senha == SENHA_CERTA:
        print('login realizado com sucesso')
    else:
        print('usuario ou senha incorretos')

abstracao()