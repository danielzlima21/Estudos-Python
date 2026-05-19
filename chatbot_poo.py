consultas = []

class AgendarConsulta:
    def __init__(self, nome, numero, dia, horario):
        self.nome = nome
        self.numero = numero
        self.dia = dia
        self.horario = horario

def salvar_consulta():
    try:
        nome = input('digite o nome: ')
        numero = int(input('digite o numero: '))
        dia = int(input('digite o dia: '))
        horario = input('digite o horario: ')
        nova_consulta = AgendarConsulta(nome, numero, dia, horario)
        consultas.append(nova_consulta)
        print(f'{nome}, Sua consulta foi criada para o dia {dia} as {horario}')
    except ValueError:
        print('algo deu errado')

def mostrar_consultas():
    if not (consultas):
        print('não há consultas')
    else:
        print('CONSULTAS')
        for consulta in consultas:
            print(f'{consulta.nome}, {consulta.numero}, Dia: {consulta.dia}, Horário: {consulta.horario}')

while True:
    print('1 - Adicionar Consulta')
    print('2 - Ver consultas')
    print('3 - Sair')

    while True:
        try:
            menu = int(input('Digite: '))
            if menu not in(1, 2, 3):
                print('Algo deu errado')
            elif menu == 1:
                salvar_consulta()
            elif menu == 2:
                mostrar_consultas()
            elif menu == 3:
                print('Programa encerrado')
                break
        except ValueError:
            print('Algo deu errado')