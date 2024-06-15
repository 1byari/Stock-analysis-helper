"""This module processes the news data fetched from the API"""

from transformers import pipeline
from components.news_layout import create_news_html, create_sentiments_total_html


def process_news_data(data, ticker):
    """Processes the news data fetched from the API.

    Args:
        data (dict): The news data from the API.
        ticker (str): The ticker symbol associated with the news.

    Returns:
        list: A list of HTML components representing the news articles.
    """
    nlp = pipeline("sentiment-analysis")
    articles = data.get('articles', [])
    sentiments = nlp([article['description'] for article in articles if article['description']])
    news = []
    if sentiments:
        positives, negatives = caclulate_sentiments(sentiments)
        news.append({"html" : create_sentiments_total_html(positives, negatives)})
    for article, sentiment in zip(articles, sentiments):
        news.append(create_news_html(article, sentiment, ticker))
    return news

def caclulate_sentiments(sentiments):
    """
    Calculates the amount of POSITIVE and NEGATIVE sentiments
    """
    positives = 0
    negatives = 0
    for sentiment in sentiments:
        if sentiment['label'] == 'POSITIVE':
            positives += 1
        else:
            negatives += 1
    return positives, negatives


    