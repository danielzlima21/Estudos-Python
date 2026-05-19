class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

contatos = []

def adicionar_contato():
    try:
        nome = input('Digite o nome do contato: ')
        numero = int(input('Digite o numero do contato: '))
        novo_contato = Contato(nome, numero)
        contatos.append(novo_contato)
        print(f'{nome} | {numero} Foi adicionado nos contatos')
    except ValueError:
        print('Algo deu errado')

def listar_contatos():
    if not contatos:
        print('Não há contatos')
    else:
        print('=== CONTATOS ===')
        for c in contatos:
            print(f'Nome: {c.nome} | Numero: {c.numero}')

def atualizar_contato():
    try:
        if not contatos:
            print('Não há contatos')
        else:
            alterar = input('digie o nome do contato que deseja alterar: ')
            encontrado = False
            for c in contatos:
                if c.nome.lower() == alterar.lower():
                    encontrado = True
                    print(f'Alterando: {c.nome} | Numero: {c.numero}')
                    while True:
                        escolha = int(input('digite: |1-Mudar Nome| x |2-Mudar Numero|: '))
                        if escolha in(1, 2):
                            break
                        else:
                            print('Algo deu errado')
                    if escolha == 1:
                        novo_nome = input('Digite o novo nome: ')
                        c.nome = novo_nome
                    elif escolha == 2:
                        novo_numero = input('Digite o novo numero: ')
                        c.numero = novo_numero
                    print('Alterações feitas com sucesso')
                    break
            if encontrado == False:
                print('Contato não encontrado')
    except ValueError:
        print('Algo deu errado')

def deletar_contato():
    try:
        if not contatos:
            print('Não há contatos')
        else:
            deletar = input('Digite o nome contanto que deseja deletar: ')
            encontrado = False
            for c in contatos:
                if c.nome.lower() == deletar.lower():
                    encontrado = True
                    contatos.remove(c)
                    print('Contato deletado')
                    break
            if encontrado == False:
                print('Contato não encontrado')
    except ValueError:
        print('Algo deu errado')

while True:
    print('=-' * 30)
    print('1 - Adicionar Contato')
    print('2 - Listar Contato')
    print('3 - Atualizar Contato')
    print('4 - Deletar Contato')
    print('=-' * 30)

    while True:
        try:
            menu =  int(input('Digite: '))
            if menu in (1, 2, 3, 4):
                break
            else:
                print('Algo deu errado')
        except ValueError:
            print('Algo de' \
            'u errado')

    if menu == 1:
        adicionar_contato()
    elif menu == 2:
        listar_contatos()
    elif menu == 3:
        atualizar_contato()
    elif menu == 4:
        deletar_contato()