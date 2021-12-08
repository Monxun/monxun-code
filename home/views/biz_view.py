from django.conf import settings
import os
import os.path
from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
import pandas as pd
from IPython.display import HTML

from .helpers import (
    CSVToDataFrame,
    MakeDataFrameJson, 
    MakeModelCSV, 
    ImportCSV, 
    TableExportCSV,
    )

media_dir = settings.MEDIA_ROOT 
static_dir = settings.STATIC_ROOT   


transactions = pd.read_csv(f'{media_dir}/data/transactions.csv', parse_dates=['date'])

oil = pd.read_csv(f'{media_dir}/data/oil.csv', parse_dates=['date'])

holidays = pd.read_csv(f'{media_dir}/data/holidays_events.csv', parse_dates=['date'])

test = pd.read_csv(f'{media_dir}/data/test.csv', parse_dates=['date'])
# In[ ]:


# NO DATE COLUMN - 'index_col=0' (index/id column)
stores = pd.read_csv(f'{media_dir}/data/stores.csv', index_col=0)

sample = pd.read_csv(f'{media_dir}/data/sample_submission.csv', index_col=0)

# LOAD DATAFRAMES

####################################################################

# LOAD CHART SVG
def BizView(request):

    # MONTHLY W/ FORECAST
    

    context = {

    }
    return render(request, 'biz/biz.html', context)

@csrf_exempt
def LoadDataFrames(request):

    template = 'partials/tabbed_view_data.html'
    context = {
        'train': train,
        'transactions': transactions,
        'oil': oil,
        'holidays': holidays,
        'stores': stores,

        'test': test,
        'sample': sample,
    }

    return render(request, template, context)


@csrf_exempt
def LoadCharts(request):
    
    template = 'partials/tabbed_view_charts.html'
    context = {
        
    }

    return render(request, template, context)


