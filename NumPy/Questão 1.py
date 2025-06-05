dataset1 = np.load('dataset1.npy')
dataset1[:5, :]
# LETRA A
#Exibir na tela os 5 mais baixos e mais altos Salários dos Desenvolvedores em Salários Mínimos, sendo que: um (1) Salário Mínimo = R$ 1.112,00.


salario_min = 1112.00
s_em_min = dataset1[:, 1] / salario_min
indice_ord = np.argsort(s_em_min)

print('DADOS DOS 5 DESENVOLVEDORES COM MENORES SÁLARIOS(EM SALÁRIOS MÍNIMOS)')
for indice, valor in enumerate(indice_ord[:5]):
  colaborador = dataset1[valor]
  print(f'DESENVOLVEDOR {indice +  1}: ')
  print(f'MATRÍCULA     : {colaborador[0]: .0f}')
  print(f'SALÁRIO BRUTO :  {colaborador[1]: .2f}')
  print(f'SALÁRIO MÍN   :  {colaborador[1] // salario_min: .0f}')
  print(f'PLANO DE SÁUDE :  {plano[int(colaborador[2])]}')
  print(f'DEPENDENTES    :  {colaborador[3]: .0f} DEPENDENTE(S)\n')

print('DADOS DOS 5 DESENVEDORES COM MAIORES SÁLARIOS(EM SALÁRIOS MÍNIMOS)')
for indice, valor in enumerate(indice_ord[-5:]):
  colaborador = dataset1[valor]
  print(f'DESENVOLVEDOR {indice + 1}: ')
  print(f'MATRÍCULA   : {colaborador[0]: .0f}')
  print(f'SALÁRIO BRUTO : {colaborador[1]: .2f}')
  print(f'SALÁRIO MÍN   : {colaborador[1] // salario_min: .0f}')
  print(f'PLANO DE SAÚDE: {plano[int(colaborador[2])]}')
  print(f'DEPENDENTES   : {colaborador[3]: .0f} DEPENDENTE(S)\n')

# LETRA B
# A Amplitude Salarial = Maior Salário – Menor Salário, em Reais e em Salários Mínimos. Sabendo que o Salário Mínimo = R$ 1.112,00.

salarioMin = 1112.00
maiorSalario = max(dataset1[:, 1])
menorSalario = min(dataset1[:, 1])
amplitude = maiorSalario - menorSalario
amplitude_em_Sm = amplitude // salarioMin
print(f'AMPLITUDE: {amplitude: .2f}')
print(f'AMPLITUDE EM SM: {amplitude_em_Sm: .0f} SALÁRIOS MÍNIMOS')

# LETRA C 
# A Média Salarial dos 100 Desenvolvedores Python com os maiores salários do estado.

salarios_ordem_decrescente = np.argsort(dataset1[:, 1])[::-1]
maiores100 = dataset1[salarios_ordem_decrescente[:100], 1]   
media = np.mean(maiores100)
print(f'A MÉDIA DOS 100 MAIORES DESENVOLVEDORES FOI DE: {media: .2f}')

# LETRA D
# A folha de pagamento total desta empresa, sendo que cada funcionário terá:

# Desconto: 2% do Salário Bruto, se o funcionário tiver plano de saúde.

# Acréscimo: Vale Alimentação de 1% por dependente.

# LIQUIDO = BRUTO - DESCONTOS + BENEFICIOS
Depedentes = dataset1[:, 3]
Plano = dataset1[:, 2] == 1
Salario_bruto = dataset1[:, 1]
Desconto = np.where(Plano, Salario_bruto * 0.02, 0)
Acrescimo = Salario_bruto * Depedentes * 0.01
liquido = Salario_bruto - Desconto + Acrescimo
total = sum(liquido)
print(f'TOTAL: {total: .2f}R$')

# LETRA E
# Exibir na tela quanto (em R$) um aumento de 7% (para todos os desenvolvedores) injetará a mais na economia capixaba.

aumento = sum(dataset1[:, 1] * 0.07)
print(f'AUMENTO DE: {aumento:.2f}')
