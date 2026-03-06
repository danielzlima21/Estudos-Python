class Veiculo:
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
	
	def buzinar(self):
		print("Carro: Bibibi")
		
class Moto(Veiculo):
	def __init__(self, marca, modelo, cilindrada):
		super().__init__(marca, modelo)
		self.cilindrada = cilindrada
			
	def empinar(self):
		print("Grau")
		
	def detalhes(self):
		print(self.marca, self.modelo, self.cilindrada)
		
	def buzinar(self):
		print("Moto: bi-bi")
		
class Caminhao(Veiculo):
		def buzinar(self):
			print("Caminhão: FOM!")
		
meu_carro = Veiculo("Honda", "Civic")
minha_moto = Moto("Kawasaki", "ninja", "100")
meu_caminhao = Caminhao("Scania", "r450")

veiculos = [meu_carro, minha_moto, meu_caminhao]

for veiculo in veiculos:
	veiculo.buzinar()
