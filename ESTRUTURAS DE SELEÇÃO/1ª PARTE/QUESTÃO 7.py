try:
  preco = float(input('Digite o valor da mercadoria:'))
  reajuste = float(input('Digite  valor do reajuste: '))
  if(preco < 0 or reajuste < 0):
    print('O valor do preço e do reajuste devem ser maiores que 0')
  else:
    identificador = int(input('Digite o número [1] se você quer um acrescimo no valor ou digite o número [2] caso queira um desconto: '))
    if(identificador != 1 and identificador != 2):
      print('Digite o número [1] para acréscimo no valor ou digite o número [2] para desconto')
    else:
      if(identificador == 1):
        preco_reajustado = preco + (preco * reajuste / 100)
        print(f'o novo valor da mercadoria com o acréscimo é de: {preco_reajustado:.2f}')
      else:
        preco_reajustado = preco - (preco * reajuste / 100)
        print(f'o novo valor da mercadoria com o desconto é de: {preco_reajustado:.2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO:  ERRO_EXCECAO ')
