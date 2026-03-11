import requests

class BuscadorEndereco:

    def __init__(self, cep):
        self.cep = cep

    def consultar_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()

            if "erro" not in dados:
                print(f"Logradouro: {dados['logradouro']}")
                print(f"Bairro: {dados['bairro']}")
                print(f"Cidade: {dados['localidade']} - {dados['uf']}")
            else:
                print("⚠️ CEP não encontrado.")
        else:
            print("⚠️ Erro na conexão com o servidor.")


num_cep = input("Digite o CEP (apenas números): ")

cep_usuario = BuscadorEndereco(num_cep)
cep_usuario.consultar_cep()
