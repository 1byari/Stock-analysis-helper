"""Layout of the news cards"""

from datetime import datetime
from dash import html


def create_news_html(article, sentiment, ticker):
    """Creates HTML components for a single news article.

    Args:
        article (dict): An article containing title, description, etc.
        sentiment (dict): Sentiment analysis result for the article's description.
        ticker (str): Stock ticker symbol related to the article.

    Returns:
        html.Div: A Dash HTML component representing the news article.
    """
    return {
        "html": html.Div([
            html.A(article['title'] + '...', href=article['url'], target="_blank"),
            html.P(f"Sentiment: {sentiment['label']} ({sentiment['score']:.2f})",
                   style={'color': '#4ee44e' if sentiment['label'] == 'POSITIVE' else '#ff0000'}),
            html.P(datetime.strptime(article["publishedAt"], '%Y-%m-%dT%H:%M:%SZ').strftime('%d.%m.%y') + f" ({ticker})")
        ], style={'border': '1px solid #ddd', 'padding': '5px', 'margin': '5px'}),
        "ticker": ticker
    }

def create_sentiments_total_html(positives_amount, negatives_amount):
    """
    Create a HTML Div containing sentiment totals formatted with color.

    Args:
        positives_amount (int): The number of positive sentiments.
        negatives_amount (int): The number of negative sentiments.

    Returns:
        dash.html.Div: A Div containing formatted positive and negative sentiment counts.
    """

    positive_text = html.Span("POSITIVES", style={'color': '#4ee44e'})
    negative_text = html.Span("NEGATIVES", style={'color': '#ff0000'})

    return html.Div([
        html.P(["Amount of ", positive_text, f": {positives_amount}"]),
        html.P(["Amount of ", negative_text, f": {negatives_amount}"]),
    ], style={'vertical-align': 'baseline'})
