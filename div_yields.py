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
from datetime import datetime

# Find info about individual stocks within the S&P500
html = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(html.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})
tickers = []
sectors = []
names = []
for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text.replace('.', '-') # Ticker symbol
    name = row.findAll('td')[1].text # Company Name
    sector = row.findAll('td')[2].text # GICS Sector Name
    ticker = ticker[:-1]
    tickers.append(ticker)
    names.append(name)
    sectors.append(sector)

# Create dataframe with basic info
df = pd.DataFrame({'tickers': tickers, 'name': names, 
                   'sectors': sectors},).set_index('tickers')

# Columns for yearly dividends
dividends = [0 for i in tickers]
for year in range(2010,2023):
    df[f'DIV{year}'] = dividends # Assign 0s and populate below
tickers = [ticker.replace('.','-') for ticker in tickers] # yfinance uses - instead of .
dt_format = "%Y-%m-%d"
for ticker in tickers:
    dividends = yf.Ticker(f"{ticker}").dividends
    new_index = dividends.index.strftime('%Y-%m-%d %H:%M:%S')
    dividends.index = pd.to_datetime(new_index, format=dt_format)
    for year in range(2010,2023):
        dividend = dividends.loc[dividends.index > datetime.strptime(f"{year}-01-01", dt_format)]
        dividend = dividend.sum()
        df[f'DIV{year}'][ticker] = dividend
        
    
df.to_csv("data/dividend_yields.csv")