#o codigo gera contas aleatorias com seguidores e seguindo aleatorios mas sao reais, gera posts aleatorios com enumerate
# e voce pode seguir estas pessoas no menu tem uma opcao de atualizar o feed e novos posts sao gerados

import random, time

tempo = random.uniform(1, 1)
nomes = ['sam', 'jhon', 'alex', 'nancy', 'bob']
posts = ['ola', 'oi pessoal', 'que belo dia', 'salve', 'como estão']
ias = []
num_ias = random.randint(3, 10)

class Usuario:
    def __init__(self, nome, seguidores, seguindo):
        self.nome = nome
        self.seguidores = seguidores
        self.seguindo = seguindo

    def u_postar(self):
        input(f'{self.nome}: ')
        time.sleep(tempo)

    def ia_postar(self):
        ia_post = random.choice(posts)
        time.sleep(tempo)
        print(f'{self.nome}: {ia_post}')

def criar_conta():
    u_name = input('Digite seu nome de usuario: ')
    return Usuario(u_name, 0, 0)

def criar_ias():
    for ia in range(num_ias):
        ia_name = random.choice(nomes)
        ia = Usuario(ia_name, 0, 0)
        ias.append(ia)

def config():#muda o nome do usuario e a linguagem do site
    pass


def ver_seguidores():#acao minha
    #se voce escolher uma pessoa do feed com o enumerate e quiser ver os seguidores dela
    pass

def ver_seguindo():#acao minha
    #se voce escolher uma pessoa do feed com o enumerate e quiser ver os seguindo dela
    pass

def app():
    user = criar_conta()
    criar_ias()
    while True:
        print(f'=== Olá, {user}')
        print('1 - Postar')
        print('2 - Configurações')
        user.u_postar()
        for ia in ias:
            ia.ia_postar()

app()