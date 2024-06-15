"""This module is responsible for the news fetching from API"""

from datetime import datetime, timedelta
import requests
from requests.exceptions import RequestException
from config import NEWS_API_KEY
from utilities.news_alalysis import process_news_data

def register_cache(cache):
    """Cache register"""
    @cache.memoize(timeout=3600)
    def fetch_news(ticker):
        """Fetches news articles for a specific stock ticker and caches the results.

        Args:
            ticker (str): The stock ticker symbol for which to fetch news.

        Returns:
            list: A list of HTML components representing the news articles.
        """
        cached_news = cache.get(ticker)
        if cached_news:
            return cached_news

        news_data = get_news_from_api(ticker)
        processed_news = process_news_data(news_data, ticker)
        cache.set(ticker, processed_news)
        return processed_news
    return fetch_news


def get_news_from_api(ticker):
    """Makes an API request to fetch news for a given ticker.

    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        dict: JSON data from the API response.
    """
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': ticker,
        'apiKey': NEWS_API_KEY,
        'sortBy': 'publishedAt',
        'from': (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
        'language': 'en'
    }
    response = requests.get(url, params=params, timeout=10)
    if response.status_code != 200:
        raise RequestException(f"Failed to fetch news: {response.text}")
    return response.json()
