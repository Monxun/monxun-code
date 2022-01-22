import sys
import os

import pandas as pd
import numpy as np

from datetime import datetime
import vectorbt as vbt
import yfinance as yf

symbol = 'GME'
symbol_price = vbt.YFData.download(symbol)

# FEATURES
closing_prices = symbol_price.get('Close')
volume =  symbol_price.get('Volume')

# INDICATORS
rsi = vbt.RSI.run(closing_prices)
obv = vbt.OBV.run(closing_prices, volume)
ma = vbt.MA.run(closing_prices, 200)
bb = vbt.BBANDS.run(closing_prices)

# SIGNALS
entries = rsi.rsi_below(30, crossover=True)
exits = rsi.rsi_above(70, crossover=True)

# BACKTEST
portfolio = vbt.Portfolio.from_signals(closing_prices, entries, exits, init_cash=10000)
# Get total return, reshape to symmetric matrix, and plot the whole thing

# PLOTTING
ma.plot().show()
obv.plot().show()
portfolio.plot().show()


def get_data(symbol):
    start = '2019-01-01 UTC'  # crypto is in UTC
    end = '2020-01-01 UTC'
    btc_price = vbt.YFData.download('BTC-USD', start=start, end=end).get('Close')

#################################################
# COMBINE MULTIPLE SYMBOLS
btc_price = vbt.YFData.download('BTC-USD').get('Close')
eth_price = vbt.YFData.download('ETH-USD').get('Close')

comb_price = btc_price.vbt.concat(eth_price,      # CONCATONATE ETH TO BTC
    keys=pd.Index(['BTC', 'ETH'], name='symbol'))
comb_price.vbt.drop_levels(-1, inplace=True)      # FORMAT 
