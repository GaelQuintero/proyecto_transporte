def save_results(data, path="outputs/clusters.csv"):
    data.to_csv(path, index=False)
