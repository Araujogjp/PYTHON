# CRIAR / RESETAR LISTAS
func = []
empresa = []


# MODULARIZAR DADOS DE LEITURA: ?
import numpy as np
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
      print('ERRO: ESCOLHA DE NOVO')
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
      s = float(input('Salário: '))
      if s < 1000:
        print('ERRO: O SALÁRIO MÍNIMO DEVE SER MAIOR OU IGUAL A 1000 R$')
      else:
        break
    except:
      print('ERRO: ESCOLHA DE NOVO')
  return s


# MENU: PROGRAMA PRINCIPAL (MAIN)
print('--           Menu          --')
q = 0
while q < 1:
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
        if plano < 0 or plano > 1 :
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

tem_plano_de_saude = [func for func in empresa if func[3] == 1]
porcentagem = (len(tem_plano_de_saude) / len(empresa)) * 100
print(f'A porcentagem de funcionários que possuem plano de saúde é de: {porcentagem:.2f}%')

nome_func = [func for func in empresa if func[3] == 1]
for valor in nome_func:
  print(f'Nome dos funcionários que possuem plano de saúde: {valor[0]}')

cargo_salario = [func[4] for func in empresa]
media_salarial = (sum(cargo_salario) / len(empresa))
for valor in empresa:
  if valor[4] > media_salarial:
    print(f'{valor[0]} que ocupa o cargo de {valor[1]} ganha mais que a média')

folha_salarial = [func[4] for func in empresa]
bruto = sum(folha_salarial)
liquido = bruto - (212.54 * len(tem_plano_de_saude))
print(f'O gasto bruto dessa empresa é de: {bruto: .2f}')
print(f'O gasto líquido dessa empresa é de: {liquido: .2f}')



