# FINVIZ, STOCKTWITZ
import finviz
import itertools

from .stocktwits_view import display_bullbear
from .stocktwits_model import get_bullbear

# VBT
import sys
import os
import json

import pandas as pd
import numpy as np

from datetime import datetime
import vectorbt as vbt
import yfinance as yf

from core.settings import BASE_DIR

from home.models.vbt_models import Backtest

#########################################
# FINVIZ

global symbol
symbol = 'GME' # MAIN SYMBOL SELECTOR

def GetStockData(symbol):

    # FOR AnalysisView(request) ######


    global info
    global news
    global insider
    global targets

    global closing_prices
    global volume
    global ohlcv

    global rsi
    global obv
    global ma
    global bb

    info_data = finviz.get_stock(symbol)
    # {'Index': 'DJIA S&P500', 'P/E': '12.91', 'EPS (ttm)': '12.15',...
    insider = finviz.get_insider(symbol)
    # [{'Insider Trading': 'KONDO CHRIS', 'Relationship': 'Principal Accounting Officer', 'Date': 'Nov 19', 'Transaction':            'Sale', 'Cost': '190.00', '#Shares': '3,408', 'Value ($)': '647,520', '#Shares Total': '8,940', 'SEC Form 4': 'Nov 21           06:31 PM'},...
    news = finviz.get_news(symbol)
    # [('Chinas Economy Slows to the Weakest Pace Since 2009', 'https://finance.yahoo.com/news/china-economy-slows-weakest-pace-      020040147.html'),...
    targets_data = finviz.get_analyst_price_targets(symbol)
    # [{'date': '2019-10-24', 'category': 'Reiterated', 'analyst': 'UBS', 'rating': 'Buy', 'price_from': 235, 'price_to': 275}, ...

    sentiment = display_bullbear(ticker=symbol)

    symbol_chart = vbt.YFData.download(symbol)

    cols = ['Open', 'High', 'Low', 'Close', 'Volume']

    ohlcv = symbol_chart.get(cols)

    closing_prices = symbol_chart.get('Close')
    volume =  symbol_chart.get('Volume')

    data = {
        'info': info_data,
        'news': news,
        'insider': insider,
        'targets': targets_data,
    }

    # {% for i in data[info] %}
        # <p>{{ i.title }}</p>
        # <p>{{ i.url }}</p>
        # <p>{{ i.description }}</p>
        #<br>
    # {% endfor %}

    #######################################################################
    # DATA OBJECT ITERATION / JSON

    # PLAIN DICTIONARY ITERATION {'key': value,...}
    # returns: dictionary
    info = {}
    for key, value in data['info'].items():
        info[key] = value

    # LIST NESTED DICTIONARIES ITERATION [{'key': value,...}, ...]
    # returns:list of dictionaries
    # insider = data['insider']
    
    # LIST OF LISTS [['A', '2', 3], ...] 
    # returns: list of tuples
    # news = data['news'] 
    
    # LIST NESTED DICTIONARIES ITERATION [{'key': value,...}, ...]
    # returns:list of dictionaries
    targets = []
    for i in data['targets']:
        dict = {}
        for key, value in i.items():
            dict[key] = value
        targets.append(dict)


    ###########################################
    # INDICATOR DICTS
    """
    use by calling: variable_name = indicator_dict['rsi']()
    """

    # params = {
    #     'rsi': [target_feature],
    #     'obv': [target_feature, volume],
    #     'ma': [target_feature, ma_window],
    #     'bb': [target_feature],
    # }

    # indicator_dict = {
    #     'rsi': vbt.RSI.run(*params['rsi']),
    #     'obv': vbt.OBV.run(*params['obv']),
    #     'ma': vbt.MA.run(*params['ma']),
    #     'bb': vbt.BBANDS.run(*params['bb']),
    # }

    #######################################################################
    # CREATE INDICATORS

    rsi = vbt.RSI.run(closing_prices)
    obv = vbt.OBV.run(closing_prices, volume)
    ma = vbt.MA.run(closing_prices, 200)
    bb = vbt.BBANDS.run(closing_prices)

    # ohlcv_plot = ohlcv.plot()
    # rsi_plot = rsi.plot()



    # close_plot = closing_prices.plot()
    # volume_plot = volume.plot()
    # obv_plot = obv.plot()
    # rsi_plot = rsi.plot()
    # bb_plot = bb.plot()
    # ma_plot = ma.plot()

    plotly_config = {'responsive': True}

    ohlcv_html = ohlcv.vbt.ohlcv.plot().to_html(full_html=False, include_plotlyjs=False)
    trends_html = rsi.plot().to_html(full_html=False, include_plotlyjs=False)
    ranging_html = bb.plot().to_html(full_html=False, include_plotlyjs=False)
    entry_exit_html = ma.plot().to_html(full_html=False, include_plotlyjs=False)
    obv_html = obv.plot().to_html(full_html=False, include_plotlyjs=False)



    charts = {
        'ohlcv': ohlcv_html,
        'trends': trends_html,
        'ranging': ranging_html,
        'entry_exit': entry_exit_html,
        'obv': obv_html,
    }

    #######################################################################
    # OUTPUT CLEANED DATA

    cleaned_data = {
        'info': info,
        'insider': insider,
        'news': news,
        'targets': targets,
        'sentiment': sentiment,
        'volume': volume,
        'closing_prices': closing_prices,
        'ohlcv': ohlcv,
        'charts': charts,
    }

    return cleaned_data




############################################
# STRATEGY

# PASS SAVED BACKTEST STRATEGY AS TEST "for test in backtest: ...""
def InitBacktest(test):

    # FOR AnalysisView(request) ######

    init_cash = test.init_cash

    target_feature = 'closing_prices' # OPTION IN GUI: CLOSE / SENTIMENT / VOL

    entry_level = 20
    entry_ma_window = 200

    exit_level = 20
    exit_ma_window = test.exit_ma_window
    exit_price = test.exit_price # OPTION IN GUI

    ############################################
    # LOAD STRATEGY

    # COLLECT EVERYTHING
    backtest_data = {
        'target': target_feature,
        'indicators': indicators,
        'entries': entries,
        'exits': exits,
        'init_cash': init_cash,

    }

    return backtest_data

    ###########################################
    # RESULTS

###################################################################################

def RunBacktests(test):

    # GRAB GLOBAL DATA
    global symbol
    global closing_prices
    global volume

    print(test['entry'])
    print(test['exit'])
    print(test['init_cash'])

    init_cash = int(test['init_cash'])

    # ENTRY/EXIT DICTS
    # entries_dict = {
    #     'rsi': rsi.rsi_below(30, crossover=True),
    #     'obv': obv.obv_above(150000, crossover=True),
    #     'sma': ma.ma_above(closing_prices, crossover=True),
    # }

    # exits_dict = {
    #     'rsi': rsi.rsi_above(70, crossover=True),
    #     'obv': obv.obv_below(150000, crossover=True),
    #     'sma': ma.ma_below(closing_prices, crossover=True),
    # }

    ##########################################################################
    # ENTRIES
    if test['entry'] == 'rsi':
        entries = rsi.rsi_below(30, crossover=True)

    elif test['entry'] == 'obv':
        entries = obv.obv_above(150000, crossover=True)

    else:
        entries = ma.ma_above(closing_prices, crossover=True)


    ##########################################################################
    # EXITS
    if test['exit'] == 'rsi':
        exits = rsi.rsi_above(70, crossover=True)

    elif test['exit'] == 'obv':
        exits = obv.obv_below(150000, crossover=True)

    else:
        exits = ma.ma_below(closing_prices, crossover=True)
    

    ##########################################################################
    # BACKTEST

    print(entries)
    print(exits)

    portfolio = vbt.Portfolio.from_signals(closing_prices, entries, exits, init_cash=init_cash)

    report_plots = portfolio.plot().to_html(full_html=False, include_plotlyjs=False)
    return_plot = portfolio.total_return()

    results = {
        'symbol': symbol,
        'results': report_plots,
        'returns': return_plot,
        'strategy': test,
        # ADD MORE
    }   

    return results