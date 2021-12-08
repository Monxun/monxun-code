from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .vbt_scripts import stocktwits_model
from .vbt_scripts.stocktwits_view import display_bullbear
from .vbt_scripts.vbt_view2 import GetStockData, RunBacktests

from home.forms import SymbolForm, BacktestForm
from home.models.vbt_models import Backtest

from rest_framework import generics
from home.serializers import BacktestSerializer

from .helpers import (
    CSVToDataFrame,
    MakeDataFrameJson, 
    MakeModelCSV, 
    ImportCSV, 
    TableExportCSV,
    )

import plotly.graph_objects as go


global symbol
global logo
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

global charts


symbol = 'GME'
symbol_data = []


####################################################################
# CUSTOM HELPERS

####################################################################
# VBT

def VbtView(request):
    form = SymbolForm

    template = 'vbt/vbt.html'

    context = {
        'symbol': symbol,
        'form': form,
    }

    return render(request, template, context)


def SymbolUpdate(request):
    global symbol 

    symbol = request.POST.get('symbol').upper()

    template = "partials/logo.html"

    context = {
        'symbol': symbol,
    }

    return render(request, template, context)

####################################################################
# ANALYSIS

def AnalysisView(request):

    global symbol
    global logo
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

    global charts

    form = BacktestForm

    symbol = request.POST.get('symbol').upper() # ADD TO FORMS.PY, MODELS.PY and TEMPLATE

    symbol_data = GetStockData(symbol=symbol)

    charts = symbol_data['charts']

    print(symbol_data['info'])
    print(symbol_data['news'])
    print(symbol_data['sentiment'])
    template = 'partials/vbt_analysis.html'

    context = {
        # GetStockData()
        'symbol': symbol,

        'info': symbol_data['info'],
        'insider': symbol_data['insider'],
        'news': symbol_data['news'],
        'targets': symbol_data['targets'],
        'sentiment': symbol_data['sentiment'],

        'volume': symbol_data['volume'],
        'closing_prices': symbol_data['closing_prices'],
        'ohlcv': symbol_data['ohlcv'],
        'charts': symbol_data['charts'],

        'chart_label': 'Closing Prices',

        'form': form,
    }

    return render(request, template, context)


####################################################################
# BACKTEST FORM

def RunBacktest(request):
    global symbol 

    backtest_entry = request.POST.get('backtest_entry')

    backtest_exit = request.POST.get('backtest_exit')


    init_cash = request.POST.get('init_cash')

    test = {
        'entry': backtest_entry,
        'exit': backtest_exit,
        'init_cash': init_cash,
    }

    results = RunBacktests(test=test)

    context = {
        'symbol': results['symbol'],
        'results': results['results'],
        'returns':results['returns'],
        'strategy': results['strategy'],
    }

    return render(request, 'partials/vbt_results.html', context)


####################################################################
# CHARTS

# OHLCV
def OHLCVUpdate(request):
    global symbol
    global charts

    context = {
        'symbol': symbol,
        'charts': charts, 
    }

    template = 'partials/chart-view.html'

    return render(request, template, context)


# TRENDS
def TrendsUpdate(request):
    global symbol
    global charts

    context = {
        'symbol': symbol,
        'charts': charts, 
    }

    template = 'partials/chart-view-trends.html'

    return render(request, template, context)


# RANGING
def RangingUpdate(request):
    global symbol
    global charts

    context = {
        'symbol': symbol,
        'charts': charts, 
    }

    template = 'partials/chart-view-ranging.html'

    return render(request, template, context)


# ENTRY/EXIT
def EntryExitUpdate(request):
    global symbol
    global charts

    context = {
        'symbol': symbol,
        'charts': charts, 
    }
    
    template = 'partials/chart-view-entry-exit.html'

    return render(request, template, context)


# OBV
def OBVUpdate(request):
    global symbol
    global charts

    context = {
        'symbol': symbol,
        'charts': charts, 
    }

    template = 'partials/chart-view-obv.html'

    return render(request, template, context)

##########################################################################



