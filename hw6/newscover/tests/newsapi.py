import unittest
import json
import os
from newscover.newsapi import fetch_latest_news
from datetime import datetime, timezone

"""python3 -m unittest discover -s newscover/tests -p 'test*.py'"""

class TestFetchLatestNews(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        secrets_path = os.path.join(os.path.dirname(__file__), 'secrets.json')
        with open(secrets_path) as f:
            secrets = json.load(f)
        cls.api_key = secrets['api_key']

    def test_no_keywords(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key, news_keywords='') #should raise ValueError
    
    def test_articles_within_timeframe(self):
        articles = fetch_latest_news(self.api_key, news_keywords='technology', lookback_days=5)
        today = datetime.now(datetime.timezone.utc)
        for article in articles:
            published_at = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            delta_days = (today - published_at).days
            self.assertLessEqual(delta_days, 5, "Found article outside the lookback period") 

    def test_invalid_keyword(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key, news_keywords='inv@alid') #should raise ValueError