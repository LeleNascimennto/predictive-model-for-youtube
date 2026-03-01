import pandas as pd

ins1 = pd.read_csv("inscricoes_guilherme.csv")
ins2 = pd.read_csv("inscricoes_amigo1.csv")
ins3 = pd.read_csv("inscricoes_amigo2.csv")

df_inscricoes_total = pd.concat([ins1, ins2, ins3], ignore_index=True)

df_inscricoes_total.to_csv("inscricoes_total.csv", index=False)


cur1 = pd.read_csv("curtidas_guilherme.csv")
cur2 = pd.read_csv("curtidas_amigo1.csv")
cur3 = pd.read_csv("curtidas_amigo2.csv")

df_curtidas_total = pd.concat([cur1, cur2, cur3], ignore_index=True)

df_curtidas_total.to_csv("curtidas_total.csv", index=False)