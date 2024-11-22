import matplotlib.pyplot as plt

def plot_clusters(X, clusters, output_path="outputs/cluster_plot.png"):
    """
    Visualiza los clusters y guarda la gráfica en un archivo.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', alpha=0.7)
    plt.title("Clusters")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.colorbar(label="Cluster")
    
    # Guardar la gráfica
    plt.savefig(output_path)
    print(f"Gráfica de clusters guardada en {output_path}")
