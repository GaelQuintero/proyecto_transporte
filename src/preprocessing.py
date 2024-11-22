from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(data):
    # Codificar columnas categóricas
    label_encoder = LabelEncoder()
    data['transportation'] = label_encoder.fit_transform(data['transportation'])
    data['gender'] = label_encoder.fit_transform(data['gender'])
    
    # Escalar datos
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[['age', 'travelDuration', 'travelCost', 'transportation']])
    return scaled_data
