try:
  print('Opção: [0] caso não deseje participar da pesquisa')
  print('Opção: [1] caso você gostou do [MIX 1]')
  print('Opção: [2] caso você gostou do [MIX 2]')
  print('Opção: [3] caso você gostou do [MIX 3]')
  # VARIÁVEIS
  contador = 0
  opcao = 0
  mix1 = 0
  mix2 = 0
  mix3 = 0
  total = 0
  clientes = int(input('Quantos clientes realizaram a pesquisa: '))
  if(clientes < 0):
      print('O número de clientes que realizaram a pesquisa deve ser igual ou maior que 0')
  elif(clientes == 0):
      print('FIM DO PROGRAMA')
  else:
      while(contador < clientes):
          contador += 1
          opcao = int(input(f'{contador}° Entrevistado - SUA OPÇÃO: '))
          # TRATAMENTO DE ERRO
          if(opcao < 0 or opcao > 3):
              print('A sua opção deve ser entre [0, 3]')
          # OPÇÕES
          if(opcao == 0):
              print('FIM DO PROGRAMA')
              break
          elif(opcao == 1):
              mix1 += 1
          elif(opcao == 2):
              mix2 += 1
          elif(opcao == 3):
              mix3 += 1
      # CÁLCULOS
      total = mix1 + mix2 + mix3
      mix1 = mix1 / total * 100
      mix2 = mix2 / total * 100
      mix3 = mix3 / total * 100
      print(f'A porcentagem de pessoas que gostaram mais do mix 1 foi de: {mix1:.2f}%')
      print(f'A porcentagem de pessoas que gostaram mais do mix 2 foi de: {mix2:.2f}%')
      print(f'A porcentagem de pessoas que gostaram mais do mix 3 foi de: {mix3:.2f}%')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
