import yfinance as yf
from talib import abstract as ta
import talib
from pprint import pprint as pp

class TS():
    df = None # None or pandas dataframe - standard from yahoo finance
    default_values = ['open', 'high', 'low', 'close','volume']

    def __init__(self,df):
        self.df = df

    def to_dic(self):
        dic = {}
    
        for col in self.default_values:
            dic[col] = self.df[col.capitalize()].values
        
        return dic

    def show(self):
        return self.df
        
    
        
class VAR():

    tickers = ['SPY', 'MSFT', 'AAPL'] #default tickers, should extend to load portfolio
    weights = [0.3, 0.2, 0.5]   # default weights
    prices = {}
    ta = {i:{} for i in tickers}

    def download_data(self, period = '10y', interval = '1d'):
        
        for ticker in self.tickers:
            data = yf.download(ticker, period = period, interval=interval)
            self.prices[ticker] = TS(data)


    def add_ta(self):
        # quick usage of talib with default indicators

        def getprops(cls):   
            return [i for i in cls.__dict__.keys() if i[:1] != '_']

        properties = getprops(talib)

        for prop in properties:
            if prop[0].isupper(): ## likely the function
                for ticker in self.tickers:
                    try:
                        abstract_func = getattr(ta, prop)
                        #func = getattr(talib, prop)
                        res = abstract_func (self.prices[ticker].to_dic())
                        self.ta[ticker][prop] = res

                    except (AttributeError, TypeError, Exception):
                        pass

    
        

if __name__ == "__main__":
    
    data = VAR()
    data.download_data()
    data.add_ta()

