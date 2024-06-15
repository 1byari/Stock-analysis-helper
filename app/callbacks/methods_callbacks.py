"""Callbacks for the displaying methods options containers"""

from dash.dependencies import Input, Output

def register_methods_callbacks(app):
    """
    Register callbacks to toggle visibility of method containers based on selected methods.
    """
    @app.callback(
        [
            Output('ma_window_container', 'style'),
            Output('macd_parameters_container', 'style'),
            Output('rsi_window_container', 'style'),
            Output('swing_shift_container', 'style')
        ],
        [Input('choose_method_dropdown', 'value')]
    )
    def toggle_method_containers(choosed_methods):
        """
        Adjust the display style of method containers based on the analysis methods chosen by the user.

        Args:
            choosed_methods (list of str): A list of analysis methods selected by the user.

        Returns:
            tuple: A tuple containing the CSS style dictionaries for MA, MACD, RSI, and Swing containers.
        """
        basic_style = {
            'display': 'none',
            'flexDirection': 'column',
            'justify-content': 'center',
            'align-items': 'center',
            'vertical-align': 'baseline',
            'padding-top': '3px',
            'padding-bottom': '3px',
            'width': '20%',
            'border': '2px solid #007BFF',
            'borderRadius': '5px',
            'height': '12vh'
        }
        ma_style = basic_style.copy()
        macd_style = basic_style.copy()
        rsi_style = basic_style.copy()
        swing_style = basic_style.copy()

        if 'MA' in choosed_methods:
            ma_style['display'] = 'flex'
        if 'MACD' in choosed_methods:
            macd_style['display'] = 'flex'
            macd_style['height'] = '20vh'
        if 'RSI' in choosed_methods:
            rsi_style['display'] = 'flex'
        if 'Swing' in choosed_methods:
            swing_style['display'] = 'flex'

        return ma_style, macd_style, rsi_style, swing_style
