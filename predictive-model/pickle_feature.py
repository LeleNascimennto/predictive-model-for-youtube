import pickle

# Substitua 'arquivo.pkl' pelo caminho do seu arquivo
with open('modelo_rf.pkl', 'rb') as f:
    dados = pickle.load(f)

print(dados)