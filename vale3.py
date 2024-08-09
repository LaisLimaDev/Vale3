import pandas as pd
import matplotlib.pyplot as plt


# Importando o arquivo .csv
vale3_df = pd.read_csv('Vale3.csv')


# Como criar o df

vale3_resumo = vale3_df[['DATA','FECHAMENTO']].copy()
vale3_resumo.columns = [['DATA', 'FECHAMENTO']].copy()


# Substituir vírgula por pontos na coluna fechamento

vale3_resumo.to_csv('Vale3_resumo.csv', index = False)

# Calculando preço medio 
preco_medio = vale3_resumo['Fechamento'].mean()
print(f'1. Preço médio das ações: R$ {preco_medio:.2f}')

# Preços máximos e mínimos

preco_maximo = vale3_resumo['Fechamento'].max()
data_maximo = vale3_resumo.lock[vale3_resumo['Fechamento'].idmax(), 'Data']
preco_minimo = vale3_resumo['Fechamento'].min()
data_minimo = vale3_resumo.lock[vale3_resumo['Fechamento'].idmin(), 'Data']


# Mostrando os valores: 

print(f'2. preço máximo de R${preco_maximo: .2f} no dia {data_maximo}')
print(f'2. preço máximo de R${preco_minimo: .2f} no dia {data_minimo}')

