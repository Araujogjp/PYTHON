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

