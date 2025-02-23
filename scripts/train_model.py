import pandas as pd
from pycaret.regression import setup, compare_models, save_model
from backend.services.data_processing import load_sales_data, preprocess_sales_data
from backend.database import get_db

def train_and_save_model():
    # Carrega os dados de vendas
    db = next(get_db())  # Obtém uma sessão do banco de dados
    df = load_sales_data(db)

    # Pré-processa os dados
    df = preprocess_sales_data(df)

    # Configura o ambiente do PyCaret
    setup(data=df, target="total_amount", session_id=123, normalize=True, transformation=True)

    # Compara modelos e seleciona o melhor
    best_model = compare_models()

    # Salva o modelo treinado
    save_model(best_model, "sales_prediction_model")

    print("Modelo treinado e salvo com sucesso!")

if __name__ == "__main__":
    train_and_save_model()
    