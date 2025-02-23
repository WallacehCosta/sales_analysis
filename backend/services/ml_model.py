import pandas as pd
from pycaret.regression import setup, compare_models, pull, save_model, load_model
from backend.database import get_mongo_db
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def load_processed_data(collection_name: str = "processed_sales"):
    """
    Carrega os dados processados do MongoDB.
    """
    mongo_db = get_mongo_db()
    collection = mongo_db[collection_name]
    data = list(collection.find({}))
    return pd.DataFrame(data)

def train_sales_prediction_model():
    """
    Treina um modelo de Machine Learning para prever o total_amount das vendas.
    Usa PyCaret para automatizar o processo de modelagem.
    """
    # Carrega os dados processados
    df = load_processed_data()

    # Seleciona as features e o target
    features = ["quantity", "price", "sale_month", "sale_year"]
    target = "total_amount"

    # Configura o ambiente do PyCaret
    setup(data=df, target=target, session_id=123, normalize=True, transformation=True)

    # Compara modelos e seleciona o melhor
    best_model = compare_models()

    # Salva o modelo treinado
    save_model(best_model, "sales_prediction_model")

    return best_model

def predict_sales(model, new_data: pd.DataFrame):
    """
    Faz previsões usando o modelo treinado.
    """
    predictions = model.predict(new_data)
    return predictions

def evaluate_model(model, test_size: float = 0.2):
    """
    Avalia o modelo usando uma divisão de treino/teste.
    """
    df = load_processed_data()
    features = ["quantity", "price", "sale_month", "sale_year"]
    target = "total_amount"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    return mae
