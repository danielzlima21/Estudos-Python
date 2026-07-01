class Console:
    def __init__(self, nome, armazenamento, ram,):
        self.nome = nome
        self.armazenamento = armazenamento
        self.ram = ram
        self.biblioteca = []

    def instalar_arquivo(self, arquivo):
        self.arquivo = arquivo

        if '.sys' in arquivo.nome:
            print('um arquivo de sistema foi indentificado')
            if self.armazenamento < arquivo.tamanho:
                print(f'não há espaço para instalar o arquivo. Espaço atual: {self.tamanho}, Tamanho do arquivo: {arquivo.tamanho}')
            else:
                self.armazenamento -= arquivo.tamanho
                #self.ram += arquivo.aumentar_ram(self.ram)
                self.biblioteca.append(arquivo)
                print('instalação concluida')



    def desinstalar_jogo(self, arquivo):
        self.arquivo = arquivo

    def abrir_jogo(self, jogo):
        self.jogo = jogo

    def rodar_jogo(self, jogo):
        self.jogo = jogo

class Jogo:
    def __init__(self, nome, tamanho, ram):
        self.nome = nome
        self.tamanho = tamanho
        self.ram = ram

    def mostrar_info(self):
        pass

class Sistema:
    def __init__(self, nome, tamanho, ram):
        self.nome = nome
        self.tamanho = tamanho
        self.ram = ram

    def aumentar_ram(self, console):
        #console.ram += self.ram
        pass

playstation = Console('ps4', 100, 100)
windows = Sistema('win.sys', 10, 10)

playstation.instalar_arquivo(windows)