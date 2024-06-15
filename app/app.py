"""App initialization and registration of the app callbacks"""

from dash import Dash
from flask_caching import Cache
from config import styles_url
from components.app_layout import create_app_layout
from callbacks.graph_callbacks import register_graph_callbacks
from callbacks.methods_callbacks import register_methods_callbacks
from callbacks.news_callbacks import register_news_callbacks
from callbacks.ticker_filter_callbacks import register_tickers_filters_callbacks
from requests_data.fetch_news import register_cache

app = Dash(__name__, external_stylesheets=[styles_url], meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
cache = Cache(app.server, config={'CACHE_TYPE': 'simple'})
app.layout = create_app_layout()

fetch_news = register_cache(cache)
register_graph_callbacks(app)
register_methods_callbacks(app)
register_news_callbacks(app, fetch_news)
register_tickers_filters_callbacks(app)
