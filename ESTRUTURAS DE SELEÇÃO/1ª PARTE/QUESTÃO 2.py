try:
  b = float(input("Digite o valor da base(em cm):  "))
  h = float(input('Digite o valor da altura(em cm):'))
  if (b <= 0 or h <= 0):
    print('O valor da base e da altura devem ser maiores que 0')
  else:
    perimetro = 2 * b + 2 * h
    p = perimetro / 2.54
    j = p * 0.03
    print(f'O valor do perimetro em polegadas é: {p:.2f}')
    print(f'o valor do perimetro em cm é: {perimetro:.2f}')
    print(f'O valor do perimetro em jardas é: {j:.2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} ')
