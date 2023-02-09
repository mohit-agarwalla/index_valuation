### NEED TO FIND HOW TO GET DIVIDEND HISTORY BUT PROMISING API

import numpy as np
import pandas as pd
import requests
import json
from alpha_vantage.alphavantage import

api_key = "QIOGYHSUFX6RRQ9Y"

ticker = "AAPL"
endpoint = f"https://www.alphavantage.co/query?function=DIVIDEND_HISTORY&symbol={ticker}&apikey={api_key}&adjusted=true"

response = requests.get(endpoint)
data = response.json()
print(data)
