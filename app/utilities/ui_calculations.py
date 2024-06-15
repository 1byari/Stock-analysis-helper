"""This module performs usefult calculations operations for the UI"""

def calculate_graph_rows(choosed_methods):
    """Calculates amount of the the graph rows"""
    rows = ('MACD' in choosed_methods) + ('Swing' in choosed_methods) + ('Candles' in choosed_methods)
    rows += 'RSI' in choosed_methods or 'Close' in choosed_methods or 'MA' in choosed_methods
    return rows if rows > 0 else 1
