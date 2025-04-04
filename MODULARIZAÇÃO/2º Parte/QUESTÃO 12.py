# CRIAR A FUNÇÃO AQUI:
# QUESTÃO 9 DA LISTA
def mercadoria(preco, reajuste):
 c_reajuste = preco * (reajuste / 100)
 total = preco - c_reajuste
 return total, c_reajuste


# MENU: REUSABILIDADE
q = 0
while(q < 5):
  try:
    preco = float(input('Digite o preço da mercadoria: '))
    if(preco <= 0):
      print('O preço tem que ser maior que 0')
    else:
      reajuste = float(input('Quanto você quer de reajuste?: '))
      if(reajuste < 0):
        print('O reajuste tem que ser maior ou igual a 0%')
      else:
        preco_final = mercadoria(preco, reajuste)[0]
        reajuste_final = mercadoria(preco, reajuste)[1]
        print(f'O preço final foi de {preco_final:.2f}R$')
        print(f'O reajuste final foi de {reajuste_final:.2f}R$')
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO {ERRO_EXCECAO}')
