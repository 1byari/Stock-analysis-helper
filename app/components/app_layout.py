"""Main layout of the app"""

from datetime import datetime, timedelta
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from config import tickers_dict, methods_dict

def create_app_layout():
    """
    Creates main layout of the app UI
    """
    used_themes = [dbc.themes.CERULEAN, dbc.themes.DARKLY]
    layout = dbc.Container([
        html.Div([
            ThemeSwitchAIO(
                aio_id="theme", themes=used_themes
            ),
            html.H4('Stock Analysis Helper', style={'margin-right': '42vw'}),
        ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'}),

        html.Div([
            html.Div([
                html.Label('Start Date', style={'margin-right': '10px'}),
                dcc.DatePickerSingle(
                    id='date-picker-start',
                    min_date_allowed=datetime.now().date() - timedelta(days=3652),
                    max_date_allowed=datetime.now().date() - timedelta(days=7),
                    display_format='D.M.Y',
                    date=datetime.now().date() - timedelta(days=365),
                ),
                html.Label('End Date', style={'margin-right': '10px', 'margin-left': '20px'}),
                dcc.DatePickerSingle(
                    id='date-picker-end',
                    min_date_allowed=datetime.now().date() - timedelta(days=3652),
                    max_date_allowed=datetime.now().date() - timedelta(days=7),
                    display_format='D.M.Y',
                    date=datetime.now().date(),
                ),
            ], style={'display': 'flex', 'align-items': 'center'}),
            html.Button("Load News", id="load-news-btn", n_clicks=0,
                        style={'background-color': '#007BFF', 'width': '7vw', 'color': 'white',
                               'border': '1px solid #007BFF', 'borderRadius': '5px'}),
        ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center', 'padding': '15px'}),

        html.Div([
            dcc.Graph(
                id="stock_graph",
                figure={
                    'data': [],
                    'layout': {
                        'title': 'Choose ticker to update data on graph',
                        'xaxis': {'title': 'Date'},
                        'yaxis': {'title': 'Price $'}
                    }
                },
                style={'border': '2px solid #007BFF', 'borderRadius': '5px', 'height': '80vh', 'width': '75%'}
            ),
            html.Div(
                id="news_container",
                children=[
                    dcc.Dropdown(
                        id='choose_ticker_filter',
                        options=[{'label': k, 'value': k} for k in tickers_dict.keys()],
                        value='Apple',
                        style={'width': '100%'}
                    ),
                    html.Div(
                        id="news_list",
                        style={'height': 'calc(100% - 40px)', 'overflowY': 'auto', 'padding': '10px'}
                    )
                ],
            ),
        ], style={'display': 'flex'}),

        html.Div([
            html.Div([
                dcc.Dropdown(
                    options=[{'label': k, 'value': k} for k in tickers_dict.keys()],
                    value=[list(tickers_dict)[0]],
                    id='choose_ticker_dropdown',
                    style={'width': '100%'},
                    multi=True,
                    clearable=False,
                ),
            ], style={'width': '50%', 'margin-right': '20px'}),

            html.Div([
                dcc.Dropdown(
                    options=[{'label': k, 'value': k} for k in methods_dict.keys()],
                    value=[list(methods_dict)[0]],
                    id='choose_method_dropdown',
                    style={'width': '100%'},
                    multi=True,
                ),
                html.Div([
                    html.Div([
                        html.Label(["MA", html.Br(), "Window:"], style={'text-align': 'center', 'line-height': '1.2', 'margin-bottom': '5px'}),
                        dcc.Input(
                            id='ma_window_input',
                            type='number',
                            value=14,
                            min=2,
                            max=365,
                            style={'width': '60px'},
                        )
                    ], id='ma_window_container'),

                    html.Div([
                        html.Label(["MACD", html.Br(), "Parameters:"], style={'text-align': 'center', 'line-height': '1.2', 'margin-bottom': '5px'}),
                        html.Div([
                            html.Label("Slow"),
                            dcc.Input(
                                id='macd_slow_input',
                                type='number',
                                value=26,
                                min=20,
                                max=40,
                                style={'width': '60px', 'margin-left': '5px'},
                            )
                        ], style={'margin-bottom': '10px'}),
                        html.Div([
                            html.Label("Fast"),
                            dcc.Input(
                                id='macd_fast_input',
                                type='number',
                                value=12,
                                min=5,
                                max=19,
                                style={'width': '60px', 'margin-left': '5px'},
                            )
                        ], style={'margin-bottom': '10px'}),
                        html.Div([
                            html.Label("Signal"),
                            dcc.Input(
                                id='macd_signal_input',
                                type='number',
                                value=9,
                                min=6,
                                max=12,
                                style={'width': '60px', 'margin-left': '5px'},
                            )
                        ])
                    ], id='macd_parameters_container'),

                    html.Div([
                        html.Label(["RSI", html.Br(), "Window:"], style={'text-align': 'center', 'line-height': '1.2', 'margin-bottom': '5px'}),
                        dcc.Input(
                            id='rsi_window_input',
                            type='number',
                            value=14,
                            min=2,
                            max=365,
                            style={'width': '60px'},
                        )
                    ], id="rsi_window_container"),

                    html.Div([
                        html.Label(["Swing", html.Br(), "Shift:"], style={'text-align': 'center', 'line-height': '1.2', 'margin-bottom': '5px'}),
                        dcc.Input(
                            id='swing_shift_input',
                            type='number',
                            value=7,
                            min=1,
                            max=100,
                            style={'width': '60px'},
                        )
                    ], id="swing_shift_container")
                ], style={'display': 'flex', 'flex-direction': 'row', 'gap': '10px', 'margin-top': '10px'})
            ], style={'width': '50%'}),
        ], style={'display': 'flex', 'alignItems': 'top', 'width': '100%', 'margin-top': '15px'}),
    ], style={'margin': '0px', 'padding': '10px', 'max-width': '100%'}, className='dbc')

    return layout
