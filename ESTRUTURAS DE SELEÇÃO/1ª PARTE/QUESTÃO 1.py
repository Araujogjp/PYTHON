import math
try:
  r = float(input('Digite o valor de r:  '))
  if(r<=0):
    print('O valor de r deve ser maior que 0')
  else:
    area = 4 * math.pi * (r**2)
    volume = (4/3) * math.pi * (r**3)
    print(f'O valor da área é de: {area:.2f}')
    print(f'O valor do volume é de: {volume:.2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} ')
