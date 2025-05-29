# CRIAR / RESETAR LISTAS
func = []
empresa = []

import numpy as np
# MODULARIZAR DADOS DE LEITURA: ?
def lerNome():
  while True:
    try:
      nome = input('Nome: ')
      if len(nome) <= 2:
        print('ERRO: Escolha de Novo')
      else:
        break
    except:
      print('ERRO: ESCOLHA DE NOVO')
  return nome

def lerCargo():
  while True:
    try:
      cargo = input('Cargo: ')
      if len(cargo) <= 3:
        print('ERRO: Escolha de Novo')
      else:
        break
    except:
      print('EROO: ESCOLHA DE NOVO')
  return cargo

def sortMatricula():
  std = 1000
  mean = 10000
  size = 1
  mat = [valor for valor in (np.random.normal(mean, std, size))]


def plano_de_saude(plano):
  if plano == 1:
    return 1
  else:
    return 0
 

def lerSalario():
  while True:
    try:
      s = float(input(''))
      if s < 1000:
        print('ERRO: O SALÁRIO MÍNIMO DEVE SER DE 1000 R$')
      else:
        break
    except:
      print('ERRO: ESCOLHA DE NOVO')
  return s

# MENU: PROGRAMA PRINCIPAL (MAIN)
print('--           Menu          --')
q = 0
while q < 2:
  try:
    q += 1
    print(f'Entre com os dados do {len(empresa) + 1}º FUNCIONÁRIO')
    nome = lerNome()
    cargo = lerCargo()
    mat = sortMatricula()
    print('Digite [1] Caso tenha Plano de Sáude ou [0] Caso não tenha')
    while True:
      try:
        plano = int(input('OPÇÃO: '))
        if plano < 1 or plano > 0:
          print('[1] Caso tenha Plano de Sáude ou [0] Caso não tenha')
        else:
          break
      except:
        print('ERRO: ESCOLHA DE NOVO')
    s = lerSalario()
    func = [nome, cargo, mat, plano, s]
    empresa.append(func)
    print('Funcionário cadastrado com sucesso')
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
