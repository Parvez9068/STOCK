# import requests

# API_KEY = 'NBOOQI8HVRVFIVL4'
# BASE_URL = 'https://www.alphavantage.co/query'

# def fetch_stock_data(symbol):
#     response = requests.get(f'{BASE_URL}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}')
#     if response.status_code == 200:
#         data = response.json()
#         return data['Time Series (Daily)']
#     return None
