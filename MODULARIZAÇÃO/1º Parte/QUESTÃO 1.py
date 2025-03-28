# CRIAR A FUNÇÃO AQUI:
# QUESTÃO 3 DA LISTA
# CRIAR A FUNÇÃO AQUI:
import math 
def arranjo(n, p): 
  return  math.factorial(n) / (math.factorial(n - p))

def combinacao(n, p):
  return arranjo(n,p) / math.factorial(p)


# MENU: REUSABILIDADE
try: 
   n = int(input('DIGITE QUALQUER NÚMERO: '))
   p = int(input('DIGITE QUALQUER NÚMERO: '))
   if(n < 0 or p < 0 or n < p):
    print('VALORES INVALIDOS')
   else:
    print(f'O VALOR DO ARRANJO FOI DE: {arranjo(n,p)}')
    print(f'O VALOR DA COMBINÇÃO FOI DE: {combinacao(n,p)}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} ')
