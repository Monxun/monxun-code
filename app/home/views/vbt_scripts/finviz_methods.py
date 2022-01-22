 import finviz
finviz.get_stock('AAPL')
# {'Index': 'DJIA S&P500', 'P/E': '12.91', 'EPS (ttm)': '12.15',...
finviz.get_insider('АAPL')
# [{'Insider Trading': 'KONDO CHRIS', 'Relationship': 'Principal Accounting Officer', 'Date': 'Nov 19', 'Transaction':            'Sale', 'Cost': '190.00', '#Shares': '3,408', 'Value ($)': '647,520', '#Shares Total': '8,940', 'SEC Form 4': 'Nov 21           06:31 PM'},...
finviz.get_news('AAPL')
# [('Chinas Economy Slows to the Weakest Pace Since 2009', 'https://finance.yahoo.com/news/china-economy-slows-weakest-pace-      020040147.html'),...
finviz.get_analyst_price_targets('AAPL')
# [{'date': '2019-10-24', 'category': 'Reiterated', 'analyst': 'UBS', 'rating': 'Buy', 'price_from': 235, 'price_to': 275}, ...

# Monthly, Candles, Large, No Technical Analysis
stock_list.get_charts(period='m', chart_type='c', size='l', ta='0')

# period='d' > daily
# period='w' > weekly
# period='m' > monthly

# chart_type='c' > candle
# chart_type='l' > lines

# size='m' > small
# size='l' > large

# ta='1' > display technical analysis
# ta='0' > ignore technical analysis


########################################################
# NEWS

def get_news(ticker):
    """
    Returns a list of sets containing news headline and url
    :param ticker: stock symbol
    :return: list
    """

    get_page(ticker)
    page_parsed = STOCK_PAGE[ticker]
    rows = page_parsed.cssselect('table[id="news-table"]')[0].xpath('./tr[not(@id)]')

    results = []
    date = None
    for row in rows:
        raw_timestamp = row.xpath("./td")[0].xpath('text()')[0][0:-2]

        if len(raw_timestamp) > 8:
            parsed_timestamp = datetime.strptime(raw_timestamp, "%b-%d-%y %I:%M%p")
            date = parsed_timestamp.date()
        else:
            parsed_timestamp = datetime.strptime(raw_timestamp, "%I:%M%p").replace(
                year=date.year, month=date.month, day=date.day)

        results.append((
            parsed_timestamp.strftime("%Y-%m-%d %H:%M"),
            row.xpath("./td")[1].cssselect('a[class="tab-link-news"]')[0].xpath("text()")[0],
            row.xpath("./td")[1].cssselect('a[class="tab-link-news"]')[0].get("href"),
            row.xpath("./td")[1].cssselect('div[class="news-link-right"] span')[0].xpath("text()")[0][1:]
        ))

    return results



# import csv
# import io
# import re
# import sqlite3


# def create_connection(sqlite_file):
#     """ Creates a database connection. """

#     try:
#         conn = sqlite3.connect(sqlite_file)
#         return conn
#     except sqlite3.Error as error:
#         raise (
#             "An error has occurred while connecting to the database: ",
#             error.args[0],
#         )


# def __write_csv_to_stream(stream, headers, data):
#     """Writes the data in CSV format to a stream."""

#     dict_writer = csv.DictWriter(stream, headers)
#     dict_writer.writeheader()
#     dict_writer.writerows(data)


# def export_to_csv(headers, data, filename=None, mode="w", newline=""):
#     """Exports the generated table into a CSV file if a file is mentioned.
#     Returns the CSV table as a string if no file is mentioned."""

#     if filename:
#         with open(filename, mode, newline=newline) as output_file:
#             __write_csv_to_stream(output_file, headers, data)
#         return None
#     stream = io.StringIO()
#     __write_csv_to_stream(stream, headers, data)
#     return stream.getvalue()


# def export_to_db(headers, data, filename):
#     """ Exports the generated table into a SQLite database into a file."""

#     field_list = ""
#     table_name = "screener_results"  # name of the table to be created
#     conn = create_connection(filename)
#     c = conn.cursor()

#     for field in headers:

#         field_cleaned = re.sub(r"[^\w\s]", "", field)
#         field_cleaned = field_cleaned.replace(" ", "")
#         field_list += field_cleaned + " TEXT, "

#     c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({field_list[:-2]})")

#     inserts = ""
#     for row in data:

#         insert_fields = "("
#         for field, value in row.items():

#             insert_fields += '"' + value + '", '

#         inserts += insert_fields[:-2] + "), "

#     insert_lines = inserts[:-2]

#     try:
#         c.execute(f"INSERT INTO {table_name} VALUES {insert_lines}")
#     except sqlite3.Error as error:
#         print("An error has occurred", error.args[0])

#     conn.commit()
#     conn.close()