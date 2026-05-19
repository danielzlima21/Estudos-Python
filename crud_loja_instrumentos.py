instrumentos = []

def adicionar_instrumento():
    id = len(instrumentos) + 1
    instrumento_nome = input('digite o nome do instrumento: ')
    instrumento_valor = float(input('digite o valor do instrumento: '))
    novo_instrumento = {'id': id, 'nome': instrumento_nome, 'valor': instrumento_valor}
    instrumentos.append(novo_instrumento)

def ver_instrumentos():
    if not instrumentos:
        print('Não instrumentos')
    else:
        for i in instrumentos:
            print(f'ID: {i["id"]} | Nome: {i["nome"]} | Valor: {i["valor"]}')

def atualizar_instrumento():
    if not instrumentos:
        print('não instrumentos')
    else:
        id_editar = int(input('Digite o ID: '))
        encontrado = False
        for i in instrumentos:
            if i["id"] == id_editar:
                encontrado = True
                novo_nome = input('Digite o novo nome: ')
                novo_valor = float(input('Digite o novo valor: '))
                i["nome"] = novo_nome
                i["valor"] = novo_valor
                break
        if encontrado == False:
            print('instrumento nao encontrado')

def deletar_instrumento():
    if not instrumentos:
        print('não instrumentos')
    else:
        id_deletar = int(input('Digite o ID: '))
        encontrado = False
        for i in instrumentos:
            if i["id"] == id_deletar:
                encontrado = True
                instrumentos.remove(i)
                break
        if encontrado == False:
            print('instrumento nao encontrado')

while True:
    print('1 - === Adicionar instrumento ===')
    print('2 - === Ver instrumentos ===')
    print('3 - === Atualizar instrumento ===')
    print('4 - === Deletar instrumento ===')
    print('5 - === Sair ===')

    while True:
        menu = int(input('Digite: '))
        if menu in(1, 2, 3, 4, 5):
            break
        else:
            print('Ação inválida')
    
    if menu == 1:
        adicionar_instrumento()
    elif menu == 2:
        ver_instrumentos()
    elif menu == 3:
        atualizar_instrumento()
    elif menu == 4:
        deletar_instrumento()
    elif menu == 5:
        print('PROGRAMA FINALIZADO')
        break