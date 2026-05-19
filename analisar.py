def analisar(texto):
    texto_maiusculo = texto.upper()
    print(f'Texto maiusculo: {texto_maiusculo}')

    texto_sem_espaco = texto.replace(' ', '')
    letras_no_texto = len(texto_sem_espaco)
    print(f'Quantidade de letras no texto: {letras_no_texto}')

    texto_sem_a = texto.replace('a', '@').replace('A', '@')
    print(f'Texto sem as letras (A): {texto_sem_a}')

analisar('Bom Dia')