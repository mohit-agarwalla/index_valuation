# yfinance Ticker.info is down (:-/)
"""
yfinance.info was to be used for most of the code below but web scraping and using requests 
from the wikipedia page and table to find some of the information regarding the index, in 
particular the ticker names and GICS sectors

It would be easier to simply use yf.Ticker({"INDEX"}).info(constituents)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import yfinance as yf
import bs4 as bs
import requests


# Find companies within the S&P500
html = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(html.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})
tickers = []
sectors = []
for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text # Ticker symbol
    sector = row.findAll('td')[2].text # GICS Sector Name
    ticker = ticker[:-1]
    tickers.append(ticker)
    sectors.append(sector)

df = pd.DataFrame({'tickers': tickers, 'sectors': sectors},).set_index('tickers')
dividends = [0 for i in tickers]
for year in range(2010,2023):
    df[f'DIV{year}'] = dividends
sectors = np.unique(sectors)
print(sectors)
tickers = [ticker.replace('.','-') for ticker in tickers] # yfinance uses - instead of .
snp = yf.Ticker("^GSPC")
prices = []
weightings = []
for ticker in tickers:
    dividends = yf.Ticker(f"{ticker}").dividends
    dividends = dividends[dividends.index > "2000-01-01"]
    df[ticker] = dividends.sum()
    
    
print(df)
    

# print(prices)

dividends = snp.info
print(dividends)