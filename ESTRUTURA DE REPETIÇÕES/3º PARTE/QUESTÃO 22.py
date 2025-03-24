# VARIÁVEIS
temperatura = 0.0
media = 0.0
soma = 0.0
q = 0
while True:
  try:
    q += 1
    temperatura = float(input(f'Temperatura do {q}º Dia: '))
    if(temperatura >= - 15 and temperatura <= 5):
      soma += temperatura 
      media = soma / q
    else: 
      print('FIM DO PROGRAMA')
      break
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
if(media == 0):
  print('A temperatura está fora do intervalo')
else:
  print(f'A média de temperatura foi de: {media: .2f}')
