import pytest
import numpy as np
import pandas as pd
from app.indicators.indicators_calculations import (
    calculate_ma,
    calculate_macd,
    calculate_rsi,
    calculate_swing
)

np.set_printoptions(threshold=np.inf)

@pytest.fixture
def sample_data():
    """
    Generates a sample dataset for testing.
    """
    np.random.seed(0)  
    data = pd.DataFrame({'Close': np.random.normal(loc=100, scale=10, size=100)})
    return data

def test_calculate_ma(sample_data):
    """
    Tests the moving average calculation function.
    """
    ma = calculate_ma(sample_data['Close'], window=5)
    expected_ma = sample_data['Close'].rolling(window=5).mean()
    pd.testing.assert_series_equal(ma, expected_ma, check_names=False)

def test_calculate_macd(sample_data):
    """
    Tests the MACD calculation function.
    """
    macd, signal, hist = calculate_macd(sample_data['Close'], slow=26, fast=12, signal=9)
    assert len(macd) == 100, "MACD line length should match input data length."
    assert len(signal) == 100, "Signal line length should match input data length."
    assert len(hist) == 100, "Histogram length should match input data length."

def test_calculate_rsi(sample_data):
    """
    Tests the RSI calculation function.
    """
    rsi = calculate_rsi(sample_data['Close'], window=14)
    assert rsi.min() >= 0 and rsi.max() <= 100, "RSI values should be between 0 and 100."

def test_calculate_swing(sample_data):
    """
    Tests the swing calculation function.
    """
    swing = calculate_swing(sample_data['Close'], shift=1)
    expected_swing = ((sample_data['Close'] / sample_data['Close'].shift(1)) - 1) * 100
    pd.testing.assert_series_equal(swing, expected_swing, check_names=False)
