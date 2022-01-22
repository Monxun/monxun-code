import pandas as pd
import requests
import psycopg2
import os
import matplotlib

from datetime import datetime
from pgcopy import CopyManager
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from config import APLHA_API_KEY, DB_NAME, DB_HOST, DB_USER, DB_PASS, DB_PORT

# INITIALIZE VARIABLES
db_password = DB_PASS  # Set to your own password
db_name = DB_NAME  # Set to your own db name
cols = "'symbol', 'open', 'high', 'low', 'close', 'volume', 'updated'"
# INITIALIZE CURSOR
conn = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} host={DB_HOST} password={DB_PASS}")
# INITIALIZE CURSOR
cur = conn.cursor()
engine = create_engine(f'postgresql://postgres:{db_password}@localhost/{db_name}')


def postgres_test():

    try:
        conn = psycopg2.connect(f"dbname=stockdata user={DB_USER} host={DB_HOST} password={DB_PASS} connect_timeout=1")
        conn.close()
        return True
    except:
        return False



def grab_stock_data(symbol='GME', interval='1min', slice='year1month1', api_key = APLHA_API_KEY):

    # interval = '1min'
    # slice='year1month1'
    # api_key = APLHA_API_KEY

    # Import the bar csv file into a dataframe
    df = pd.read_csv(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={symbol}&interval={interval}&slice={slice}&apikey={api_key}')

    # Some formatting
    df['symbol'] = symbol
    df = df[['time', 'symbol', 'open', 'high', 'low', 'close', 'volume']]
    df['time'] = pd.to_datetime(df['time'])
    df = df.fillna(0)
    df['updated'] = pd.to_datetime('now')
    print(df.head())

    return df


def create_stock_table(df, table_name='gme_1min'):

    df.to_sql(table_name, engine, if_exists='replace', index=False)


def create_stock_pk(table_name):
    query = f"""ALTER TABLE {table_name}
                ADD PRIMARY KEY (symbol, time);"""
    engine.execute(query)


def create_stock_hypertable(symbol='gme', interval='1min'):
    # query = f'SELECT create_hypertable("{symbol}_{interval}", "time");'
    # engine.execute(query)

    conn = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} host={DB_HOST} password={DB_PASS}")
    table_name = f'{symbol}_{interval}'
    cur = conn.cursor()
    # CHECK ANF CREATE TIMESCALEDB EXT ON DATABASE
    cur.execute("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;")
    conn.commit()

    # SELECT create_hypertable('gme_1min', 'time');
    cur.execute(f"SELECT create_hypertable('{table_name}', 'time', migrate_data => true);")
    conn.commit()
    # SCRIPT TO CHECK THEN CREATE TABLE IF NONE EXISTS AND HYPERTABLE FOR TIMESCALE_DB
    # cur.execute(f"SELECT create_hypertable('{table_name}', 'time');")
    # # cur.execute(f"SELECT create_hypertable('{table_name}', 'time');")
    # conn.commit()
    print("Hypertable CREATED")

def read_stock_prices_from_db(symbol='gme', interval='1min'):
    df = pd.read_sql(f'{symbol}_{interval}', engine, index_col=['symbol', 'time'])
    return df


def main(symbol, interval='1min', slice='year1month1'):

    symbol = symbol.lower()
    table_name = f"{symbol}_{interval}"

    print(postgres_test())
    df = grab_stock_data(symbol)
    create_stock_table(df, table_name)
    create_stock_pk(table_name)
    create_stock_hypertable(symbol, interval)
    df = read_stock_prices_from_db(symbol)
    print(df.head())

# PASS 'tsla' AS ARG WITH DEFAULT KEYWORD ARGS 'interval' AND 'slice'
main('tsla')
