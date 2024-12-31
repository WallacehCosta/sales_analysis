import matplotlib.pyplot as plt
from matplotlib.pyplot import title


def plot_sales_by_product(df):
    sales_by_product = df.groupby('Produto')['Valor Total da Venda'].sum().sort_values(ascending=False)
    sales_by_product.plot(kind='bar', title='Vendas por Produto')
    plt.ylabel('Valor Total da Venda')
    plt.show()
