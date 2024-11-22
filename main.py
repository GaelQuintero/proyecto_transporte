from src.data_loading import load_data
from src.preprocessing import preprocess_data
from src.clustering import run_kmeans
from src.visualization import plot_clusters
import pandas as pd

# 1. Cargar datos
user_information,use_transport,routes = load_data()

# 2. Integrar datos
data = pd.merge(use_transport,user_information, on="idUser")
data = pd.merge(data, routes, on="idRoute")

# 3. Preprocesar datos
X = preprocess_data(data)

# 4. Aplicar clustering
clusters = run_kmeans(X, n_clusters=3)

# 5. Visualizar resultados
plot_clusters(X, clusters)

# 6. Guardar resultados
data['Cluster'] = clusters
data.to_csv("outputs/clusters.csv", index=False)
