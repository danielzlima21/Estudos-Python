carrinho = []
desconto = 0

while True:
	print("1 adicionar produtos")
	print("2 nota fiscal")
	
	while True:
		try:
			menu = int(input("Digite: "))
			if menu in (1, 2):
				break
			else:
				print("digite um número válido")
		except ValueError:
			print("Digite apenas números")
			
	if menu == 1:
		while True:
			print("1 informar produto")
			print("2 sair")
			print("=" * 32)
			acao = int(input("digite: "))
			if acao == 2:
				break
			else:
				produto_nome = input("digite o nome do produto: ")
				produto_valor = float(input("digite o valor: "))
				novo_produto = {"nome": produto_nome, "valor": produto_valor}
				carrinho.append(novo_produto)
				
	elif menu == 2:
		desconto = 0
		if len(carrinho) == 0:
			print("não há produtos")
		else:
			subtotal = sum(produto['valor'] for produto in carrinho)
			
			if subtotal > 200:
				desconto = subtotal * 20 / 100
			
			elif subtotal > 100:
				desconto = subtotal * 10 / 100
			
			total_final = subtotal - desconto
			
			print(f"Quantidade de produtos: {len(carrinho)}")
			for produto in carrinho:
				print(f"{produto['nome']} | R$ {produto['valor']}")
			print("=" * 32)
			print(f"Subtotal: R$ {subtotal:.2f}")
			print(f"Desconto: R$ {desconto:.2f}")
			print(f"Total final: R$ {total_final:.2f}")
