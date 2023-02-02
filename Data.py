import pandas as pd 
import numpy as np
import yfinance as yf


class Data:
    def __init__(self):
        # you can add more stocks in this list
        self.stocks = ['AAPL', 'SPY', 'QQQ', 'PLTR']
    
    # returns stocks list
    def getStocks(self):
        return self.stocks
    
    # returns a list of indicators
    def getIndicators(self):
        return ['Exponential moving average (EMA)',
                'Moving Average Convergence/Divergence Oscillator (MACD)',
                'Accumulation Distribution (A/D)',
                'On Balance Volume (OBV)',
                'Price-volume trend (PVT)',
                'Average true range (ATR)',
                'Bollinger Bands',
                'Chaikin Oscillator',
                'Typical Price',
                'Ease of Movement',
                'Mass Index',
                'Average directional movement index',
                'Money Flow Index (MFI)',
                'Negative Volume Index (NVI)',
                'Positive Volume Index (PVI)',
                'Momentum',
                'Relative Strenght Index (RSI)',
                'Chaikin Volatility (CV)',
                "William's Accumulation/Distribution",
                "William's % R",
                'TRIX',
                'Ultimate Oscillator']

    # returns OHLCV data from yfinance API
    def getData(self, start, end):
            data = yf.download(tickers = self.stocks, start=start, end=end, interval = '1d', 
                    group_by = 'ticker',  auto_adjust = True, repair = True)
            return data