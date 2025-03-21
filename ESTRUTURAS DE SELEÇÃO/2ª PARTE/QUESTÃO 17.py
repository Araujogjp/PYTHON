try:
  a = float(input('Digite o valor do lado A ='))
  b = float(input('Digite o valor do lado B ='))
  c = float(input('Digite o valor do lado C '))
  if(a <= 0 or b <= 0 or c <= 0):
    print('Todos os lados devem ser maiores que 0')
  else:
    if(a<b+c and b<a+c and c<a+b):
      print('A, B e C FORMAM UM TRIÂNGULO')
      if(a==b and a == c):
        print('O TRIÂNGULO É Equilátero')
      elif ( a==b or a==c or b==c):
        print('O TRIÂNGULO É Isósceles')
      else:
        print('O TRIÂNGULO É Escaleno')
    else:
      print('NÃO É UM TRIÂNGULO')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
