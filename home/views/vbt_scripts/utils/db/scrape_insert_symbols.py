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

# JUST A LIST OF AVAILABLE INTERVALS FOR insert_to_db()
INTERVALS = ['1min', '5min', '15min', '30min', '60min']

################################################################################
# TEST CONNECTION TO POSTGRES
def postgres_test():

    try:
        conn = psycopg2.connect(f"dbname=stockdata user={DB_USER} host={DB_HOST} password={DB_PASS} connect_timeout=1")
        conn.close()
        return True
    except:
        return False


################################################################################
# CONNECT TO POSTGRES AND CREATE TABLE FOR MARKET DATA
def make_table(symbol):

    conn = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} host={DB_HOST} password={DB_PASS}")
    table_name = f'{symbol}'
    cur = conn.Cursor()
    # SCRIPT TO CHECK THEN CREATE TABLE IF NONE EXISTS AND HYPERTABLE FOR TIMESCALE_DB
    cur.execute(f"CREATE TABLE IF NOT EXISTS public.{table_name} (id INTEGER, time TIMESTAMP, open NUMERIC, high NUMERIC, low NUMERIC, close NUMERIC, volume INTEGER, symbol CHAR);")
    # cur.execute(f"SELECT create_hypertable('{table_name}', 'time');")
    conn.commit()


################################################################################
def create_prices_table(symbol):

    # INITIALIZE VARIABLES
    interval = '1min'
    slice = 'year1month1'
    api_key = APLHA_API_KEY
    db_password = DB_PASS  # Set to your own password
    db_name = 'stockdata'  # Set to your own db name
    engine = create_engine(f'postgres://postgres:{DB_PASS}@localhost:5432/{DB_NAME}?sslmode=require')

    # Import the bar csv file into a dataframe
    df = pd.read_csv(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={symbol}&interval={interval}&slice={slice}&apikey={api_key}')

    # Some formatting
    df['symbol'] = symbol
    df = df[['symbol', 'time', 'open', 'high', 'low', 'close', 'volume']]
    df['time'] = pd.to_datetime(df['time'])
    df = df.fillna(0)
    df['updated'] = pd.to_datetime('now')
    print(df.head())
    # Write the data into the database, this is so fucking cool
    df.to_sql(f'{symbol}_{interval}', engine, if_exists='replace', index=False)

    # Create a primary key on the table
    query = f'ALTER TABLE {symbol}_{interval} ADD PRIMARY KEY (symbol, time);'
    engine.execute(query)

    query = f"SELECT create_hypertable('{symbol}_{interval}', 'time');"
    engine.execute(query)

    return f'{symbol} {interval} prices table created'


################################################################################
# TOP 50 US MARKET CAP COMPANIES
def get_symbols():
    """
    args: symbol, intervals
    symbol: 'TSLA': a string containing the ticker symbol of the instrument you
    want retrieved from apha and inserted to postgres

    """
    url = 'https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/'
    html = requests.get(url).text # NO CLOSING PARENTHESES

    # INITIALIZES BS4 ENGINE
    soup = BeautifulSoup(html, 'html.parser')

    # soup.select('html-element') returns a beautifulsoup object that needs to be
    # iterated through using list comprehension.
    # (Grabs .text for each item parsed in BS4 object)
    symbols = [e.text for e in soup.select('div.company-code')]

    return symbols


################################################################################
# APLHA ADVANTAGE TIME SERIES INTRADAY EXTENDED HISTORY
def insert_to_db(symbol):


    interval = '1min'
    slice = 'year1month1'
    api_key = APLHA_API_KEY

    CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={symbol}&interval={interval}&slice={slice}&apikey={api_key}'

    df = pd.read_csv(CSV_URL)

    ############################################################################
    # INSERT INDICATORS, DUMMY VARIABLES, ETC HERE:
    df['symbol'] = symbol
    #MAKE DATETIME OBJECT WITH 'time'
    df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
    # IF RENAME IS NEEDED: df.rename(dict of name pairs: {'old':'new'})

    # df = df.rename(columns={'time': 'stock_datetime', 'open': 'price_open',
    # 'high': 'price_high', 'low': 'price_low', 'close': 'price_close',
    # 'volume': 'trading_volume',})

    # print(CSV_URL)
    print(df.head())

    ############################################################################
    # ITERATE OVER ZIPPED OBJECT TO LIST COMPREHEND TUPLES TO FEED INTO PGCOPY
    records = [row for row in df.itertuples(index=False, name=None)]

    # NAME COLUMNS IN TABLE THAT CORRESPOND TO DF COLUMNS (RENAME @ 1:00:00 IN VIDEO)
    cols = ('id', 'time', 'open', 'high', 'low', 'close', 'volume', 'symbol')
    now = datetime.now()

    conn = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} host={DB_HOST} password={DB_PASS} connect_timeout=1")
    # print(conn)
    cur = conn.cursor()

    # INITIALIZES COPY MANAGER
    mgr = CopyManager(conn, f'{symbol}_{interval}', cols)
    mgr.copy(records)

    # DON'T FORGET TO COMMIT!
    conn.commit()


################################################################################
#CREATE INDICATOR DATA / CREATE COLUMN / UPDATE TABLE
def create_indicators():
    pass


################################################################################
# RUN SCRIPT
def main(symbol='GME'):
    create_prices_table(symbol)
    # insert_to_db(symbol)

print(postgres_test())
main()
