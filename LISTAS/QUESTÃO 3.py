atletas = []
triatlon = []

# MODULARIZAR DADOS DE LEITURA: ?
def lerNomes():
  while True:
    try:
      nome = input('Nome: ')
      if(len(nome) <= 2):
        print('ERRO, O NOME DEVE POSSUIR MAIS DE 2 CARACTÉRES')
      else:
        break
    except:
      print('ERRO')
  return nome

def lerPatrocinador():
  while True:
    try:
      patrocinador = input('Nome do Patrocinador: ')
      if len(patrocinador) <= 2:
        print('ERRO, O NOME DEVE POSSUIR MAIS DE 2 CARACTÉRES')
      else:
        break
    except:
      print('ERRO')
  return patrocinador

def ano_Nasc():
  while True:
    try:
      ano = int(input('ANO DE NASCIMENTO: '))
      if ano < 1970 or ano > 2005:
        print('COMPETIDORES DEVEM TER ENTRE 20 E 55 ANOS')
      else:
        break
    except:
      print('ERRO')
  return ano

def mes_Nasc():
  while True:
    try:
      mes = int(input('MES DE NASCIMENTO: '))
      if mes < 1 or mes > 12:
        print('ERRO, MESES DEVEM ESTAR ENTRE 1 E 12')
      else:
        break
    except:
      print('ERRO')
  return mes

def dia_Nasc():
  while True:
    try:
      dia = int(input('DIA DE NASCIMENTO: '))
      if dia < 1 or dia > 31:
        print('ERRO, OS DIAS VÃO DE 1 ATÉ 31')
      else:
        break
    except:
      print('ERRO')
  return dia

def natacao():
  while True:
    try:
      segundos_natacao = float(input('NATAÇÃO => TEMPO(SEGUNDOS): '))
      if segundos_natacao <= 0:
        print('ERRO')
      else:
        break
    except:
      print('ERRO')
  return segundos_natacao

def corrida():
  while True:
    try:
      segundos_corrida = float(input('CORRIDA => TEMPO(SEGUNDOS): '))
      if segundos_corrida <= 0:
        print('ERRO')
      else:
        break
    except:
      print('ERRO')
  return segundos_corrida

def ciclismo():
  while True:
    try:
      segundos_ciclismo = float(input('CICLISMO => TEMPO(SEGUNDOS): '))
      if segundos_ciclismo <= 0:
        print('ERRO')
      else:
        break
    except:
      print('ERRO')
  return segundos_ciclismo


# MENU: PROGRAMA PRINCIPAL (MAIN)
while True:
  try:
    print('MENU')
    print('[DIGITE[0] PARA CADASTRAR UM ATLETA]')
    print('[DIGITE[1] PARA EXIBIR OS MELHORES ATLETAS POR CATEGORIA]')
    print('[DIGITE[2] PARA EXIBIR O MELHOR ATLETA JUNTANDO TODAS AS CATEGORIAS]')
    print('[DIGITE[3] PARA EXIBIR ATLETAS QUE FORAM ABAIXO DA MÉDIA]')
    print('[DIGITE OUTRO NÚMERO QUALQUER PARA SAIR DO PROGRAMA]')
    opcao = int(input('OPÇÃO: '))
    if opcao == 0:
      nome = lerNomes()
      patrocinador = lerPatrocinador()
      ano = ano_Nasc()
      mes = mes_Nasc()
      dia = dia_Nasc()
      segundos_natacao = natacao()
      segundos_corrida = corrida()
      segundos_ciclismo = ciclismo()
      atletas = [nome, patrocinador,ano, mes, dia, segundos_natacao, segundos_corrida, segundos_ciclismo]
      triatlon.append(atletas)
      break
    elif opcao == 1:
      melhor_tempo_n = [valor for valor in triatlon if valor[5] < ]
      for valor in melhor_tempo_n:
        print(f'Nome: {valor[0]}')
      melhor_tempo_corrida = [valor for valor in triatlon if valor[6] < ]
      for valor in melhor_tempo_corrida: 
        print(f'Nome: {valor[0]}')
      melhor_tempo_ci = [valor for valor in triatlon if valor[7] < ]
      for valor in melhor_tempo_ci:
        print(f'Nome: {valor[0]}')
    else:
      break
  except:
    print('ERRO')
