import random

dia_atual = 0
apostas = 0
saldo = 100
climas = ['sol', 'chuva']

while True:
  dia_atual += 1
  clima_atual = random.choice(climas)
  print(f"dia: {dia_atual}")
  print(f"clima: {clima_atual}")
  print(f"saldo: {saldo}$")

  if apostas == 0:
    while True:
      quer_apostar = input("quer apostar? (s/n): ")
      if quer_apostar in ('s', 'n'):
        break
      else:
        print('digite s ou n')
    if quer_apostar == "n":
      break
    else:
      while True:
        qtd_apostar = int(input('digite a quantidade que quer apostar: '))
        if qtd_apostar <= saldo:
          break
        else:
          print('quantidade nao pode ser maior que o seu saldo')
      saldo -= qtd_apostar
      while True:
        apostar_dia = int(input('se no dia: '))
        if apostar_dia > dia_atual:
          break
        else:
          print('o dia precisa ser maior que o atual')
          print(f'dia atual: {dia_atual}')
      print('=== CLIMAS ===')
      for clima in climas:
        print(clima)
      print('=== === === ===')
      while True:
        apostar_clima = (input('o clima for: '))
        if apostar_clima in climas:
          break
        else:
          print('digite um clima valido')
      aposta_w = qtd_apostar * 2
      print(f'voce recebera: {aposta_w}$')
      apostas += 1
  elif dia_atual == apostar_dia and clima_atual == apostar_clima:
    print(f'voce ganhou a aposta +{aposta_w}$')
    saldo += aposta_w
    print(f'seu saldo: {saldo}$')
    apostas -= 1
  elif dia_atual > apostar_dia:
    print(f'voce perdeu a aposta de: {qtd_apostar}$')
    break
