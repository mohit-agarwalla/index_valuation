import requests
import json

def dividend(ticker):
    endpoint = f"https://finance.yahoo.com/quote/{ticker}/history?p={ticker}"
    response = requests.get(endpoint)
    data = response
    print(data)

dividend("MSFT")