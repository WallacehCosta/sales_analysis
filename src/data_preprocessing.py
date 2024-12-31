import pandas as pd

def prepocess_data(file_path):
    df = pd.read_csv(file_path)
    df['Data da Venda'] = pd.to_datetime(df['Data da Venda'])
    df = df.dropna()
    return df
