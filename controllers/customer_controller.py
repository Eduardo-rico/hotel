import pandas as pd
from models.model_loader import load_model_from_db

# Cargar el modelo al iniciar el controlador
model = load_model_from_db()

def predict_customer_type(input_data):
    input_df = pd.DataFrame([input_data.dict()])
    prediction = model.predict(input_df)
    return prediction
