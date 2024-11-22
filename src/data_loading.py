import pandas as pd

def load_data():
    user_information = pd.read_csv("data/raw/user_information.csv")
    use_transport = pd.read_csv("data/raw/use_transport.csv")
    routes = pd.read_csv("data/raw/routes.csv")
    return user_information, use_transport, routes
