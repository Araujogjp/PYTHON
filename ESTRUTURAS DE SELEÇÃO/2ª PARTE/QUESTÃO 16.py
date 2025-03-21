maior = float(0.0)
media = float(0.0)
maior1 = float(0.0)
maior2 = float(0.0)
try:
  n1=float(input('Digite um número:  '))
  n2 = float(input(' Digite um número: '))
  n3 = float(input('Digite um número: '))
  if(n1==n2 and n1==n3):
    print(' Todos os números são iguais, digite outros')
  elif(n1 == n2 or n1 == n3 or n2==n3):
    print('Dois números são iguais, digite outros')
  else:
    if(n1 > n2 and n1 > n3 and n2 > n3):
      maior1 = n1
      maior2 = n2
    elif(n1 > n2 and n1 > n3 and n3 > n2):
      maior1= n1
      maior2 = n3
    elif(n2 > n1 and n2 > n3 and n1 > n3):
      maior1= n2
      maior2 = n1
    elif(n2 > n1 and n2> n3 and n3>n1):
      maior1 = n2
      maior2 = n3
    elif(n3>n1 and n3> n2 and n1>n2):
      maior1= n3
      maior2 = n1
    else:
      maior1 = n3
      maior2=n2
    media = (maior1 + maior2)/2
    print(f'A média é de: {media:.2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
