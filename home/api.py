from django.urls.base import clear_script_prefix
from ninja import NinjaAPI
from core.settings import BASE_DIR

import finviz
import itertools

import requests
import base64

# VBT
import sys
import os
import json

import pandas as pd
import numpy as np

from datetime import datetime
import vectorbt as vbt
import yfinance as yf



api = NinjaAPI()

@api.get("/test")
def test(request):
    return {'test': 'success'}


@api.get("/get_info")
def get_info(request, symbol: str):
    info_data = finviz.get_stock(symbol)

    return info_data


# ERRORS FIX LATER / USE VIEW METHOD INSTEAD

# @api.get("/get_logo")
# def get_logo(request, symbol: str):
#     logo_file = requests.get(f'https://eodhistoricaldata.com/img/logos/US/{symbol}.png')
#     logo = open(f"{symbol}_logo.png", "wb")
#     logo.write(logo_file.content)
#     logo.close()

#     logo_data = {}
#     with open(logo, mode='rb') as file:
#         img = file.read()
#     logo_data['img'] = base64.encodebytes(img).decode('utf-8')

#     return logo_data


@api.get("/get_news")
def get_news(request, symbol: str):
    info_data = finviz.get_news(symbol)

    return info_data


@api.get("/get_ohlcv")
def get_ohlcv(request, symbol: str):
    symbol_chart = vbt.YFData.download(symbol)

    cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    ohlcv = symbol_chart.get(cols)


    return ohlcv.to_json()
clear_script_prefix

# STRATEGY ENDPOINT
@api.get("/chart_rsi")
def chart_rsi(request, symbol: str):
    symbol_chart = vbt.YFData.download(symbol)

    closing_prices = symbol_chart.get('Close')

    rsi = vbt.RSI.run(closing_prices)
    plot = rsi.plot().to_json()
    
    return plot



# DEF CREATE STRATEGY("create_strategy/") 

