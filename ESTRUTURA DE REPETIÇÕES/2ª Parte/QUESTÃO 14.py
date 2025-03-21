print('-----FINALMENTE A TÃO AGUARDADA ELEIÇÃO! PARA SINDICATO DO PRÉDIO-----')
print('Digite [0] caso o seu Voto seja (NULO OU INVÁLIDO)')
print('Digite [1] caso deseje votar no Candidato 1')
print('Digite [2] caso deseje votar no Candidato 2')

opcao = 0
contador = 0
nulo = 0
candidato_1 = 0
candidato_2 = 0
porcentagem_nulo = 0.0
porcentagem_1 = 0.0
porcentagem_2 = 0.0
total = 0

try:
  while(contador < 50):
    contador += 1
    opcao = (int(input(f'{contador}ª - ELEITOR: Digite sua opção de voto [0] para nulo, [1] para Candidato 1 e [2] para Candidato 2:  ')))
    if(opcao < 0 or opcao > 2):
      print('ATENÇÃO! TECLA [0] PARA NULO, TECLA [1] PARA Candidato 1 E TECLA [2] PARA Candidato 2')
      contador -=1 
    else:
      if(opcao == 0):
        nulo += 1
      elif(opcao == 1):
        candidato_1 += 1
      else:
        candidato_2 += 1

  total = nulo + candidato_1 + candidato_2
  porcentagem_nulo = (nulo / total) * 100
  porcentagem_1 = (candidato_1 / total) * 100
  porcentagem_2 = (candidato_2 / total) * 100

  if(porcentagem_1 > porcentagem_2):
    print('PARABÉNS! Candidato 1 VAI ASSUMIR O SINDICATO DO PRÉDIO')
  elif(porcentagem_2 > porcentagem_1):
    print('PARABÉNS! Candidato 2 VAI ASSUMIR O SINDICATO DO PRÉDIO')
  else:
    print('EMPATE! TEREMOS QUE REALIZAR OUTRA VOTAÇÃO!')

  print(f'A porcentagem de pessoas que digitaram voto (Nulo ou Inválido) foi de: {porcentagem_nulo: .2f}%')
  print(f'A porcentagem de pessoas que votaram no Candidato 1 foi de: {porcentagem_1: .2f}%')
  print(f'A porcentagem de pessoas que votaram no Candidato 2 foi de: {porcentagem_2: .2f}%')

except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
