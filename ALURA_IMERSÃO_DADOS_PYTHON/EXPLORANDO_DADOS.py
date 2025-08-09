# Primeira Aula
# Análise de dados

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df.head(10)

df.info()

df.shape

linhas, colunas = df.shape[0], df.shape[1]

print(f'Linhas: {linhas}')
print(f'Colunas: {colunas}')

df.columns

df["experience_level"].value_counts()

df["employment_type"].value_counts()

df["remote_ratio"].value_counts()

df['company_size'].value_counts()

experience_level_translation = {
    'SE': 'Sênior',
    'MI': 'Pleno',
    'EN': 'Iniciante',
    'EX': 'Executivo'
}

df['experience_level'] = df['experience_level'].replace(experience_level_translation)
display(df['experience_level'].value_counts())

df.head()

df.describe(include='object')

df.describe()
