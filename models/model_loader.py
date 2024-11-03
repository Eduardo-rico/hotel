import os
import psycopg2
import joblib
import io
from dotenv import load_dotenv

load_dotenv()


def load_model_from_db(model_name='SVM'):
    valid_model_names = ['KNN', 'Random Forest', 'SVM', 'XGBoost']  
    if model_name not in valid_model_names:
        raise ValueError(f"Invalid model name. Please choose one of the following: {valid_model_names}")

    database_url = os.getenv("DATABASE_URL")

    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()
    cursor.execute("SELECT model_data FROM models WHERE model_name = %s", (model_name,))
    model_data = cursor.fetchone()[0]
    model = joblib.load(io.BytesIO(model_data))
    cursor.close()
    connection.close()
    return model
