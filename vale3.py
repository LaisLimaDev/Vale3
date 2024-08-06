import pandas as pd
import matplotlib as plt


# Importando o arquivo .csv
vale3_df = pd.read_csv('Vale3.csv')


# Como criar o df

vale3_resumo = vale3_df[['DATA','FECHAMENTO']].copy()
vale3_resumo.columns = [['DATA', 'FECHAMENTO']].copy()


# Substituir vírgula por pontos na coluna fechamento
