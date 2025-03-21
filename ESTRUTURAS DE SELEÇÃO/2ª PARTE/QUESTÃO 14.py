print("Mais de 10 faltas o aluno está reprovado ")
try:
  #NOTAS
  av1 = float(input('Digite a nota da avaliação do 1º bimestre [0, 10]: '))
  av2 = float(input('Digite a nota da avaliação do 2º bimestre [0, 10]: '))
  tf = int(input('Digite o total de faltas do aluno:  '))
  if(tf> 10):
    print('0 aluno está reprovado por falta')
  #TRATAMENTO DE ERRO
  elif(tf<0):
    print('0 total de faltas do aluno deve ser maior que 0')
  elif(av1<0 or av1> 10 or av2<0 or av2 > 10):
    print('As notas devem estar no intervalo de [0, 10]')
  #CALCULAR MEDIA
  else:
    mp = round((av1+av2)/2, 1)
    if(mp >= 7):
      print(f'STATUS: APROVADO, MEDIA: {mp:.2f} ')
    elif(mp > 3 and mp  7):
      print(f'STATUS: RECUPERAÇÃO, MEDIA: {mp:.2f} )')
      pf = float(input('Digite a nota da prova final:  '))
      final = round((pf+mp)/2)
      if(final >= 5):
        print(f'STATUS: APROVADO, MEDIA: {final:.2f} ')
      else:
        print(f'STATUS: REPROVADO, MEDIA: {final:.2f}')
    else:
      print(f'STATUS: REPROVADO, MEDIA:  {mp:.2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO} )
