import math
# CRIAR A FUNÇÃO AQUI:
# QUESTÃO 16 DA LISTA

def area(r):
  return math.pi * (r ** 2)

def volume(r, h): 
  return area(r) * h


# MENU: REUSABILIDADE
try:
  r = float(input('Digite o valor de r: '))
  if(r < 0):
    print('O valor de r deve ser igual ou maior que 0')
  else:
    print(f'A área do círculo é de: {area(r):.3f}')
    h = float(input('Digite o valor de h: '))
    if(h < 0):
      print('O valor de h deve ser maior ou igual a 0')
    else:
      print(f'O volume do cilindro é de: {volume(r, h):.3f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} ')
