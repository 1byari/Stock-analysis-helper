"""Callbacks for the tickers filter in news container"""

from dash.dependencies import Input, Output

def register_tickers_filters_callbacks(app):
    """
    Registers a callback for updating the options and default value of the ticker filter
    based on the ticker selection from a dropdown.
    """
    @app.callback(
        [
            Output('choose_ticker_filter', 'options'),
            Output('choose_ticker_filter', 'value')
        ],
        [Input('choose_ticker_dropdown', 'value')]
    )
    def update_choose_ticker_filter(tickers_chosen):
        """
        Updates the selectable options in the ticker filter based on the user's chosen tickers
        from the dropdown menu and sets the default selected value to the first ticker.

        Args:
            tickers_chosen (list): List of ticker symbols selected by the user.

        Returns:
            tuple: A tuple containing the list of tickers as options and the first ticker as the default value.
        """
        if tickers_chosen:
            return [{'label': ticker, 'value': ticker} for ticker in tickers_chosen], tickers_chosen[0]
        return [], None
