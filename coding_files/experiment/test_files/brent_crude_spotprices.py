import pandas as pd
import requests

url = "https://api.eia.gov/v2/petroleum/pri/spt/data/?frequency=daily&data[0]=value&start=2026-04-01&end=2026-05-01&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"
params = {
    "frequency": "daily",
    "data[0]": "value",
    "start": "2026-04-01",
    "end": "2026-05-01",
    "api_key": "3pJRg1JvR1g7cWxlmw3eKFLfcpLv9QhK5eTC3s6K"
}

r = requests.get(url, params=params)
data = r.json()
print(data)


df = pd.DataFrame(data['response']['data'])
brent_data = df[[df['series']=='RBRTE'], columns=['Date', 'Price ($/bbl)']]

print(brent_data)
