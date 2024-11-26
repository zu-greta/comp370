import unittest
import json
from datetime import datetime, timedelta
from newscover.newsapi import fetch_latest_news

class TestNewsAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("newscover/tests/test_secrets.json", "r") as file:
            cls.api_key = json.load(file)["api_key"]
            
    def test_keywords(self):        
        # Test case 1: No keywords provided
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key, [])

        # Test case 2: Non-alphabetic characters in keywords
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key, ["mcg!ll$", "143"])

    def test_lookback_days(self):
        articles = fetch_latest_news(self.api_key, ["mcgill"], lookback_days=2)
        for article in articles:
            published_at = article["publishedAt"][:10]
            self.assertGreaterEqual(published_at, (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"))
