import yfinance as yf
import pandas as pd

from dash import Dash, dcc, html
from dash.dependencies import Input, Output

import plotly.graph_objects as go

app = Dash(__name__)

app.layout = html.Div([

    html.H1("Live AAPL Stock Dashboard"),

    dcc.Graph(id='live-chart'),

    dcc.Interval(
        id='interval-component',
        interval=10*1000,   # refresh every 10 seconds
        n_intervals=0
    )
])

@app.callback(
    Output('live-chart', 'figure'),
    Input('interval-component', 'n_intervals')
)

def update_graph(n):

    data = yf.download(
        'AAPL',
        period='1d',
        interval='1m'
    )

    # Remove multilevel columns if needed
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close']
            )
        ]
    )

    fig.update_layout(
        xaxis_rangeslider_visible=False,
        title='AAPL Live Stock Price'
    )

    return fig

app.run(debug=True)