import sys
import os

import pandas as pd
import numpy as np

from datetime import datetime
import vectorbt as vbt
import yfinance as yf

# GET DATA
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
