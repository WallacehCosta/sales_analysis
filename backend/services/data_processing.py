import pandas as pd
from backend.database import get_db
from backend.models.sales import Sale
from sqlalchemy.orm import Session

def load_sales_data(db: Session):
    """
    Carrega os dados de vendas do banco de dados PostgreSQL.
    """
    sales = db.query(Sale).all()
    sales_data = [
        {
            "id": sale.id,
            "product_name": sale.product_name,
            "quantity": sale.quantity,
            "price": sale.price,
            "total_amount": sale.total_amount,
            "sale_date": sale.sale_date,
        }
        for sale in sales
    ]
    return pd.DataFrame(sales_data)

def preprocess_sales_data(df: pd.DataFrame):
    """
    Pré-processa os dados de vendas:
    - Converte datas para o formato adequado.
    - Remove outliers (se necessário).
    - Adiciona novas features (se necessário).
    """
    # Converte a coluna de data para o tipo datetime
    df["sale_date"] = pd.to_datetime(df["sale_date"])

    # Exemplo: Adiciona uma coluna de mês e ano
    df["sale_month"] = df["sale_date"].dt.month
    df["sale_year"] = df["sale_date"].dt.year

    # Exemplo: Remove outliers (valores muito altos ou baixos)
    df = df[(df["total_amount"] > 0) & (df["total_amount"] < 10000)]

    return df

def save_processed_data(df: pd.DataFrame, collection_name: str = "processed_sales"):
    """
    Salva os dados processados no MongoDB.
    """
    from backend.database import get_mongo_db

    mongo_db = get_mongo_db()
    collection = mongo_db[collection_name]
    collection.insert_many(df.to_dict("records"))

def process_sales_pipeline(db: Session):
    """
    Pipeline completo para processamento de dados de vendas:
    1. Carrega os dados do PostgreSQL.
    2. Pré-processa os dados.
    3. Salva os dados processados no MongoDB.
    """
    df = load_sales_data(db)
    df = preprocess_sales_data(df)
    save_processed_data(df)
    return df
