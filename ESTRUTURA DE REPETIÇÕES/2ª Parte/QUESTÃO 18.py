# VARIÁVEIS
n = 0
contador = 0
media = 0
print('DICA: PARA UM NÚMERO SER ÍMPAR E MÚLTIPLO DE 7, COMEÇE DO 7 E SEMPRE ADICIONE + 14')
try: 
  while(contador < 100):
    contador += 1
    n = float(input(f'{contador}ª Número -> Digite números ímpares e múltiplos de 7: '))
    if(n % 2 != 0 and n % 7 == 0):
      media += n
    else: 
      print('Os números devem ser ímpares e múltiplos de 7')
      contador -= 1
  media /= contador 
  print(f'A média foi de: {media: .2f}')  
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
