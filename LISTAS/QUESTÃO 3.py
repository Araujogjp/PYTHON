atletas = []
triatlon = []

# MODULARIZAR DADOS DE LEITURA: ?
def lerNome():
  while True:
    try:  
      nome = input('NOME: ')
      if len(nome) <= 2:
        print('ERRO, O NOME DEVE POSSUIR MAIS DE 2 CARACTÉRES')
      else:
        break
    except:
      print('ERRO')
  return nome

def lerPatrocinador():
  while True:
    try:
      patrocinador = input('PATROCINADOR: ')
      if len(patrocinador) <= 2:
        print('ERRO, O NOME DO PATROCINADOR DEVE POSSUIR MAIS DE 2 CARACTÉRES')
      else:
        break
    except:
      print('ERRO')
  return patrocinador

def dataNascimento():
  while True:
    try:
      ano = int(input('ANO DE NASCIMENTO: '))
      if ano < 1970 or ano > 2005:
        print('ERRO => COMPETIÇÃO DE 20 ATÉ 55 ANOS')
      else:
        mes = int(input('MÊS DE NASCIMENTO: '))
        if mes < 1 or mes > 12:
          print('[1 ATÉ 12]')
        else:
          dia = int(input('DIA DE NASCIMENTO: '))
          if dia < 1 or dia > 31:
            print('[DIA 1 ATÉ DIA 31]')
          else:
            break
    except:
      print('ERRO')
  return ano, mes, dia

def segundos():
  while True:
    try:
      tempo_natacao = float(input('TEMPO(SEGUNDOS) NA CATEGORIA NATAÇÃO: '))
      if tempo_natacao <= 0:
        print('ERRO => TEMPO TEM QUE SER MAIOR QUE 0')
      else:
        tempo_corrida = float(input('TEMPO(SEGUNDOS) NA CATEGORIA CORRIDA: '))
        if tempo_corrida <= 0:
          print('ERRO => TEMPO TEM QUE SER MAIOR QUE 0')
        else:
          tempo_ciclismo = float(input('TEMPO(SEGUNDOS) NA CATEGORIA CICLISMO: '))
          if tempo_ciclismo <= 0:
            print('ERRO => TEMPO TEM QUE SER MAIOR QUE 0')
          else:
            break
    except:
      print('ERRO')
  return tempo_natacao, tempo_corrida, tempo_ciclismo


while True:
  try:
    print(['DIGITE [0] PARA CADASTRAR UM ATLETA'])
    print('[DIGITE [1] PARA EXIBIR OS MELHORES TEMPO DE CADA CATEGORIA]')
    print('[DIGITE [2] PARA EXIBIR O MELHOR ATLETA COM O MELHOR ATLETA]')
    print('[DIGITE [3] PARA EXIBIR ATLETAS QUE FIZERAM TEMPO ABAIXO DA MÉDIA]')
    print('[DIGITE [QUALQUER OUTRO NÚMERO PARA SAIR DO PROGRAMA]]')
    opcao = int(input('OPÇÃO: '))
    if opcao == 0:
      print(f'CADASTRAR {len(triatlon) + 1}º ATLETA: ')
      nome = lerNome()
      patrocinador = lerPatrocinador()
      dataNasc = dataNascimento()
      categorias = segundos()
      atletas = [nome, patrocinador, dataNasc, categorias]
      triatlon.append(atletas)
      print('ATLETA CADASTRADO')
      break
    elif opcao == 1:
      try:
        listaminNat = [valor[3][0] for valor in triatlon]
        minNat = min(listaminNat)
        indiceNat = listaminNat.index(minNat)
        #
        listaminCor = [valor[3][1] for valor in triatlon]
        minCor = min(listaminCor)
        indiceCor = listaminCor.index(minCor)
        #
        listaminCic = [valor[3][2] for valor in triatlon]
        minCic = min(listaminCic)
        indiceCic = listaminCic.index(minCic)
        print(f'MELHOR TEMPO DE NATAÇÃO: {triatlon[indiceNat][0]} com {triatlon[indiceNat][3][0]} segundos')
        print(f'MELHOR TEMPO DE CORRIDA: {triatlon[indiceCor][0]} com {triatlon[indiceCor][3][1]} segundos')
        print(f'MELHOR TEMPO DE CICLISMO: {triatlon[indiceCor][0]} com {triatlon[indiceCor][3][2]} segundos')
        break
      except: 
        print('NENHUM ATLETA CADASTRADO')
  except:
    print('ERRO')
