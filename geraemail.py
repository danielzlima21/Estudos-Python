nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
nome_empresa = input('Digite o nome da empresa: ')

email = (nome + '.' + sobrenome + '@' + nome_empresa + '.com.br').replace(' ', '').lower()
print(email)