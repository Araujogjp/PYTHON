# CRIAR A FUNÇÃO AQUI:
# QUESTÃO 19 DA LISTA
def triangulo(a, b, c):
  if(a < b + c and b < a + c and c < a + b):
    if(a == b and a == c):
      return 3
    elif(a == b or b == c or a == c):
      return 2
    else:
      return 1
  else:
    return 0 


# MENU: REUSABILIDADE
print('Verificação de Triângulo')
print('Condição obrigatória: É triângulo se, somente se (A < B + C) e (B < A + C) e (C < A + B).')
print('Triângulo Escaleno = 0 lados iguais')
print('Triângulo Isósceles = 2 lados iguais')
print('Triângulo Equilátero = 3 lados iguais')
a = int(input('Digite o valor de a: '))
if(a < 0):
  print('O lado A deve ser maior que 0')
else: 
  b = int(input('Digite o valor de b: '))
  if(b < 0):
    print('O lado B deve ser maior que 0')
  else:
    c = int(input('Digite o valor de c: '))
    if(c < 0):
      print('O lado C deve ser maior que 0')
    else:
      verificacao = triangulo(a, b, c)
      if(verificacao == 0):
        print('Não é um triângulo')
      else: 
        print('É um Triângulo')
        if(verificacao == 3):
          print('É um Triângulo Equilátero')
        elif(verificacao == 2):
          print('É um Triângulo Isósceles')
        else:
          print('É um Triângulo Escaleno')
