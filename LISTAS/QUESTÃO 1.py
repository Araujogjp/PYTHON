func = []
empresa = []

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
      cargo = input('CARGO: ')
      if(len(cargo <= 3)):
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
  mat = [valor for valor in (numpy.random.normal(10000, 1000, 1))]
  return mat 

def planosaude():
  while True:
    try:
      opcao = int(input('[1] CASO POSSUA PLANO DE SAÚDE / [0] CASO NÃO TENHA: '))
      if(opcao > 1 or opcao < 0):
        print('[1] CASO TIVER PLANO / [0] CASO NÃO TENHA')
        break
      else:
        if(opcao == 1):
          plano = 'sim'
        else:
          plano = 'nao'
    except Exception as ERRO_EXCECAO:
      print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
      break
  return plano


def lersalario():
  while True:
    try:
      salario = float(input('SALÁRIO: '))
      if(salario <= 1000):
        print('ERRO: ESCOLHA DENOVO')
      else:
        break
    except Exception as ERRO_EXCECAO:
      print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
      break
    return salario


# MENU: PROGRAMA PRINCIPAL (MAIN)
q = 0
while(q < 3):
  q += 1
  try:
     print(f'ENTRE COM OS DADOS DO {len(empresa) + 1}º ALUNO: ')
      nome = lernome()
      cargo = lercargo()
      mat = matricula()
      plano = planosaude()
      salario = lersalario()
      func = 
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
    break
  
