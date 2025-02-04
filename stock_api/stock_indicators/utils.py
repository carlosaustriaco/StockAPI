import yfinance as yf

def fetch_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period='1d')
