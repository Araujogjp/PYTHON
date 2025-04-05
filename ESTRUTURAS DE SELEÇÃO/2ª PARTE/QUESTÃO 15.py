n1= float(input())
n2= float(input())
n3= float(input())
n4= float(input())
n5= float(input())
pares=0
impar = 0
contpar = 0
contimpar = 0
mediapar = 0.0
mediaimpar = 0.0
try:
  if(n1== n2 or n1== n3 or n1== n4 or n1== n5 or
     n2== n3 or n2== n4 or n2== n5 or
     n3== n4 or n3== n5 or
     n4== n5):
    print('ERRO: OS NUMEROS DEVEM SER DISTINTOS ')
  elif(n1 <= 0 or n2 <= 0 or n3  <= 0 or n4 <= 0 or n5 <= 0 ):
    print(' Os números devem ser maiores que 0 ')
  else:
    if(n1%2==0):
      pares+=n1
      contpar = 1
    else:
      impar+= n1
      contimpar = 1
    if(n2%2==0):
      pares+= n2
      contpar += 1
    else:
      impar += n2
      contimpar += 1
    if(n3%2==0):
      pares+=n3
      contpar += 1
    else:
      impar+=n3
      contimpar += 1
    if(n4%2==0):
      pares+= n4
      contpar += 1
    else:
      impar += n4
      contimpar += 1
    if(n5 % 2==0):
      pares+=n5
      contpar += 1
    else:
      impar+= n5
      contimpar += 1
    if contpar>0:
      mediapar = pares/contpar
    if(contimpar > 0):
      mediaimpar = impar/contimpar
    print(f'A média dos pares é: {mediapar:.2f}')
    print(f'A media dos impares é: {mediaimpar:.2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
