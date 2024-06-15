"""Layout of the graph and its traces"""

from plotly.subplots import make_subplots
import plotly.graph_objects as go
from indicators.indicators_calculations import (
    calculate_ma,
    calculate_macd,
    calculate_rsi,
    calculate_swing
)

def setup_figure_layout(rows: int):
    """
    Setup the basic layout for the plotly figure with specified number of rows.

    Args:
        rows: Number of rows in the subplot.

    Returns:
        plotly.graph_objs.Figure: Configured subplot figure.
    """
    specs = [[{}]] * rows
    specs[0] = [{"secondary_y": True}]

    figure = make_subplots(
        rows=rows,
        cols=1,
        shared_xaxes=False,
        vertical_spacing=0.2,
        specs=specs
    )

    return figure

def create_ma_graph(figure, data, ticker, amount_of_tickers, window=30, row=1):
    """
    Adds a Moving Average trace to a given figure.

    Args:
        figure: Plotly figure to which the MA trace will be added.
        data: Dataframe containing stock data.
        ticker: Ticker symbol of the stock.
        amount_of_tickers: Number of tickers, used to adjust data references.
        window: Window size for the moving average.
        row: Row number in subplot to place this graph.

    Returns:
        The figure with the MA trace added.
    """
    column = ("Close", ticker) if amount_of_tickers > 1 else "Close"
    figure.add_trace(
        go.Scatter(
            x=data[column].index,
            y=calculate_ma(data[column], window),
            mode='lines',
            name=f'MA {ticker}'
        ),
        row=row,
        col=1
    )
    figure.update_yaxes(title_text="Close Price $", row=row, col=1)
    figure.update_xaxes(title_text="Date", row=row, col=1)
    return figure

def create_swing_graph(figure, data, ticker, amount_of_tickers, shift=1, row=3):
    """
    Adds a Swing graph trace to a given figure.

    Args:
        figure: Plotly figure to which the swing trace will be added.
        data: Dataframe containing stock data.
        ticker: Ticker symbol of the stock.
        amount_of_tickers: Number of tickers, used to adjust data references.
        row: Row number in subplot to place this graph.
        shift: Shift parameter for swing calculation.

    Returns:
        The figure with the Swing trace added.
    """
    column = ("Close", ticker) if amount_of_tickers > 1 else "Close"
    figure.add_trace(
        go.Scatter(
            x=data[column].index,
            y=calculate_swing(data[column], shift),
            mode='lines',
            name=f'Swing {ticker}'
        ),
        row=row,
        col=1
    )
    figure.update_yaxes(title_text="Swing Value", row=row, col=1)
    figure.update_xaxes(title_text="Date", row=row, col=1)
    return figure

def create_close_graph(figure, ticker, data, amount_of_tickers, row=1):
    """
    Adds a Close price graph trace to a given figure.

    Args:
        figure: Plotly figure to which the close trace will be added.
        data: Dataframe containing stock data.
        ticker: Ticker symbol of the stock.
        amount_of_tickers: Number of tickers, used to adjust data references.
        row: Row number in subplot to place this graph.

    Returns:
        The figure with the Close trace added.
    """
    column = ("Close", ticker) if amount_of_tickers > 1 else "Close"
    figure.add_trace(
        go.Scatter(
            x=data[column].index,
            y=data[column],
            mode='lines',
            name=f'Close {ticker}'
        ),
        row=row,
        col=1
    )
    figure.update_yaxes(title_text="Close Price $", row=row, col=1)
    figure.update_xaxes(title_text="Date", row=row, col=1)
    return figure

def create_candles_graph(figure, ticker, data, amount_of_tickers, row=2):
    """
    Adds a Candlestick graph trace to a given figure.

    Args:
        figure: Plotly figure to which the candlestick trace will be added.
        data: Dataframe containing stock data.
        ticker: Ticker symbol of the stock.
        amount_of_tickers: Number of tickers, used to adjust data references.
        row: Row number in subplot to place this graph.

    Returns:
        The figure with the Candlestick trace added.
    """
    open_column = ("Open", ticker) if amount_of_tickers > 1 else "Open"
    close_column = ("Close", ticker) if amount_of_tickers > 1 else "Close"
    low_column = ("Low", ticker) if amount_of_tickers > 1 else "Low"
    high_column = ("High", ticker) if amount_of_tickers > 1 else "High"
    figure.add_trace(
        go.Candlestick(
            x=data[close_column].index,
            open=data[open_column],
            high=data[high_column],
            low=data[low_column],
            close=data[close_column],
            name=f'Candles {ticker}'
        ),
        row=row,
        col=1
    )
    figure.update_yaxes(title_text="Price $", row=row, col=1)
    figure.update_xaxes(title_text="Date", row=row, col=1)
    return figure

def create_rsi_graph(figure, ticker, data, amount_of_tickers, window=14, secondary_y=True, row=1):
    """
    Adds an RSI graph trace to a given figure.

    Args:
        figure: Plotly figure to which the RSI trace will be added.
        data: Dataframe containing stock data.
        ticker: Ticker symbol of the stock.
        amount_of_tickers: Number of tickers, used to adjust data references.
        window: Window size for the RSI calculation.
        secondary_y: Whether the trace should use a secondary Y-axis.
        row: Row number in subplot to place this graph.

    Returns:
        The figure with the RSI trace added.
    """
    rsi = calculate_rsi(data['Close'] if amount_of_tickers == 1 else data['Close'][ticker], window=window)
    figure.add_trace(
        go.Scatter(
            x=data.index,
            y=rsi,
            mode='lines',
            name=f'RSI {ticker}'
        ),
        secondary_y=secondary_y,
        row=row,
        col=1
    )
    figure.update_yaxes(title_text="RSI value", row=row, col=1)
    figure.update_xaxes(title_text="Date", row=row, col=1)
    return figure

def create_macd_graph(figure, ticker, data, amount_of_tickers, slow=26, fast=12, signal=9, row=2):
    """
    Adds MACD line, signal line, and histogram to the provided figure.

    Args:
        figure (plotly.graph_objs.Figure): The figure to which the MACD graph will be added.
        ticker (str): The ticker symbol for the stock.
        data (pandas.DataFrame): Dataframe containing stock data.
        amount_of_tickers (int): Indicates if more than one ticker is being analyzed.
        slow (int): The number of periods for the slow moving average.
        fast (int): The number of periods for the fast moving average.
        signal (int): The number of periods for the signal line.
        row (int): The row of the subplot in which to place the MACD graph.

    Returns:
        plotly.graph_objs.Figure: The figure updated with MACD graph traces.
    """
    macd, signal_line, histogram = calculate_macd(
        data['Close'] if amount_of_tickers == 1 else data['Close'][ticker],
        slow, fast, signal
    )

    # MACD trace
    figure.add_trace(
        go.Scatter(x=data.index, y=macd, mode='lines', name=f'MACD {ticker}'),
        row=row, col=1
    )

    # Signal trace
    figure.add_trace(
        go.Scatter(x=data.index, y=signal_line, mode='lines', name=f'Signal {ticker}'),
        row=row, col=1
    )

    # Histogram trace
    figure.add_trace(
        go.Bar(x=data.index, y=histogram, name=f'Histogram {ticker}'),
        row=row, col=1
    )

    figure.update_yaxes(title_text="MACD value", row=row, col=1)
    figure.update_xaxes(title_text="Date", row=row, col=1)
    return figure
