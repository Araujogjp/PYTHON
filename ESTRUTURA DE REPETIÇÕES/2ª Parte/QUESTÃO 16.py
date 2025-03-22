import numpy as np
# VARIAVÉIS
n = 0.0
contador = 0
maiorpar = -1 * np.inf
menorpar = np.inf
maiorimpar = -1 * np.inf
menorimpar = np.inf 
while(contador < 6):
  try: 
    contador += 1
    n = float(input(f'{contador}ª NÚMERO - OBS: ELE TEM Q SER POSITIVO!: '))
    # TRATAMENTO DE ERRO
    if(n < 0):
      print('O NÚMERO TEM QUE SER POSITIVO')
      contador -= 1
    else: 
      if(int(n) % 2 == 0):
        if(n < menorpar):
          menorpar = n
        if(n > maiorpar):
          maiorpar = n
      else:
        if(n < menorimpar):
          menorimpar = n
        if(n > maiorimpar):
          maiorimpar = n
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
if(maiorpar != -1 * np.inf and menorpar != np.inf):
  print(f'O maior número par digitado foi o número: {maiorpar: .2f}')
  print(f'O menor número par digitado foi o número: {menorpar: .2f}')
else:
  print('Nenhum número par foi digitado')
if(maiorimpar != -1 * np.inf and menorimpar != np.inf):
  print(f'O maior número ímpar digitado foi o número: {maiorimpar: .2f}')
  print(f'O menor número ímpar digitado foi o número: {menorimpar: .2f}')
else:
  print('Nenhum número ímpar foi digitado')
