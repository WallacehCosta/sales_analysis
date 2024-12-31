import pandas as pd

def total_sales_by_month(df):
    df['Month'] = df['Data da Venda'].dt.to_period('M')
    sales_per_month = df.groupby('Month')['Valor Total da Venda'].sum()
    return sales_per_month
