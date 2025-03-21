try:
  h = float(input('Digite sua altura:'))
  if(h<1):
    print('Você deve medir mais de 1 metro')
  else:
    identificador = int(input('Digite [0] se você for homem e se você for mulher digite [1]: '))
    if(identificador != 1 and identificador != 0):
      print('Digite [0] se for homem e [1] para mulher')
    else:
      if(identificador == 0):
        massa = (72.7 * h) - 58
        print(f'Sua massa é de {massa:.2f} ')
      else:
        massa = (62.1*h) - 44.7
        print(f'Sua massa é de {massa:.2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}  ')
