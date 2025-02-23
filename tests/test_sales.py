import pytest
from backend.services.data_processing import load_sales_data, preprocess_sales_data, save_processed_data, process_sales_pipeline
from backend.database import get_db
from sqlalchemy.orm import Session

def test_load_sales_data():
    """
    Testa a função load_sales_data.
    """
    db = next(get_db())
    df = load_sales_data(db)
    assert not df.empty, "Os dados de vendas não devem estar vazios"

def test_preprocess_sales_data():
    """
    Testa a função preprocess_sales_data.
    """
    db = next(get_db())
    df = load_sales_data(db)
    processed_df = preprocess_sales_data(df)
    assert "sale_month" in processed_df.columns, "A coluna sale_month deve existir após o pré-processamento"
    assert "sale_year" in processed_df.columns, "A coluna sale_year deve existir após o pré-processamento"

def test_save_processed_data():
    """
    Testa a função save_processed_data.
    """
    db = next(get_db())
    df = load_sales_data(db)
    processed_df = preprocess_sales_data(df)
    save_processed_data(processed_df)
    # Verifica se os dados foram salvos no MongoDB (opcional)
    from backend.database import get_mongo_db
    mongo_db = get_mongo_db()
    collection = mongo_db["processed_sales"]
    saved_data = list(collection.find({}))
    assert len(saved_data) > 0, "Os dados processados devem ser salvos no MongoDB"

def test_process_sales_pipeline():
    """
    Testa o pipeline completo de processamento de dados.
    """
    db = next(get_db())
    df = process_sales_pipeline(db)
    assert not df.empty, "O pipeline deve retornar um DataFrame não vazio"
