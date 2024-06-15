"""This modulates calculates values for different methods"""

import numpy as np
import pandas as pd

def calculate_rsi(data: pd.Series, window: int = 14) -> pd.Series:
    """
    Calculate the Relative Strength Index (RSI) for the given data.

    Parameters:
    - data (pd.Series): The input price data as a Pandas Series.
    - window (int): The lookback period for calculation.

    Returns:
    - pd.Series: The RSI values.
    """
    delta = data.diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = pd.Series(gain).rolling(window=window, min_periods=1).mean()
    avg_loss = pd.Series(loss).rolling(window=window, min_periods=1).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(data: pd.Series, slow: int = 26, fast: int = 12, signal: int = 9) -> tuple:
    """
    Calculate the Moving Average Convergence Divergence (MACD) for the given data.

    Parameters:
    - data (pd.Series): The input price data as a Pandas Series.
    - slow (int): The slow EMA period.
    - fast (int): The fast EMA period.
    - signal (int): The signal line EMA period.

    Returns:
    - tuple: Tuple containing the MACD line, signal line, and histogram.
    """
    exp1 = data.ewm(span=fast, adjust=False).mean()
    exp2 = data.ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    histogram = macd - signal_line
    return macd, signal_line, histogram

def calculate_ma(data: pd.Series, window: int = 30) -> pd.Series:
    """
    Calculate the moving average of the given data.

    Parameters:
    - data (pd.Series): The input price data as a Pandas Series.
    - window (int): The moving average window size.

    Returns:
    - pd.Series: The moving average of the data.
    """
    return data.rolling(window=window).mean()

def calculate_swing(data: pd.Series, shift: int = 1) -> pd.Series:
    """
    Calculate the swing or percentage change between the current and a shifted data.

    Parameters:
    - data (pd.Series): The input price data as a Pandas Series.
    - shift (int): The number of periods to shift for the calculation.

    Returns:
    - pd.Series: The percentage change of the data.
    """
    return (data / data.shift(shift) - 1) * 100
