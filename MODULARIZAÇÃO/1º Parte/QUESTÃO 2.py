# QUESTÃO 4 DA LISTA 
# CRIAR A FUNÇÃO AQUI: 
def ano(ano):
    if(ano % 400 == 0):
      return 1
    elif(ano % 4 == 0 and ano % 100 != 0):
      return 1
    else:
      return 0
      
# MENU: REUSABILIDADE
verificao = int(input('INFORME UM ANO: '))
if(verificao < 0):
  print('O ANO TEM QUE SER MAIOR QUE 0')
else:
  bissexto = ano(verificao)
  if(bissexto == 0):
    print('O ANO NÃO É BISSEXTO')
  else:
    print('O ANO É BISSEXTO')
