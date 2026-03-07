novo_nome = input("digite um nome: ")

with open("meus_dados.txt", "a") as arquivo:
	arquivo.write(novo_nome + "\n")
		
print(f"{novo_nome} foi adicionado sem apagar os anteriores ✔️")


print("=== LENDO NOMES SALVOS ===")
try:
	with open("meus_dados.txt", "r") as arquivo:
		conteudo = arquivo.read()
		print(conteudo)
except FileNotFoundError:
	print("⚠️O arquivo ainda não existe salve algo primeir")
