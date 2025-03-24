import math
# VARIÁVEIS
n = 0.0
media = 0.0
soma = 0.0
q = 0
print('Digite um número que esteja no intervalo de 10 * pi e 100 * pi / Digite um número fora do intervalo para parar o programa')
try:
  while True:
    q += 1
    n = float(input(f'{q}º NÚMERO: '))
    if( n >= 10 * math.pi and n <= 100 * math.pi):
      soma += n
    else: 
      if(n != 10 * math.pi and n != 100 * math.pi):
        print('FIM DO PROGRAMA')
        q -= 1
        break
  media = soma / q
  if(media > 0):  
    print(f'A média foi de: {media: .2f}')
  else:
    print('O NÚMERO DIGITADO ESTÁ FORA O INTERVALO')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} ')
