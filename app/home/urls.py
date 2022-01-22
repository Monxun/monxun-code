"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView, 
    VbtView, 
    BizView, LoadDataFrames, LoadCharts,
    MusView, SongSearch, SongSearchUpdate, AnalyzeSong,
    RegisterPage, SymbolUpdate, AnalysisView, RunBacktest,
    OHLCVUpdate, TrendsUpdate, RangingUpdate, EntryExitUpdate, OBVUpdate,
    LoginPage,
)

urlpatterns = [
    path('register/', RegisterPage, ),
    path('login/', LoginPage, ),

    path('', HomeView, name='home'),
    path('biz/', BizView, name='biz'),
    path('vbt/', VbtView, name='vbt'),
    path('mus/', MusView, name='mus'),
]

HTMX_PATTERNS = [
    # BIZ PARTIALS
    path('dataframes/', LoadDataFrames, name='load_dataframes'),
    path('charts/', LoadCharts, name='load_charts'),

    # MUS PARTIALS
    path('get_song_info/', SongSearch, name='get_song_info'),
    path('update_song_info/', SongSearchUpdate, name='update_song_info'),
    path('analyze_song/', AnalyzeSong, name='analyze_song'),

    # VBT PARTIALS
    path('vbt_symbol/', SymbolUpdate, name='vbt_symbol'),
    path('vbt_analysis/', AnalysisView, name='vbt_analysis'),
    path('vbt_run_backtest/', RunBacktest, name='vbt_run_backtest'),


    # VBT CHARTS
    path('vbt_ohlcv/', OHLCVUpdate, name='vbt_ohlcv'),
    path('vbt_trends/', TrendsUpdate, name='vbt_trends'),
    path('vbt_ranging/', RangingUpdate, name='vbt_ranging'),
    path('vbt_entry_exit/', EntryExitUpdate, name='vbt_entry_exit'),
    path('vbt_obv/', OBVUpdate, name='vbt_obv'),

]

urlpatterns += HTMX_PATTERNS