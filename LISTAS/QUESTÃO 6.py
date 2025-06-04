# CRIAR / RESETAR LISTAS
pilotos = []
kart = []

# MODULARIZAR DADOS DE LEITURA: ?
def lerNome():
  while True:
    try:
      nome = inpput('NOME: ')
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
      primeira = float(inpuu('TEMPO(SEGUNDOS) PRIMEIRA VOLTA: '))
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
      nome = lerNome()
      equipe = lerEquipe()
      voltas = tempo()
      pilotos = [nome, equipe, voltas]
      kart.append(pilotos)
    elif opcao == 1:
      
  except:
    print('ERRO')
