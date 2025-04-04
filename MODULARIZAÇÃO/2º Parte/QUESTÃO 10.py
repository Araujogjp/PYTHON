# CRIAR A FUNÇÃO AQUI:
# QY=UESTÃO 7 DA LISTA 
def calculadora(n1, n2, opcao):
  if(opcao == 1):
    return n1 + n2
  elif(opcao == 2):
    return n1 - n2
  elif(opcao == 3):
    return n1 * n2
  elif(opcao == 4):
    return n1 / n2
  elif(opcao == 5):
    return n1 % n2
  else:
    return n1 // n2


# MENU: REUSABILIDADE
q = 0
while(q < 5):
  try:
    q += 1
    n1 = int(input(f'{q}º NÚMERO: '))
    if(n1 < 0):
      print('N1 TEM QUE SER POSITIVO')
    else: 
      n2 = int(input(f'{q}º NÚMERO: '))
      if(n2 < 0):
        print('N2 TEM QUE SER POSITIVO')
      else:
        print('[1] PARA SOMAR')
        print('[2] PARA SUBTRAIR')
        print('[3] PARA MULTIPLICAR')
        print('[4] PARA DIVIDIR')
        print('[5] PARA MOD')
        print('[6] PARA DIV')
        opcao = int(input('QUAL SUA OPÇÃO?: '))
        if(opcao < 1 or opcao > 6):
          print('ERRO DE ENTRADA [1, 6]')
        else:
          mini = calculadora(n1, n2, opcao)
          print(f'{mini:.2f}')
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO {ERRO_EXCECAO}')
