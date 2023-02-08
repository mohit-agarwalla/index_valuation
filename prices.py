import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import yfinance as yf
import bs4 as bs
import pickle
import requests

# Set proxies
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

# Find companies within the S&P500
html = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(html.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})
tickers = []
for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text
    ticker = ticker[:-1]
    tickers.append(ticker)

# print(tickers)
# # yFinance
tickers = [ticker.replace('.','-') for ticker in tickers] # yfinance uses - instead of .
snp = yf.Ticker("^GSPC")
prices = []
weightings = []
for ticker in tickers:
    # Add current price
    prices += [yf.Ticker(f"{ticker}").history()['Close'].iloc[-1]]
    stock = yf.Ticker(ticker)
    market_cap = stock.info['marketCap']
    weightings += [market_cap/snp.info['marketCap']]
    

prices = pd.DataFrame({'ticker': tickers,
                       'last close': prices}).set_index('ticker')

# print(prices)

dividends = snp.info
print(dividends)