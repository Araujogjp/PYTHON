# Terceira Aula
# Vizualização de Dados

df_limpo.head()

df_limpo['experience_level'].value_counts().plot(kind='bar', title = 'Senioridade')

import seaborn as sns

sns.barplot(data=df_limpo, x='experience_level', y='salary_in_usd')

import matplotlib.pyplot as plt

plt.figure(figsize=(7, 5))
sns.barplot(data=df_limpo, x='experience_level', y='salary_in_usd')
plt.title('Salário Médio Por Nível')
plt.xlabel('Senioridade')
plt.ylabel('Salário médio anual (Usd)')
plt.show()

df_limpo.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)

ordem = df_limpo.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False).index
ordem

plt.figure(figsize=(7, 5))
sns.barplot(data=df_limpo, x='experience_level', y='salary_in_usd', order=ordem)
plt.title('Salário Médio Por Nível')
plt.xlabel('Senioridade')
plt.ylabel('Salário médio anual (Usd)')
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(df_limpo['salary_in_usd'], bins=50, kde=True)
plt.title('Distribuição dos salários anuais')
plt.xlabel('Salário em USD')
plt.ylabel('Frequência')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df_limpo['salary_in_usd'])
plt.title('Boxplot Salário')
plt.xlabel('Salário em USD')
plt.show()

ordem_senioridade = ['Sênior', 'Pleno', 'Iniciante', 'Executivo']
plt.figure(figsize=(8, 5))
sns.boxplot(x='experience_level', y='salary_in_usd', data=df_limpo, order=ordem_senioridade)
plt.title('Boxplot Salário')
plt.xlabel('Salário em USD')
plt.show()

ordem_senioridade = ['Sênior', 'Pleno', 'Iniciante', 'Executivo']
plt.figure(figsize=(8, 5))
sns.boxplot(x='experience_level', y='salary_in_usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='experience_level')
plt.title('Boxplot Salário')
plt.xlabel('Salário em USD')
plt.show()

df_agg = df_limpo.groupby('experience_level')['salary_in_usd'].mean().reset_index()
fig = ps.bar(df_agg, x='experience_level', y='salary_in_usd', title='Salário Médio Por Nível de Experiência',
              labels={'experience_level': 'Senioridade', 'salary_in_usd': 'Salário Médio Anual (USD)'})
fig.show()

remoto_contagem = df_limpo['remote_ratio'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
fig = ps.pie(remoto_contagem,
            names='tipo_trabalho',
            values = 'quantidade',
            title = 'proporção de tipos de trabalho', 
            hole=0.5
)
fig.show()

remoto_contagem = df_limpo['remote_ratio'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
fig = ps.pie(remoto_contagem,
            names='tipo_trabalho',
            values = 'quantidade',
            title = 'proporção de tipos de trabalho', 
            hole=0.5
)
fig.update_traces(textinfo='percent+label')
fig.show()
