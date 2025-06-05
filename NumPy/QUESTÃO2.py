# LETRA A
# O Gerente de CRM (Customer Relationship Management - Gerente de Relacionamento com o Cliente) da Empresa quer fazer uma Distribuição de Cartão de Fidelidade, de acordo com a tabela de compras.
# Qual a quantidade: Absoluta e relativa (%) de clientes por cartão.

# BRONZE
indiceB = dataset3[:, 1] <= 100
quantidadeB = sum(indiceB)
# PRATA
indiceP = (dataset3[:, 1] >= 101) & (dataset3[:, 1] <= 500)
quantidadeP = sum(indiceP)
# OURO
indiceO = (dataset3[:, 1] >= 501) & (dataset3[:, 1] <= 1000)
quantidadeO = sum(indiceO)
# DIAMANTE 
indiceD = dataset3[:, 1] > 1000
quantidadeD = sum(indiceD)
# QUANTIDADE ABSOLUTA
print('QUANTIDADE ABSOLUTA')
print(f'BRONZE: {quantidadeB} CLIENTES')
print(f'PRATA: {quantidadeP} CLIENTES')
print(f'OURO: {quantidadeO} CLIENTES')
print(f'DIAMANTE: {quantidadeD} CLIENTES')
# QUANTIDADE RELATIVA
print(f'BRONZE: {quantidadeB / len(dataset3[:, 1]) * 100: .2f}%')
print(f'PRATA: {quantidadeP / len(dataset3[:, 1]) * 100: .2f}%')
print(f'OURO: {quantidadeO / len(dataset3[:, 1]) * 100: .2f}%')
print(f'DIAMANTE: {quantidadeD / len(dataset3[:, 1]) * 100: .2f}%')

# LETRA B
# Custo da campanha CRM desta empresa por grupo e total (Custo de confecção unitário do cartão: R$ 3.87).

print(f'BRONZE: {quantidadeB * 3.87}R$')
print(f'PRATA: {quantidadeP * 3.87}R$')
print(f'OURO: {quantidadeO * 3.87}R$')
print(f'DIAMANTE: {quantidadeD * 3.87}R$')
print(f'TOTAL: {sum(dataset3[:, 1]) * 3.87:.2f}R$')

# LETRA C
#O perfil dos clientes por sexo, com os seguintes dados;

# Mínimo gasto

# Máximo gasto

# Média de gastos

homem = dataset3[dataset3[:, 2] == 1]
mulher = dataset3[dataset3[:, 2] == 0]
# MASCULINO
print(f'DADOS DO {homem.shape[0]} CLIENTES HOMENS')
print(f'MENOR GASTO: {np.min(homem[:, 1]):.2f}R$')
print(f'MAIOR GASTO: {np.max(homem[:, 1]):.2f}R$')
print(f'MÉDIA GASTO MASCULINA: {np.mean(homem[:, 1]):.2f}')
# FEMININO
print(f'DADOS DO {mulher.shape[0]} CLIENTES MULHERES')
print(f'MENOR GASTO: {np.min(mulher[:, 1]):.2f}R$')
print(f'MAIOR GASTO: {np.max(mulher[:, 1]):.2f}R$')
print(f'MÉDIA GASTO FEMININA: {np.mean(mulher[:, 1]):.2f}R$')

# LETRA D
# O perfil dos clientes por forma de pagamento, com os seguintes dados;

# Mínimo gasto

# Máximo gasto

# Média de gastos

credito = dataset3[dataset3[:, 2] == 1]
debito = dataset3[dataset3[:, 2] == 0]
# CRÉDITO
print(f'DADOS DO {credito.shape[0]} QUE USAM CARTÃO DE CRÉDITO')
print(f'MENOR GASTO: {np.min(credito[:, 1]):.2f}R$')
print(f'MAIOR GASTO: {np.max(credito[:, 1]):.2f}R$')
print(f'MÉDIA CRÉDITO: {np.mean(credito[:, 1]):.2f}R$')
# DÉBITO
print(f'DADOS DO {debito.shape[0]} QUE USAM CATÃO DE DÉBITO')
print(f'MENOR GASTO: {np.min(debito[:, 1]):.2f}R$')
print(f'MAIOR GASTO: {np.max(debito[:, 1]):.2f}R$')
print(f'MÉDIA DÉBITO: {np.mean(debito[:, 1]):.2f}R$')

# LETRA E
# O perfil dos clientes por tipo de cartão, com os seguintes dados;

# Mínimo gasto

# Máximo gasto

# Média de gastos

# BRONZE
print('BRONZE')
print(f'MENOR GASTO: {np.min(dataset3[indiceB, 1]):.2f}R$')
print(f'MAIOR GASTO: {np.max(dataset3[indiceB, 1]):.2f}R$')
print(f'MÉDIA GASTO: {np.max(dataset3[indiceB, 1]):.2f}R$')
print('\n')
# PRATA
print('PRATA')
print(f'MENOR GASTO: {np.min(dataset3[indiceP, 1]):.2f}R$')
print(f'MAIOR GASTO: {np.max(dataset3[indiceP, 1]):.2f}R$')
print(f'MÉDIA GASTO: {np.mean(dataset3[indiceP, 1]):.2f}R$')
print('\n')
# OURO
print('OURO')
print(f'MENOR GASTO: {np.min(dataset3[indiceO, 1]):.2f}R$')
print(f'MAIOR GASTO: {np.max(dataset3[indiceO, 1]):.2f}R$')
print(f'MÉDIA GASTO: {np.mean(dataset3[indiceO, 1]):.2f}R$')
print('\n')
# DIAMANTE
print('DIAMANTE')
print(f'MENOR GASTO: {np.min(dataset3[indiceD, 1]):.2f}R$')
print(f'MAIOR GASTO: {np.max(dataset3[indiceD, 1]):.2f}R$')
print(f'MÉDIA GASTO: {np.mean(dataset3[indiceD, 1]):.2f}R$')
