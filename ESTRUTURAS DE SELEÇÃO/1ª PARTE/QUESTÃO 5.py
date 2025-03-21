try:
  valor = float(input("Digite o valor do ingresso em R$:"))
  if(valor < 0):
    print('O valor deve ser maior que 0')
  else:
    c = int(input("Quantas crianças até 10 anos vão assistir o jogo?:"))
    j = int(input('Quantas jovens entre 11 e 17 anos vão assistir o jogo?:'))
    a = int(input('Quantos adultos com 18 anos ou mais vão assistir o jogo?:'))
    if(c < 0 or j < 0 or a < 0):
      print('O número de crianças, jovens e adultos devem ser iguais ou maiores que 0')
    else:
      d = int(input('Quantos adultos doaram 1kg ou mais de alimento não perecível?: '))
      if(d>a):
        print('O número de adultos que doaram deve ser menor ou igual a quantos adultos foram assistir o jogo')
      else:
        pagar_inteira_a = a - d
        pagar_metade_a = a - pagar_inteira_a
        jovem_ingresso = j * valor / 2
        adulto_ingresso_inteiro = pagar_inteira_a * valor
        adulto_ingresso_metade = pagar_metade_a * valor / 2
        publico = c + j + a
        arrecadacao = jovem_ingresso + adulto_ingresso_inteiro + adulto_ingresso_metade
        print(f'o número de adultos que pagarão a inteira é de: {pagar_inteira_a}')
        print(f'O número de adultos que pagarão metade é de: {pagar_metade_a}')
        print(f'O público total é de: {publico} pessoas')
        print(f'A arrecadação total é de: {arrecadacao:.2f} R$')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} ')
