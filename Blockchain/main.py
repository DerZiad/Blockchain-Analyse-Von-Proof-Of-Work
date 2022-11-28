import hashlib

from numba import cuda

from SystemScanner import *


API_KEY = "QZvQvCGoiO_ln4v29ZSqTMLcSYw8bsoG"

import requests
import pandas as pd
import time

def get_crypto_prices(symbol, start, end):
    api_key = 'QZvQvCGoiO_ln4v29ZSqTMLcSYw8bsoG'
    api_url = f'https://api.polygon.io/v2/aggs/ticker/X:{symbol}USD/range/1/day/{start}/{end}?unadjusted=true&sort=asc&apiKey={api_key}'
    raw = requests.get(api_url).json()
    df = pd.DataFrame(raw['results']).set_index('t')[['o', 'h', 'l', 'c', 'v']]
    df = df.rename(columns = {'o':'open', 'h':'high', 'l':'low', 'c':'close', 'v':'volume'})
    df.index = pd.to_datetime(df.index, unit = 'ms')
    return df


actuelTime = int(time.time() * 1000)
raw = requests.get(f"https://blockchain.info/blocks/{actuelTime}?format=json")
print(raw.json())
