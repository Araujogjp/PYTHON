import numpy as np
# VARIÁVEIS
n = 0.0 # DIGITAR NÚMEROS
q = 0 # ENUMERAR
menor = np.inf
parar = 0
print('Digite somente números positivos ou digite [0] para encerrar o programa')
try: 
  while True: 
    q += 1
    n = float(input(f'{q}ª Número: '))
    if(n < 0):
      print('Os números devem ser todos positivos e maiores que 0')
      q -= 1
    if(n == 0):
      parar += n
      print('FIM DO PROGRAMA')
      break
    if(n < menor):
      menor = n
  if(menor != np.inf): 
    print(f'O menor número foi: {menor: .2f}')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
