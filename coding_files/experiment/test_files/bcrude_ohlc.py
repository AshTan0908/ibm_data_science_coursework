import yfinance as yf

data = yf.download('BZ=F', period = 'max')
print(data.head())
print(data.shape)
#candlestick_data = data.groupby(data['Price Ticker Date'].dt.date).agg({'Price':['min', 'max','first','low']})
# yfinance already provides ohlc data, so no need to use groupby function
import plotly
import plotly.graph_objects as go
fig1 = go.Figure(
    data = [
        go.Candlestick(
            x=data.index,
            open=data['Open']['BZ=F'],
            high=data['High']['BZ=F'],
            low=data['Low']['BZ=F'],
            close=data['Close']['BZ=F']
        )
    ]
)
fig1.update_layout(
    xaxis_rangeslider_visible=False,
    xaxis_title='Date',
    yaxis_title='Price ($/bbl)',
    title='Brent Crude OHLC Price Chart'
)
plotly.offline.plot(
    fig1,
    filename='./bcrude_candlestick_graph.html',
    auto_open=False
)
fig1.show()