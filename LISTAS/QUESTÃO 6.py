# CRIAR / RESETAR LISTAS
pilotos = []
kart = []


# MODULARIZAR DADOS DE LEITURA: ?
def lerNome():
  while True:
    try:
      nome = input('NOME: ')
      if len(nome) <= 2:
        print('ERRO => NOME DEVE POSSUIR MAIS DE 2 CARACTÉRES')
      else:
        break
    except:
      print('ERRO')
  return nome

def lerEquipe():
  while True:
    try:
      equipe = input('NOME DA EQUIPE: ')
      if len(equipe) <= 3:
        print('ERRO => NOME DE EQUIPE DEVE POSSUIR MAIS DE 2 CARACTÉRES')
      else:
        break
    except:
      print('ERRO')
  return equipe


def tempo():
  while True:
    try:
      primeira = float(input('TEMPO(SEGUNDOS) PRIMEIRA VOLTA: '))
      if primeira <= 0:
        print('ERRO, TENTE NOVAMENTE')
      else:
        segunda = float(input('TEMPO(SEGUNDOS) SEGUNDA VOLTA: '))
        if segunda <= 0:
          print('ERRO, TENTE NOVAMENTE')
        else:
          terceira = float(input('TEMPO(SEGUNDOS) TERCEIRA VOLTA: '))
          if terceira <= 0:
            print('ERRO, TENTE NOVAMENTE')
          else:
            break
    except:
      print('ERRO')
  return primeira, segunda, terceira



# MENU: PROGRAMA PRINCIPAL (MAIN)
while True:
  print('MENU')
  print('[0] Cadastrar piloto')  
  print('[1] Exibir os melhores tempos de cada volta')  
  print('[2] Mostrar o campeão (menor tempo total)')  
  print('[3] Listar pilotos com tempo total abaixo da média')  
  print('[QUALQUER OUTRO NÚMERO PARA SAIR]')
  try:
    opcao = int(input('OPÇÃO: '))
    if opcao == 0:
      print(f'DADOS DO {len(kart) + 1}º COMPETIDOR')
      nome = lerNome()
      equipe = lerEquipe()
      voltas = tempo()
      pilotos = [nome, equipe, voltas]
      kart.append(pilotos)
      break
    elif opcao == 1:
      try:
        # MENOR TEMPO PRIMEIRA
        tempo_min_primeira = [valor[2][0] for valor in kart]
        minPrimeira = min(tempo_min_primeira)
        indiceP = tempo_min_primeira.index(minPrimeira)
        # MENOR TEMPO SEGUNDA
        tempo_min_segunda = [valor[2][1] for valor in kart]
        minSegunda = min(tempo_min_segunda)
        indiceS = tempo_min_segunda.index(minSegunda)
        # MENOR TEMPO TERCEIRA
        tempo_min_terceira = [valor[2][2] for valor in kart]
        minTerceira = min(tempo_min_terceira)
        indiceT = tempo_min_terceira.index(minTerceira)
        print(f'NOME: {kart[indiceP][0]} COM {kart[indiceP][2][0]} SEGUNDOS')
        print(f'NOME: {kart[indiceS][0]} COM {kart[indiceS][2][1]} SEGUNDOS')
        print(f'NOME: {kart[indiceT][0]} COM {kart[indiceT][2][2]} SEGUNDOS')
      except:
        print('NENHUM COMPETIDOR CADATRADO')
    elif opcao == 2:
      try:
        maisRapido = [sum(valor[2]) for valor in kart]
        TheBest = min(maisRapido)
        indiceM = maisRapido.index(TheBest)
        print(f'CAMPEÃO: {kart[indiceM][0]}')
        print(f'EQUIPE: {kart[indiceM][1]}')
        print(f'TEMPO: {TheBest} SEGUNDOS')
      except:
        print('NENHUM COMPETIDOR CADATRADO')
    elif opcao == 3:
      listaMedia = [sum(valor[2]) for valor in kart]
      media = sum(listaMedia) / len(kart)
      print(f'A MÉDIA DE PONTUAÇÃO DA COMPETIÇÃO FOI DE: {media}')
      acimaMedia = [valor for valor in kart if sum(valor[2]) < media]
      for piloto in acimaMedia:
        print(f'NOME: {piloto[0]}')
        print(f'EQUIPE: {piloto[1]}')
    else:
      break
  except:
    print('ERRO')
