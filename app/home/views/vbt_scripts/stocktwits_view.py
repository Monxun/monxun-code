import pandas as pd

from .stocktwits_model import get_bullbear, get_messages, get_trending, get_stalker


from tabulate import tabulate

def display_bullbear(ticker: str):
    """
    Print bullbear sentiment based on last 30 messages on the board.
    Also prints the watchlist_count. [Source: Stocktwits]
    Parameters
    ----------
    ticker: str
        Stock ticker
    """
    watchlist_count, n_cases, n_bull, n_bear = get_bullbear(ticker)
    print(f"Watchlist count: {watchlist_count}")
    if n_cases > 0:
        return (f"Last {n_cases} sentiment messages:"),  (f"Bullish {round(100*n_bull/n_cases, 2)}%"), (f"Bearish {round(100*n_bear/n_cases, 2)}%")
    else:
        print("No messages found")
    print("")


def display_messages(ticker: str, limit: int = 30):
    """Print up to 30 of the last messages on the board. [Source: Stocktwits]
    Parameters
    ----------
    ticker: str
        Stock ticker
    limit: int
        Number of messages to get
    """
    messages = get_messages(ticker, limit)

    if gtff.USE_TABULATE_DF:
        print(
            tabulate(
                pd.DataFrame(messages), headers=[], tablefmt="grid", showindex=False
            )
        )
    else:
        for message in messages:
            print(message, "\n")


def display_trending():
    """Show trensing stocks on stocktwits"""
    df_trending = get_trending()
    if gtff.USE_TABULATE_DF:
        print(
            tabulate(
                df_trending,
                headers=df_trending.columns,
                tablefmt="fancy_grid",
                showindex=False,
            )
        )
    else:
        print(df_trending.to_string(index=False))
    print("")


def display_stalker(user: str, limit: int = 10):
    """Show last posts for given user
    Parameters
    ----------
    user : str
        Stocktwits username
    limit : int, optional
        Number of messages to show, by default 10
    """
    messages = get_stalker(user, limit)
    for message in messages:
        print(
            "------------------------------------------------------------------------------"
        )
        print(message["created_at"].replace("T", " ").replace("Z", ""))
        print(message["body"])
        print("")