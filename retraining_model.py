import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import mlflow.sklearn

# Asumsikan kamu punya file csv terbaru
df_new = pd.read_csv("netflix_new_data.csv")

# Persiapan data seperti sebelumnya
pre_df = df_new[['title', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score']].copy()
pre_df['imdb_votes'] = np.log(pre_df['imdb_votes'] + 1)
pre_df['tmdb_popularity'] = np.log(pre_df['tmdb_popularity'] + 1)
X_scaled = StandardScaler().fit_transform(pre_df[['imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score']])

# Training ulang
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
pre_df['cluster'] = kmeans.fit_predict(X_scaled)

# MLflow logging ulang
mlflow.set_experiment("KMeans Netflix Retrain")
mlflow.end_run()
with mlflow.start_run():
    mlflow.log_param("model", "KMeans")
    mlflow.log_param("clusters", 3)
    sil = silhouette_score(X_scaled, pre_df['cluster'])
    mlflow.log_metric("silhouette_retrain", sil)
    mlflow.sklearn.log_model(kmeans, "model_retrained")
