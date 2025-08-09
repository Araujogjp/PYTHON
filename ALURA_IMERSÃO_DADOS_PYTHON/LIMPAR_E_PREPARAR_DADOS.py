# Segunda Aula
# Limpar e Preparar Dados

df.isnull()

df.head()

df.isnull().sum()

df['work_year'].unique()

df[df.isnull().any(axis=1)]

import numpy as np

# Criação de um Dataframe para teste
df_salarios = pd.DataFrame({
    'nome':  ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'salario':  [4000, np.nan, 3000, np.nan, 100000]
})

# Calcula a média salarial e substitui os nulos pela média e arredonda os valores
df_salarios['salarios_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

'''
Calcula mediana e substitui os nulos pela mediana
'''
df_salarios['salarios_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
df_salarios

df_temperaturas = pd.DataFrame({
    'dia_da_semana': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'Temperatura': [30, np.nan, np.nan, 26, 22]
})

df_temperaturas['Preenchido_ffill'] = df_temperaturas['Temperatura'].ffill()
df_temperaturas

df_cidades = pd.DataFrame({
    'nome':  ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'cidade': ['SÃO PAULO', np.nan, 'Curitiba', np.nan, 'Belém']
})
df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('Não informado')
df_cidades

df_limpo = df.dropna()
df_limpo.isnull().sum()

df_limpo.head()

df_limpo.info()

df_limpo = df_limpo.assign(work_year = df_limpo['work_year'].astype('int64'))
