import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
bitcoin = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency = 'usd', days = 30)
data = pd.DataFrame(bitcoin['prices'], columns = ['TimeStamp', 'Price'])
data['TimeStamp'] = pd.to_datetime(data['TimeStamp'], unit = 'ms')
candlestick_data = data.groupby(data['TimeStamp'].dt.date).agg({'Price' : ['min', 'max', 'first', 'last']})

import plotly.graph_objects as go
import plotly

fig = go.Figure(
    data=[
        go.Candlestick(
            x=candlestick_data.index,
            open=candlestick_data['Price']['first'],
            high=candlestick_data['Price']['max'],
            low=candlestick_data['Price']['min'],
            close=candlestick_data['Price']['last']
        )
    ]
)

fig.update_layout(
    xaxis_rangeslider_visible=False,
    xaxis_title='Date',
    yaxis_title='Price (USD $)',
    title='Bitcoin Candlestick Chart Over Past 30 Days'
)

plotly.offline.plot(
    fig,
    filename='./bitcoin_candlestick_graph.html',
    auto_open=False
)
fig.show()