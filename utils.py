import pandas as pd
import numpy as np
import yfinance as yf
import yahooquery as yq
import csv
import os

# Check and update the tickers within the SP500 using wiki library
def SP500_tickers_update():
    tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    sp500 = tables[0]['Symbol'].tolist()
    sp500 = [symbol.replace(".", "-") for symbol in sp500] # yahoo finance uses - not .
    loc = "data/SP500_tickers.csv"
    with open(loc, 'w', newline="") as file:
        writer = csv.writer(file)
        for row in sp500:
            writer.writerow([row])
    print(f"Data Acquisition Completed: Data can be found at {loc}")

# CURRENTLY DEFUNCT, DO NOT USE
def SP500_tickers(update=False, loc="data/SP500_tickers.csv"):
    # Update from wiki library if asked for and create file if it does not already exist
    if update or (not os.path.exists(os.path.dirname(loc))):
        SP500_tickers_update()
        
    return tickers
    
    