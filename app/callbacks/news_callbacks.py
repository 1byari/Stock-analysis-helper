"""Callbacks for generating news container"""

from dash.dependencies import Input, Output

def register_news_callbacks(app, fetch_news):
    """
    Registers the callback for updating the news list and layout styles based on user interaction.

    Args:
        app (dash.Dash): The Dash application instance to which the callback will be attached.
    """
    @app.callback(
        [
            Output("news_list", "children"),
            Output("news_container", "style"),
            Output("stock_graph", "style")
        ],
        [
            Input("load-news-btn", "n_clicks"),
            Input("choose_ticker_filter", "value")
        ]
    )
    def update_news(number_clicked, ticker_filter):
        """
        Updates the news display based on user interaction, specifically the press of a button.

        Args:
            number_clicked (int): The number of times the 'Load News' button has been clicked.
            ticker_filter (str): The ticker symbol selected by the user for filtering news.

        Returns:
            tuple: A tuple containing the updated news HTML, the new style for the news container, and the new style for the stock graph.
        """

        news_style = {
            'border': '2px solid #007BFF', 
            'borderRadius': '5px', 
            'padding': '10px', 
            'height': '80vh', 
            'width': '20%', 
            'vertical-align': 'baseline', 
            'display': 'none', 
            'margin-left': '10px'
        }
        graph_style = {
            'border': '2px solid #007BFF', 
            'borderRadius': '5px', 
            'padding': '5px', 
            'height': '80vh', 
            'width': '100%'
        }

        if number_clicked > 0:
            filtered_news = []
            filtered_news.extend(fetch_news(ticker_filter))
            if filtered_news:
                filtered_news = [item["html"] for item in filtered_news]
                news_style['display'] = 'block'
                graph_style['width'] = '80%'
                return filtered_news, news_style, graph_style
        
        return [], news_style, graph_style
