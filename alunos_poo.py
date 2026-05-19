class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media

    def status(self):
        return 'aprovado' if self.calcular_media() >= 7 else 'reprovado'

def restantes():
    global n
    n += 1
    print(f'({n}/{qtd})')

qtd = int(input('digite a quantidae de alunos: '))
alunos = []

n = 0
for aluno in range(qtd):
    restantes()
    nome = input('digite o nome do aluno: ')

    while True:
        nota1 = int(input(f'digite a nota 1 de {nome}: '))
        if nota1 >= 0 and nota1 <= 10:
            break
        else:
            print(f'{nota1} deve estar entre 0 e 10')

    while True:
        nota2 = int(input(f'digite a nota 2 de {nome}: '))
        if nota2 >= 0 and nota2 <= 10:
            break
        else:
            print(f'{nota2} deve estar entre 0 e 10')

    aluno = Aluno(nome, nota1, nota2)
    alunos.append(aluno)
    print('=' * 30)

total_alunos = len(alunos)
total_alunos_aprovados = 0
total_alunos_reprovados = 0

for aluno in alunos:
    media = aluno.calcular_media()
    status = aluno.status()

    print(f'{aluno.nome} sua media é {media} | {status}')

    if status == 'aprovado':
        total_alunos_aprovados += 1
    else:
        total_alunos_reprovados += 1

print(f'o total de alunos é: {total_alunos}')
print(f'o total de alunos aprovados é: {total_alunos_aprovados}')
print(f'o total de alunos reprovados é: {total_alunos_reprovados}')