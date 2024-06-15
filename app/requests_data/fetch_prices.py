"""This module is responsible for data fetching from Yahoo Finance"""

import yfinance as yf
import pandas as pd

def fetch_prices_data(tickers: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetches historical price data for specified tickers from Yahoo Finance.

    Returns:
        pd.DataFrame: A DataFrame containing the historical price data.
    """
    ticker_info = yf.download(tickers, start=start_date, end=end_date, interval="1d")
    data = pd.DataFrame(ticker_info)
    return data
