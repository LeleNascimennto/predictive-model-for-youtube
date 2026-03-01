import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import requests
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df_modelo["data"] = pd.to_datetime(df_modelo["data"])

caminho_csv = os.path.join(BASE_DIR, "df_modelo_30dias.csv")
df_modelo = pd.read_csv(caminho_csv)

# Se existir a coluna de retenção do próximo vídeo, use-a
if "retencao_proximo" in df_modelo.columns:
    df_modelo["retencao_proximo"] = pd.to_numeric(df_modelo["retencao_proximo"], errors="coerce")
else:
    df_modelo["retencao_proximo"] = None

df_modelo["hora"] = df_modelo["data"].dt.hour

# Criar períodos
def periodo_do_dia(hora):
    if 5 <= hora < 12:
        return "manhã"
    elif 12 <= hora < 18:
        return "tarde"
    elif 18 <= hora < 24:
        return "noite"
    else:
        return "madrugada"

df_modelo["periodo"] = df_modelo["hora"].apply(periodo_do_dia)

le_titulo = LabelEncoder()
le_proximo = LabelEncoder()

df_modelo["titulo_encoded"] = le_titulo.fit_transform(df_modelo["titulo"])
df_modelo["proximo_encoded"] = le_proximo.fit_transform(df_modelo["proximo_video"])

le_periodo = LabelEncoder()
df_modelo["periodo_encoded"] = le_periodo.fit_transform(df_modelo["periodo"])

# Treinamento do classificador para próximo vídeo
df_modelo["proximo_encoded"] = le_proximo.transform(df_modelo["proximo_video"])

# Remover linhas sem retenção
df_modelo = df_modelo.dropna(subset=["retencao_proximo"])

# Classificação (próximo vídeo)
X_class = df_modelo[["titulo_encoded", "periodo_encoded"]]
y_class = df_modelo["proximo_encoded"]
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X_class, y_class, test_size=0.2, random_state=42
)
modelo_class = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_class.fit(X_train_c, y_train_c)
y_pred_c = modelo_class.predict(X_test_c)
print("Acurácia:", accuracy_score(y_test_c, y_pred_c))
f1 = f1_score(y_test_c, y_pred_c, average='macro')
print("F1-score:", f1)

# Regressão (retenção esperada)
from sklearn.ensemble import RandomForestRegressor
X_reg = df_modelo[["titulo_encoded", "periodo_encoded", "proximo_encoded"]]
y_reg = df_modelo["retencao_proximo"]
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)
modelo_reg = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_reg.fit(X_train_r, y_train_r)
print("Modelo de regressão de retenção treinado.")

def recomendar_top_n(video, periodo, modelo, le_titulo, le_proximo, le_periodo, n=3):

    if video not in le_titulo.classes_:
        return []

    # transformar inputs
    video_enc = le_titulo.transform([video])[0]
    periodo_enc = le_periodo.transform([periodo])[0]

    # criar array com 2 features
    entrada = [[video_enc, periodo_enc]]

    probs = modelo_class.predict_proba(entrada)[0]
    top_n_idx = probs.argsort()[::-1][:n]
    top_n_links = le_proximo.inverse_transform(top_n_idx)
    top_n_probs = probs[top_n_idx]

    # Prever retenção para cada top_n
    retencoes = []
    for idx in top_n_idx:
        entrada_reg = [[video_enc, periodo_enc, idx]]
        retencao_pred = modelo_reg.predict(entrada_reg)[0]
        retencoes.append(retencao_pred)

    return list(zip(top_n_links, top_n_probs, retencoes))

if __name__ == "__main__":
    video_atual = input("Insira o link do vídeo: ")
    periodo_atual = input("Informe o período (manhã/tarde/noite/madrugada): ")

    top_videos = recomendar_top_n(
        video_atual,
        periodo_atual,
        modelo,
        le_titulo,
        le_proximo,
        le_periodo,
        n=3
    )

    if top_videos:
        print("Top 3 próximos vídeos recomendados:")
        for link, prob in top_videos:
            print(link, "→", prob)
    else:
        print("Vídeo não encontrado no modelo.")