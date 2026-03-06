produtos = []
produto_id = 0

while True:
	print("1 - Cadastrar Produto")
	print("2 - Listar Produtos")
	print("3 - Atualizar Estoque")
	print("4 - Remover Produto")
	print("5 - Relatório e Salvar em txt")
	print("6 - Sair")
	
	while True:
		try:
			menu = int(input("digite: "))
			if menu in (1, 2, 3, 4, 5, 6):
				break
			else:
				print("⚠️ Número inválido")
		except ValueError:
			print("⚠️ Digite apenas números")
			
	def cadastrar_produto():
		global produto_id
		try:
			produto_id += 1
			produto_nome = input("nome do produto: ")
			produto_valor = float(input("valor do produto: "))
			
			while True:
				produto_quantidade = int(input("quantidade do produto: "))
				if produto_quantidade >= 1:
					break
				else:
					print("⚠️ Quantidade não pode ser 0 ou menor")
					
			produto_valor_estoque = produto_valor * produto_quantidade
			
			novo_produto = {"id": produto_id, "nome": produto_nome, "valor": produto_valor, "quantidade": produto_quantidade, "valor_estoque": produto_valor_estoque}
			produtos.append(novo_produto)
		except ValueError:
			print("⚠️ Erro de digitação")
			
	def listar_produtos():
		if len(produtos) < 1:
			print("não ha produtos")
		else:
			print("=== PODUTOS ===")
			for produto in produtos:
				print(f"ID: {produto['id']} | Nome: {produto['nome']} | Valor: {produto['valor']} | Qtd: {produto['quantidade']} Valor em estoque: {produto['valor_estoque']}")
				
	def atualizar_estoque():
			if len(produtos) < 1:
				print("Não há produtos")
			else:
				try:
					id_atualizar = int(input("Digite o ID para atualizar: "))
					encontrado = False
					for produto in produtos:
						if id_atualizar == produto['id']:
							encontrado = True
							while True:
								acao = int(input("1-Adicionar Quantidade | 2-Remover Quantidade: "))
								if acao in (1, 2):
									break
								else:
									print("⚠️ Número inválido")
							if acao == 1:
								while True:
									produto_adicionar_quantidade = int(input("Digite a quantidade para adicionar: "))
									if produto_adicionar_quantidade >= 1:
										break
									else:
										print("⚠️ Quantidade não pode ser negativo")
								produto['quantidade'] += produto_adicionar_quantidade
							elif acao == 2:
								while True:
									produto_remover_quantidade = int(input("Digite a quantidade para remover: "))
									if produto_remover_quantidade >= 1:
										break
									else:
										print("⚠️ Número não pode ser negativo")
								produto['quantidade'] -= produto_remover_quantidade
								break
					if encontrado == False:
						print("⚠️ Produto não encontrado")
				except ValueError:
							print("⚠️ Erro de digitação")
							
	def remover_produto():
		if len(produtos) < 1:
			print("Não há produtos")
		else:
			try:
				id_remover = int(input("Digite o ID para remover: "))
				encontrado = False
				for produto in produtos:
					if id_remover == produto['id']:
						encontrado = True
						produtos.remove(produto)
						break
				if encontrado== False:
					print("⚠️ Produto não encontrado")
			except ValueError:
				print("⚠️ Erro de digitação")
		
	def relatorio_e_salvar():
		if len(produtos) < 1:
			print("Não há produtos")
		else:
			with open("estoque.txt", "w") as arquivo:
				for p in produtos:
					linha = f"{p['id']};{p['nome']};{p['valor']};{p['quantidade']}\n"
					arquivo.write(linha)
		
			try:
				print("=== RELATÓRIO DE ESTOQUE ===")
				for produto in produtos:
					total_itens = sum(produto['quantidade'] for produto in produtos)
				for produto in produtos:
					total_valor = sum(produto['valor_estoque'] for produto in produtos)
					
					print(f"ID: {produto['id']}, {produto['nome']}, R$: {produto['valor']}, qtd: {produto['quantidade']}, Total: {produto['valor_estoque']},")
					
				print("")
				print(f"TOTAL DE ITENS: {total_itens}")
				print(f"VALOR TOTAL EM ESTOQUE: {total_valor}")
			except ValueError:
				print("⚠️ Erro de digitação")
				
	if menu == 1:
		cadastrar_produto()
	elif menu == 2:
		listar_produtos()
	elif menu == 3:
		atualizar_estoque()
	elif menu == 4:
		remover_produto()
	elif menu == 5:
		relatorio_e_salvar()
	else:
		print("Programa finalizado")
		break
