# QUESTÃO 1 DA LISTA

import math
k = math.pi
p = math.e 
def f_a(n):
  return k / (math.factorial(int(n)) + k)

def f_b(n):
  return ((k ** n) - k) / (p * n)

def soma(n):
  return f_b(n) + f_a(k)

def media(n):
  return soma(n) / 2

try:
  n = float(input('Digite o valor de n: '))
  funcao_a = f_a(n)
  funcao_b = f_b(n)
  soma_termos = soma(n)
  media_termos = media(n)
  print(f'O VALOR DA FUNÇÃO A É: {funcao_a:.2f}')
  print(f'O VALOR DA FUNÇÃO B É: {funcao_b:.2f}')
  print(f'A SOMA É {soma_termos: .2f}')
  print(f'A MÉDIA É: {media_termos: .2f}')
except Exception as ERRO_EXCECAO: 
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} ')
