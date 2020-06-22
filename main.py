import yfinance as yf
import talib
from pprint import pprint as pp

class TS():
    df = None # None or pandas dataframe - standard from yahoo finance

    def __init__(self,df):
        self.df = df

    def to_dic(self):
        dic = {}
    
        for col in self.df.columns:
            dic[col] = self.df[col].values
        
        return dic

    def show(self):
        return self.df
        
    
        
class VAR():

    tickers = ['SPY', 'MSFT', 'AAPL'] #default tickers, should extend to load portfolio
    weights = [0.3, 0.2, 0.5]   # default weights
    prices = {}

    def download_data(self, period = '10y', interval = '1d'):
        
        for ticker in self.tickers:
            data = yf.download(ticker, period = period, interval=interval)
            self.prices[ticker] = TS(data)
        

if __name__ == "__main__":
    
    data = VAR()
    data.download_data()
    print (data.prices['SPY'].to_dic())
    

