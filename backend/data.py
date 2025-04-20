import yfinance as yf
import pandas as pd

def fetch_data(tickers, start_date, end_date):
    
    #Fetch OHLC data from yahoo finance
    return yf.download(tickers, start_date, end_date)

#local fetch_data call test
#res = fetch_data('MSFT','2015-01-01','2024-12-31')
#print(res)