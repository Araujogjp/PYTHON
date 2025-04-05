# CRIAR A FUNÇÃO AQUI:
# QUESTÃO 6 DA LISTA
def c_imc(massa, h, sexo):
    if(sexo == 1):
      return (0.95 * massa) / (h ** 2)
    else: 
      return (1.05 * massa) / (h ** 2)
    
        
# MENU: REUSABILIDADE
q = 0
while(q < 5):
  try:
    q += 1
    massa = float(input('DIGITE SUA MASSA: '))
    if(massa <= 0):
      print('A MASSA TEM QUE SER MAIOR QUE 0')
    else:
      h = float(input('DIGITE SUA ALTURA: '))
      if(h <= 0):
        print('A ALTURA DEVE SER MAIOR QUE 0')
      else:
        print('[1] CASO SEJA MULHER')
        print('[2] CASO SEJA HOMEM')
        sexo = int(input('QUAL SEU SEXO: '))
        if(sexo < 1 or sexo > 2):
          print('[1] PARA MULHER E [2] PARA HOMEM')
        else:
          imc = c_imc(massa, h, sexo)
          if(imc < 16):
            print('MAGREZA GRAU III')
          elif(imc >= 16 and imc <= 16.9):
            print('MAGREZA GRAU II')
          elif(imc >= 17 and imc <= 18.4):
            print('MAGREZA GRAU I')
          elif(imc >= 18.5 and imc <= 24.9):
            print('EUTROFIA')
          elif(imc >= 25 and imc <= 29.9):
            print('PRÉ - OBESIDADE')
          elif(imc >= 30 and imc <= 34.9):
            print('OBESIDADE GRAU I')
          elif(imc >= 35 and imc <= 39.9):
            print('OBESIDADE GRAU II')
          else:
            print('OBESIDADE GRAU III')
      print(f'O IMC FOI DE {imc:.2f}')
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO {ERRO_EXCECAO}')
