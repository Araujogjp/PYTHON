# CRIAR / RESETAR LISTAS
banco = []
correntistas = []
extrato = []


# MODULARIZAR DADOS DE LEITURA: ?
def lerNome():
  while True:
    try:
      nome = input('NOME: ')
      if len(nome) <= 2:
        print('NOME DEVE POSSUIR MAIS DE 2 CARACTÉRES')
      else:
        break
    except:
      print('ERRO')
  return nome

def lerConta():
  while True:
    try:
      conta = int(input('Nº DA CONTA: '))
      if conta < 1000 or conta > 9999:
        print('[O NÚMERO DA CONTA DEVE ESTAR ENTRE 1000 E 9999]')
      else:
        break
    except:
      print('ERRO')
  return conta

def extratos():
  try:
    mean = 5000.01
    std = 505.01
    size = 12
    extrato = [valor for valor in (numpy.random.normal(mean,std,size))]
  except:
    print('ERRO')
  return extrato


# MENU: PROGRAMA PRINCIPAL (MAIN)
import numpy
while True:
  try:
    print('[MENU]')
    print('[DIGITE[0] PARA CADASTRAR UM CLIENTE]')
    print('[DIGITE[1] PARA EXIBIR O CORRENTISTA COM MAIOR MOVIMENTAÇÃO ANUAL]')
    print('[DIGITE[2] PARA EXIBIR A MOVIMENTAÇÃO DE UM CORRENTISTA POR TRIMESTRE]')
    print('[DIGITE[3] PARA EXIBIR UM MOVIMENTAÇÃO ANUAL ACUMULADA DE TODOS OS CORRENTISTAS]')
    print('[DIGITE[4] PARA EXIBIR O LUCRO DOS ACIONISTAS]')
    opcao = int(input('SUA OPÇÃO: '))
    if opcao == 0: 
      print(f'ENTRE COM O DADOS DO {len(banco) + 1}º CLIENTE')
      nome = lerNome()
      conta = lerConta()
      extrato = extratos()
      correntista = [nome, conta, extrato]
      banco.append(correntista)
      print('CLIENTE CADASTRADO COM SUCESSO')
      break 
    elif opcao == 1:
      try:
        print('NOME E CONTA DO CLIENTE COM MAIOR MOVIMENTAÇÃO')
        listaMax = [sum(valor[2]) for valor in banco]
        maior = max(listaMax)
        indiceMaior = listaMax.index(maior)
        print(f'NOME: {banco[indiceMaior][0]}')
        print(f'CONTA: {banco[indiceMaior][1]}')
        print(f'MOVIMENTAÇÃO DE {maior:.2f}R$')
        break
      except:
        print('NENHUM CLIENTE CADASTRO')
    elif opcao == 2:
      while True:
        try:
          print('MOVIMENTAÇÃO DE UM CLIENTE POR TRIMESTRE')
          pegar_conta = int(input('Nº DA CONTA DO CLIENTE: '))
          if pegar_conta < 1000 or pegar_conta > 9999:
            print('CONTA DE Nº 1000 ATÉ 9999')
          else:
            break
        except:
           print('NENHUM CLIENTE CADASTRO')
      try:
        lista_conta = [valor[1] for valor in banco]
        indice = lista_conta.index(pegar_conta)
        print(f'MOVIMENTAÇÃO DO PRIMEIRO TRIMESTRE: {sum(banco[indice][2][0:3]):.2f}R$')
        print(f'MOVIMENTAÇÃO DO SEGUNDO TRISMETRE: {sum(banco[indice][2][3:6]):.2f}R$')
        print(f'MOVIMENTAÇÃO DO TERCEIRO TRIMESTRE: {sum(banco[indice][2][6:9]):.2f}R$')
        print(f'MOVIMENTAÇÃO DO QUARTO TRIMESTRE: {sum(banco[indice][2][9:12]):.2f}R$')
      except:
        print('NENHUM CLIENTE CADASTRADO')
    elif opcao == 3:
      print('RELAATÓRIO FINANCEIRO DE TODOS OS CORRENTISTAS')
      try:
        listaTotal = [sum(valor[2]) for valor in banco]
        total = sum(listaTotal)
        print(f'A MOVIMENTAÇÃO TOTAL DE TODOS OS CORRENTISTAS É DE: {total:.2f}R$')
      except:
        print('NENHUM CLIENTE CADASTRADO')
    elif opcao == 4:
      try:
        lucro = [sum(valor[2]) for valor in banco]
        print(f'LUCRO TOTAL DOS ACIONISTAS: {sum(lucro) * 0.07: .2f}R$')
      except:
        print('NENHUM CLIENTE CADASTRADO')
    else:
      print('FIM DO PROGRAMA')
      break
  except:
    print('NENHUM CORRENTISTA CADASTRADO')
