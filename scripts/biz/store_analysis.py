import os
import os.path
import pandas as pd
import numpy as np
import seaborn as sns

# %config InlineBackend.figure_format = 'retina'
import warnings
import itertools
import mpld3
from django.http import HttpResponse
from io import StringIO
import matplotlib.pyplot as plt
import lightgbm as lgb
from pylab import rcParams
from sklearn.metrics import mean_squared_log_error
from statsmodels.tsa.seasonal import seasonal_decompose
from pathlib import Path

sns.set()

rcParams['figure.figsize'] = 18, 8
rcParams['figure.figsize'] = 18, 8

from sktime.forecasting.base import ForecastingHorizon
from sktime.transformations.series.detrend import Deseasonalizer, Detrender
from sktime.forecasting.trend import PolynomialTrendForecaster
from sktime.forecasting.model_selection import (
    temporal_train_test_split,
)
from sktime.utils.plotting import plot_series
from sktime.forecasting.compose import (
    TransformedTargetForecaster,
    make_reduction
)

ROOT_PATH = Path(__file__).resolve().parent
DATA_DIR = 'data' # CHANGED SINCE RUNNNING BY DEVELOPER
# os.path.join(ROOT_PATH, 'data')


#################################################################################
def graph_svg(fig, name):

    if os.path.exists(f'/graphs/{name}.svg'):
        graph_svg = open(f'/graphs/{name}.svg', "r")
        return graph_html
    else:
        mpld3.save_html(fig,f"{name}.html")
        mpld3.fig_to_html(fig,template_type="simple")
        graph_html = mpld3.fig_to_html(fig)
        return graph_html


#################################################################################

train = pd.read_csv(f'{DATA_DIR}/train.csv', parse_dates=['date'])
transactions = pd.read_csv(f'{DATA_DIR}/transactions.csv', parse_dates=['date'])
oil = pd.read_csv(f'{DATA_DIR}/oil.csv', parse_dates=['date'])
holidays = pd.read_csv(f'{DATA_DIR}/holidays_events.csv', parse_dates=['date'])
test = pd.read_csv(f'{DATA_DIR}/test.csv', parse_dates=['date'])


# In[ ]:


# NO DATE COLUMN - 'index_col=0' (index/id column)
stores = pd.read_csv(f'{DATA_DIR}/stores.csv', index_col=0)
sample = pd.read_csv(f'{DATA_DIR}/sample_submission.csv', index_col=0)


#################################################################################

# # W/ DATE COLUMN - 'parse_dates='date' (date column)


# train = pd.read_csv(f'{DATA_DIR}/train.csv', parse_dates=['date'])
# transactions = pd.read_csv(f'{DATA_DIR}/transactions.csv', parse_dates=['date'])
# oil = pd.read_csv(f'{DATA_DIR}/oil.csv', parse_dates=['date'])
# holidays = pd.read_csv(f'{DATA_DIR}/holidays_events.csv', parse_dates=['date'])
# test = pd.read_csv(f'{DATA_DIR}/test.csv', parse_dates=['date'])


# # NO DATE COLUMN - 'index_col=0' (index/id column)
# stores = pd.read_csv(f'{DATA_DIR}/stores.csv', index_col=0)
# sample = pd.read_csv(f'{DATA_DIR}/sample_submission.csv', index_col=0)

#################################################################################

export_period = 'M' # DAILY / MOTHLY / YEARLY

#For the sake of demonstration, we will train our model on monthly aggregated Sales data of a particular store# Select sales for Store 1 Only.
store1_agg = train.loc[train['store_nbr']==1].groupby(['date'])['sales'].sum()
store1_agg.index = pd.to_datetime(store1_agg.index)
#Aggregate the Data on a Monthly basis.
store1_agg_monthly = store1_agg.resample(export_period).sum()


#################################################################################
# #For the sake of demonstration, we will train our model on monthly aggregated Sales data of a particular store# Select sales for Store 1 Only.
#     store1_agg = train.loc[train['store_nbr']==1].groupby(['date'])['sales'].sum()
#     store1_agg.index = pd.to_datetime(store1_agg.index)
#     #Aggregate the Data on a Monthly basis.
#     store1_agg_monthly = store1_agg.resample('M').sum()



#--------------------Visulaize Data on a Time Plot------------------
monthly_graph = sns.lineplot(
    data=store1_agg_monthly, 
)
plt.title("Store-1 Sales Data aggreagted at Month Level")
month_fig = monthly_graph.get_figure()
month_fig.savefig(f'graphs/{export_period}_sales.svg') # SEABORN
monthly_plot = open(f"graphs/{export_period}_sales.svg", "r")
# monthly sales var
# monthly_plot = graph_svg(month_fig, 'monthly')


# monthly_graph = sns.lineplot(
#     data=store1_agg_monthly, 
# )
# plt.title("Store-1 Sales Data aggreagted at Month Level")
# month_fig = monthly_graph.get_figure()
# # monthly sales var
# monthly_plot = graph_svg(month_fig, 'monthly')

#################################################################################


#Annual Seasonal Decomposition
seasonal_graph = seasonal_decompose(store1_agg_monthly,model="multiplicative",period=12).plot()
seasonal_fig = seasonal_graph.get_figure()
seasonal_fig.savefig(f'graphs/{export_period}_seasonal.svg')
seasonal_plot = open(f"graphs/{export_period}_seasonal.svg", "r")

# #Annual Seasonal Decomposition
# seasonal_graph = seasonal_decompose(store1_agg_monthly,model="multiplicative",period=12).plot()
# seasonal_fig = seasonal_graph.get_figure()
# seasonal_plot = graph_svg(seasonal_fig, 'seasonal')


#################################################################################


#--------------------Time Series Train-Test split-------------------#
store1_agg_monthly.index = store1_agg_monthly.index.to_period(export_period) 
y_train, y_test = temporal_train_test_split(store1_agg_monthly, test_size=0.2)


# #--------------------Time Series Train-Test split-------------------#
# store1_agg_monthly.index = store1_agg_monthly.index.to_period('M') 
# y_train, y_test = temporal_train_test_split(store1_agg_monthly, test_size=0.2)


#################################################################################
    

#--------------------------Detrender-----------------------------

#degree=1 for Linear
forecaster = PolynomialTrendForecaster(degree=1) 
transformer = Detrender(forecaster=forecaster)

#Get the residuals after fitting a linear trend
y_resid = transformer.fit_transform(y_train)

# Internally, the Detrender uses the in-sample predictions
# of the PolynomialTrendForecaster
forecaster = PolynomialTrendForecaster(degree=1)
fh_ins = -np.arange(len(y_train))  # in-sample forecasting horizon
y_pred = forecaster.fit(y_train).predict(fh=fh_ins)
detrender_fig, _ = plot_series(y_train, y_pred, y_resid, labels=["y_train", "fitted linear trend", "residuals"])
detrender_fig.savefig(f'graphs/{export_period}_detrender.svg') # PLOTLY
detrender_plot = open(f"graphs/{export_period}_detrender.svg", "r")


# #degree=1 for Linear
# forecaster = PolynomialTrendForecaster(degree=1) 
# transformer = Detrender(forecaster=forecaster)

# #Get the residuals after fitting a linear trend
# y_resid = transformer.fit_transform(y_train)

# # Internally, the Detrender uses the in-sample predictions
# # of the PolynomialTrendForecaster
# forecaster = PolynomialTrendForecaster(degree=1)
# fh_ins = -np.arange(len(y_train))  # in-sample forecasting horizon
# y_pred = forecaster.fit(y_train).predict(fh=fh_ins)
# detrender_fig, _ = plot_series(y_train, y_pred, y_resid, labels=["y_train", "fitted linear trend", "residuals"])
# detrender_plot = graph_svg(detrender_fig, 'detrender')

#################################################################################



#--------------------------Deseasonalizer---------------------------

#Multiplicative Deseasonalizer, period = 12(for Monthly Data)
deseasonalizer = Deseasonalizer(model="multiplicative", sp=12)
deseasonalizer_fig, _ = plot_series(deseasonalizer.fit_transform(y_train))
deseasonalizer_fig.savefig(f'graphs/{export_period}_deseasonalizer.svg')
deseasonalizer_plot = open(f'graphs/{export_period}_deseasonalizer.svg', "r")

deseasonalizer.fit_transform(y_train)


# #--------------------------Deseasonalizer---------------------------

# #Multiplicative Deseasonalizer, period = 12(for Monthly Data)
# deseasonalizer = Deseasonalizer(model="multiplicative", sp=12)
# deseasonalizer_fig, _ = plot_series(deseasonalizer.fit_transform(y_train))
# deseasonalizer_plot = graph_svg(deseasonalizer_fig, 'desason')
# deseasonalizer.fit_transform(y_train)


#################################################################################


regressor = lgb.LGBMRegressor()
forecaster = make_reduction(
                    #hyper-paramter to set recursive strategy
                    estimator=regressor, window_length=4,strategy="recursive" 
)


# regressor = lgb.LGBMRegressor()
# forecaster = make_reduction(
#                     #hyper-paramter to set recursive strategy
#                     estimator=regressor, window_length=4,strategy="recursive" 
# )



#################################################################################
#----------------------------Create Pipeline--------------------


    
#Initialize Light GBM Regressor
def get_transformed_target_forecaster(alpha,params):   
    regressor = lgb.LGBMRegressor(alpha = alpha,**params)

#-----------------------Forecaster Pipeline-----------------

#1.Separate the Seasonal Component.
#2.Fit a forecaster for the trend.
#3.Fit a Autoregressor to the resdiual(autoregressing on four historic values).

    forecaster = TransformedTargetForecaster(
        [
            ("deseasonalise", Deseasonalizer(model="multiplicative", sp=12)),
            ("detrend", Detrender(forecaster=PolynomialTrendForecaster(degree=1))),
            (
                # Recursive strategy for Multi-Step Ahead Forecast.
                # Auto Regress on four previous values
                "forecast",
                make_reduction(
                    estimator=regressor, window_length=4, strategy="recursive",
                ),
            ),
        ]
    )
    return forecaster

#################################################################################

#-------------------Fitting an Auto Regressive Light-GBM------------

#Setting Quantile Regression Hyper-parameter.
params = {
    'objective':'quantile'
}
#A 10 percent and 90 percent prediction interval(0.1,0.9 respectively).
quantiles = [.1, .5, .9] #Hyper-parameter "alpha" in Light GBM#Capture forecasts for 10th/median/90th quantile, respectively.
forecasts = []#Iterate for each quantile.
for alpha in quantiles:
    
    forecaster = get_transformed_target_forecaster(alpha,params)
    
    #Initialize ForecastingHorizon class to specify the horizon of forecast
    fh = ForecastingHorizon(y_test.index, is_relative=False)
    
    #Fit on Training data.
    forecaster.fit(y_train)
    
    #Forecast the values.
    y_pred = forecaster.predict(fh)
    
    #List of forecasts made for each quantile.
    y_pred.index.name="date"
    y_pred.name=f"predicted_sales_q_{alpha}"
    forecasts.append(y_pred)
    
#Append the actual data for plotting.
store1_agg_monthly.index.name = "date"
store1_agg_monthly.name = "original"
forecasts.append(store1_agg_monthly)


# In[ ]:


error = mean_squared_log_error(y_test, y_pred)


# In[ ]:



#-------------------Final Plotting of Forecasts------------------

plot_data = pd.melt(pd.concat(forecasts,axis=1).reset_index(), id_vars=['date'], value_vars=['predicted_sales_q_0.1', 'predicted_sales_q_0.5', 'predicted_sales_q_0.9','original'])
plot_data['date'] = pd.to_datetime(plot_data['date'].astype(str).to_numpy())
plot_data['if_original'] = plot_data['variable'].apply(
    lambda r:'original' if r=='original' else 'predicted' 
)
forecast_graph = sns.lineplot(data = plot_data,
        x='date',
        y='value',
        hue='if_original',
        style="if_original",
        markers=['o','o'],
)

plt.title(f"Final Forecast - Error: {error}")
forecast_fig = forecast_graph.get_figure()
forecast_fig.savefig(f'graphs/{export_period}_forecast.svg')
forecast_plot = open(f'graphs/{export_period}_forecast.svg', 'r')

# plots = [
# monthly_sales_plot, # SHOW
# seasonal_plot, # SHOW
# detrender_plot,
# deseasonalizer_plot,
# forecast_plot,# SHOW
# ]

plots = {
'monthly_plot': monthly_plot, # SHOW
'seasonal_plot': seasonal_plot, # SHOW
'detrender_plot': detrender_plot,
'deseasonalizer_plot': deseasonalizer_plot,
'forecast_plot': forecast_plot, # SHOW
}


# References
# 
#     Bontempi, Gianluca & Ben Taieb, Souhaib & Le Borgne, Yann-Aël. ( 2013). Machine Learning Strategies for Time Series Forecasting — https://www.researchgate.net/publication/236941795_Machine_Learning_Strategies_for_Time_Series_Forecasting.
#     Markus Löning, Anthony Bagnall, Sajaysurya Ganesh, Viktor Kazakov, Jason Lines, Franz Király (2019): “sktime: A Unified Interface for Machine Learning with Time Series”
#     LightGBM-Quantile loss — https://towardsdatascience.com/lightgbm-for-quantile-regression-4288d0bb23fd
