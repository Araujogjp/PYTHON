# CRIAR A FUNÇÃO AQUI:
# QUESTÃO 8 DA LISTA
def fibonacci(n):
  ultimo = 0 
  penultimo = 1
  soma = 0
  if(n == 0):
    soma += ultimo
  if(n == 1):
    soma += penultimo
  soma += penultimo
  for i in range(2, n + 1):
    proximo = ultimo + penultimo
    ultimo = penultimo 
    penultimo = proximo
    soma += proximo
  return soma 

# MENU: REUSABILIDADE
n = int(input('DIGITE UM NÚMERO: '))
if(n < 0):
  print('N TEM QUE SER MAIOR OU IGUAL A 0')
else:
  somatorio = fibonacci(n)
  print(f'{somatorio}')
