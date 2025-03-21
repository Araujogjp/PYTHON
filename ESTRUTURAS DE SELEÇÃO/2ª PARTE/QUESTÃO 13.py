PHI = 1.61803398875
limite_i = 10 * PHI
limite_f = 200 * PHI
try:
  a = float(input('Digite qualquer número:'))
  b = float(input('Digite qualquer número:  '))
  c = float(input('Digite qualquer número: '))
  media = ((a+b+c)/3)
  if(media< limite_i or media > limite_f):
    media_f = media ** 3
    print(f'A média ao cubo é de: {media_f:.5f}')
  else:
    print(f'A média é de: {media:.5f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} )
