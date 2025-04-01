# CRIAR A FUNÇÃO AQUI:
# QUESTÃO 17 DA LISTA
def publico(c, j, a):
  return c + j + a 

def valor_total(valor, j, a, d):
  valor_j = j * (valor / 2)
  valor_a = (a - d) * valor
  valor_d = d * (valor / 2)
  return valor_j + valor_a + valor_d


# MENU: REUSABILIDADE
print('Crianças abaixo de 10 anos não pagam')
print('Jovens de 11 a 17 pagam 1⁄2 entrada')
print('Acima dos 18 anos paga 1⁄2 entrada se doarem um quilo de alimento não perecível.')
try:
  valor = int(input('Qual o valor de entrada?: '))
  if(valor < 0):
    print('O valor deve ser >= 0')
  else: 
    c = int(input('Quantas crianças de <= 10 anos assitiram o jogo?: '))
    if(c < 0):
      print('O número de crianças que assistiram o jogo deve ser >= 0')
    else:
      j = int(input('Quantos jovens de 11 a 17 anos assistiram o jogo?: '))
      if(j < 0):
        print('O número de jovens que assistiram o jogo deve ser >= 0')
      else:
        a = int(input('Quantos adultos de >= 18 anos assistiram o jogo?: '))
        if(a < 0):
          print('O número de adultos que assistiram o jogo deve ser >= 0')
        else:
          d = int(input('Quantos adultos doaram mais 1 de kg de comida?: '))
          if(d < 0 or d > a):
            print('O número de doadores que assitiram o jogo deve ser >= 0 e o números de doadores deve ser <= a')
          else:
            print(f'O público total foi de: {publico(c , j, a)}')
            print(f'A arrecadação total foi de: {valor_total(valor, j, a, d):.2f}R$')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} ')
