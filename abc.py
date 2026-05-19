# import os

# def limpar_terminal():
#     # 'nt' é para Windows, 'posix' para Linux/macOS
#     os.system('cls' if os.name == 'nt' else 'clear')

# # Exemplo de uso
# print("Texto antigo que será apagado...")
# limpar_terminal()
# print("Terminal limpo! Esta é a nova saída.")

import random
palavras = ['abacate', 'banana', 'pera', 'uva', 'acerola', 'jaca', 'melao', 'melancia', 'cadeira', 'mesa', 'sofa', 'elevador', 'ventilador', 'cama', 'estojo', 'chinelo']
frutas = ['abacate', 'banana', 'pera', 'uva', 'acerola', 'jaca', 'melao', 'melancia']
objetos = ['cadeira', 'mesa', 'sofa', 'elevador', 'ventilador', 'cama', 'estojo', 'chinelo']
#tema = [frutas,]
#tema = random.choice([frutas, objetos]random.choice(tema))
#print(tema)

jogo = random.choice(palavras)
tema = None
for palavra in palavras:
    if palavra in frutas and jogo == palavra:
        tema = 'FRUTAS'
        break
    elif palavra in objetos and jogo == palavra:
        tema = 'OBJETOS'
        break
print(palavra, tema)