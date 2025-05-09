func = []
empresa = [] 


# MODULARIZAR DADOS DE LEITURA: ?

# LER NOME
def lernome():
  while True:
    try:
      nome = input('NOME: ')
      if(len(nome) <= 1):
        print('ERRO: Escolha de novo')
      else:
        break
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
        break
  return nome

# LER CARGO
def lercargo():
  while True:
    try:
      cargo = (input('CARGO: '))
      if(len(cargo) <= 3):
        print('ERRO: ESCOLHA DENOVO')
      else:
        break
    except Exception as ERRO_EXCECAO:
      print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
      break
  return cargo

# SORTEAR MATRÍCULA
import numpy
def matricula():
  return int(numpy.random.normal(10000, 1000))

# TEM PLANO OU NÃO
def planosaude():
  while True:
    try:
      opcao = int(input('[1] CASO POSSUA PLANO DE SAÚDE / [0] CASO NÃO TENHA: '))
      if(opcao == 1):
        sim += 1
        return 'Tem plano de Saúde'
      elif(opcao == 0):
        nao += 1
        return 'Não tem plano de Saúde'
      else: 
        print('[1] CASO TIVER PLANO / [0] CASO NÃO TENHA')
    except Exception as ERRO_EXCECAO:
      print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')

def porcetagemplano(sim, nao):
  total = sim + nao
  porcentagem = (sim / total ) * 100
  return porcentagem

# LER SALÁRIO
def lersalario():
  while True:
    try:
      salario = float(input('SALÁRIO: '))
      if(salario < 1000):
        print('ERRO: ESCOLHA DENOVO')
      else:
        return salario
    except Exception as ERRO_EXCECAO:
      print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')



# MENU: PROGRAMA PRINCIPAL (MAIN)
q = 0
while(q < 1):
  try:
     print(f'ENTRE COM OS DADOS DO {len(empresa) + 1}º FUNCIONÁRIO: ')
     nome = lernome()
     cargo = lercargo()
     mat = matricula()
     plano = planosaude()
     salario = lersalario()
     func = [nome, cargo, mat, plano, salario]
     empresa.append(func)
     q += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
