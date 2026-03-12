alunos = []

while True:
	print("1 - Cadastrar Aluno")
	print("2 - Mostrar Resultados")
	print("3 - Sair")
	
	while True:
		try:
			menu = int(input("digite: "))
			if menu in (1, 2, 3):
				break
			else:
				print("ação invalida")
		except ValueError:
			print("ação invalida")
			
	def cadastrar_aluno():
		try:
			while True:
				aluno_nome = input("digite o nome do aluno: ")
				if aluno_nome != " ":
					break
				else:
					print("nome não pode ser vazio")
			while True:
				aluno_nota1 = float(input("digite a nota 1: "))
				if aluno_nota1 >= 0 and aluno_nota1 <= 10:
					break
				else:
					print("nota precisa ser maior que 0 e menor que 10")
			while True:
				aluno_nota2 = float(input("digite a nota 2: "))
				if aluno_nota2 >= 0 and aluno_nota2 <= 10:
					break
				else:
					print("nota precisa ser maior que 0 e menor que 10")
					
			novo_aluno = {"nome": aluno_nome, "nota1": aluno_nota1, "nota2": aluno_nota2}
			alunos.append(novo_aluno)
			print(f"Aluno(a): {aluno_nome} Cadastrado")
		except ValueError:
			print("ação invalida ")
		
	def mostrar_resultados():
		if len(alunos) == 0:
			print("Não há alunos")
		else:
			for aluno in alunos:
				media = (aluno['nota1'] + aluno['nota2']) / 2
				if media < 6:
					status = "Reprovado"
				else:
					status = "Aprovado"
				print(f"Nome: {aluno['nome']} | Status: {status} | Média: {media:.2f}")
			
	if menu == 1:
		cadastrar_aluno()
	elif menu == 2:
		mostrar_resultados()
	elif menu == 3:
		print("PROGRAMA FINALIZADO")
		break
