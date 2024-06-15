"""Callbacks for updating data on graph"""

from dash.dependencies import Input, Output
from dash_bootstrap_templates import ThemeSwitchAIO
from components.graph_layout import (
    setup_figure_layout,
    create_ma_graph,
    create_close_graph,
    create_rsi_graph,
    create_macd_graph,
    create_swing_graph,
    create_candles_graph
)
from utilities.ui_calculations import calculate_graph_rows
from config import tickers_dict
from requests_data.fetch_prices import fetch_prices_data

def apply_selected_methods(figure, ticker, data, choosed_methods, ma_window, macd_slow, macd_fast, macd_signal, rsi_window, swing_shift, amount_of_tickers):
    """
    Apply selected analysis methods to the figure based on user input.

    Args:
        figure (go.Figure): The plotly figure to which traces will be added.
        ticker (str): The stock ticker symbol.
        data (DataFrame): The data containing stock information.
        choosed_methods (list): List of methods chosen by the user.
        ma_window (int): The moving average window size.
        macd_slow (int): The slow EMA period for MACD.
        macd_fast (int): The fast EMA period for MACD.
        macd_signal (int): The signal line period for MACD.
        rsi_window (int): The period for RSI calculation.
        swing_shift (int): The shift period for swing calculation.

    Returns:
        go.Figure: The updated figure with the selected analysis methods applied.
    """

    used_rows = 1
    if 'MA' in choosed_methods:
        figure = create_ma_graph(figure, data, ticker, amount_of_tickers, ma_window, used_rows)
    if 'Close' in choosed_methods:
        figure = create_close_graph(figure, ticker, data, amount_of_tickers, used_rows)
    if 'RSI' in choosed_methods:
        secondary_y = "MA" in choosed_methods or "Close" in choosed_methods
        figure = create_rsi_graph(figure, ticker, data, amount_of_tickers, rsi_window, secondary_y, used_rows)
    if 'RSI' in choosed_methods or 'MA' in choosed_methods or 'Close' in choosed_methods:
        used_rows += 1
    if 'MACD' in choosed_methods:
        figure = create_macd_graph(figure, ticker, data, amount_of_tickers, macd_slow, macd_fast, macd_signal, used_rows)
        used_rows += 1
    if 'Swing' in choosed_methods:
        figure = create_swing_graph(figure, data, ticker, amount_of_tickers, swing_shift, used_rows)
        used_rows += 1
    if 'Candles' in choosed_methods:
        figure = create_candles_graph(figure, ticker, data, amount_of_tickers, used_rows)
        used_rows += 1

    return figure

def register_graph_callbacks(app):
    @app.callback(
        Output("stock_graph", "figure"),
        [
            Input("choose_ticker_dropdown", "value"),
            Input("choose_method_dropdown", "value"),
            Input("date-picker-start", "date"),
            Input("date-picker-end", "date"),
            Input("ma_window_input", "value"),
            Input("macd_slow_input", "value"),
            Input("macd_fast_input", "value"),
            Input("macd_signal_input", "value"),
            Input("rsi_window_input", "value"),
            Input("swing_shift_input", "value"),
            Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
        ]
    )
    def update_graph(choosed_tickers, choosed_methods, start_date, end_date, ma_window, macd_slow, macd_fast, macd_signal, rsi_window, swing_shift, theme):
        """
        Update the stock graph based on user inputs and selected methods.

        Args:
            choosed_tickers (list): List of selected ticker symbols.
            choosed_methods (list): List of selected analysis methods.
            start_date (str): Start date for data acquisition.
            end_date (str): End date for data acquisition.
            ma_window (int): Window size for moving average calculation.
            macd_slow (int): Slow parameter for MACD calculation.
            macd_fast (int): Fast parameter for MACD calculation.
            macd_signal (int): Signal parameter for MACD calculation.
            rsi_window (int): Window size for RSI calculation.
            swing_shift (int): Shift size for Swing calculation.
            theme (bool): Theme indicator from the theme switcher.

        Returns:
            plotly.graph_objs.Figure: Updated figure object for Dash graph component.
        """

        rows = calculate_graph_rows(choosed_methods)
        figure = setup_figure_layout(rows)

        template = 'plotly_white' if theme else 'plotly_dark'
        figure.update_layout(template=template, showlegend=True)

        if len(choosed_methods) < 1 or len(choosed_tickers) < 1:
            return figure
        
        tickers = []
        for ticker in choosed_tickers:
            tickers.append(tickers_dict[ticker])

        data = fetch_prices_data(' '.join(tickers), start_date, end_date)

        for ticker in tickers:
            apply_selected_methods(figure, ticker, data, choosed_methods, ma_window, macd_slow, macd_fast, macd_signal, rsi_window, swing_shift, len(tickers))

        return figure