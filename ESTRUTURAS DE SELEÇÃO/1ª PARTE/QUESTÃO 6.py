try:
  n = float(input('Digite um número é igual ou maior que 0:'))
  if(n<0):
    print('O número deve ser maior ou igual a 0')
  else:
    verificar = n ** 2
    if (verificar%2 != 0  and verificar % 11 == 0):
      print(f'o número {verificar:.2f} é impar e múltiplo de 11')
    else:
      print(f'o quadrado de {n:.2f} é {verificar:.2f}, que não atende aos critérios.')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
