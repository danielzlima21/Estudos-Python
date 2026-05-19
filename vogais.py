vogais = 'aeiouAEIOU'

def analisar(palavra):
    vogais_na_palavra = 0
    for i in palavra:
        if i in vogais:
            vogais_na_palavra += 1
    consoantes = len(palavra) - vogais_na_palavra
    print(f'Na palavra: {palavra} há: {vogais_na_palavra} vogais e: {consoantes} consoantes')

analisar('carro')