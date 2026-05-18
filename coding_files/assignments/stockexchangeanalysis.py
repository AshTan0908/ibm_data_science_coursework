import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup

'''
apple = yf.Ticker('AAPL')
hist_data = apple.history(period='max')
#print(hist_data.head())
#print(apple.dividends)
#apple.dividends.plot()

import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"

response = requests.get(url)

with open("amd.json", "wb") as file:
    file.write(response.content)

print("Downloaded amd.json")

import json
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
#print(amd_info)
print(amd_info['country'])
print(amd_info['sector'])

amd = yf.Ticker('AMD')
h = amd.history(period='max')
print(h['Volume'])


import json
jd = data.to_json()
with open('apple.json', 'w') as jfile:
    jfile.write(jd)

#USING BEAUTIFULSOUP TO PARSE HTML DATA AND REPRESENT USING PANDAS

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data = requests.get(url).text
#print(data)
soup = BeautifulSoup(data, 'html.parser')
#print(soup)
netflix_data = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = pd.concat([netflix_data,pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)   
print(netflix_data.head())
'''
data = yf.download('AAPL', period='max')
data.columns = data.columns.droplevel(1)

data['Price Movement'] = data['Close'] - data['Open']
data['Market Trend'] = data['Price Movement'].apply(
    lambda x: 'Bullish' if x>0 else 'Bearish'
)

print(data)
import plotly
import plotly.graph_objects as go

fig = go.Figure(
    data = [
        go.Candlestick(
            x = data.index,
            open = data['Open'],
            close = data['Close'],
            high = data['High'],
            low = data['Low']
        )
    ]
)
fig.update_layout(
    xaxis_rangeslider_visible = False,
    xaxis_title='Time (in Years)',
    yaxis_title='Price per Share (in USD)',
    title='AAPL OHLC Stock Chart'
)
plotly.offline.plot(
    fig,
    filename = './aaplstock.html',
    auto_open = False
)
fig.show()