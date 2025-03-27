# QUESTÃO 3 DA LISTA
# CRIAR A FUNÇÃO AQUI:
import math 
def arranjo(n, p): 
  if(n < 0 or p < 0 or n < p):
    print('VALORES INVALIDOS')
    return None
  else:
    a = math.factorial(n) / (math.factorial(n - p))
    return a

def combinacao(n, p):
  if(n < 0 or p < 0 or n < p):
    print('VALORES INVALIDOS')
    return None
  else: 
    c = arranjo(n,p) / math.factorial(p)
    return c 

""" 
REUSIBILIDADE
print(arranjo(5,2))
print(combinacao(5,2))
"""
