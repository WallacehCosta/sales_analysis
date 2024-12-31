import dash
from dash import dcc, html
import plotly.express as px
from matplotlib.pyplot import figure
from src.app import df

from src.vizualization import plot_sales_by_product

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Análise de Vendas'),
    dcc.Graph(figure=plot_sales_by_product(df))

])

if __name__ == '__main__':
    app.run_server(debug=True)
