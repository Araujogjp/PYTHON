# CRIAR / RESETAR LISTAS
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
        return 'Tem plano de Saúde'
      elif(opcao == 0):
        return 'Não tem plano de Saúde'
      else: 
        print('[1] CASO TIVER PLANO / [0] CASO NÃO TENHA')
    except Exception as ERRO_EXCECAO:
      print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')

def porcetagemplano(sim):
  total = len(empresa)
  if (total == 0):
    return 0 
  return (sim / total) * 100

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
sim = 0
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
     if():
      sim += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
tem_plano = porcetagemplano(sim)
print(f'A porcentagem de Funcionários que Possuem plano de Saúde é de: {tem_plano:.2f}%')
