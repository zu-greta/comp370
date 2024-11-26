import requests
import re
from datetime import datetime, timedelta

NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_latest_news(api_key, news_keywords, lookback_days=10, use_all_keywords=False):
    """Fetch the latest news articles based on provided keywords and lookback days"""
    # Check if keywords are provided
    if not news_keywords:
        raise ValueError("Keywords must be provided.")
        
    # Check if keywords contain only alphabetic characters
    for keyword in news_keywords:
        if not re.match("^[a-zA-Z]+$", keyword):
            raise ValueError("Keywords must contain only alphabetic characters.")

    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=lookback_days)).strftime("%Y-%m-%d")
    
    # Formulate the query string
    if use_all_keywords:
        query = " AND ".join(news_keywords)  # All keywords must appear in the article
    else:
        query = " OR ".join(news_keywords)   # Any keyword can appear in the article
    
    params = {
        "apiKey": api_key,
        "q": query,
        "from": start_date,
        "to": end_date,
        "language": "en",
    }
    
    response = requests.get(NEWS_API_URL, params=params)
    
    # Raise an exception if the API call fails
    if response.status_code != 200:
        raise Exception(f"Error fetching news: {response.status_code}")
    
    # Return the articles as a list of dictionaries
    return response.json().get("articles", [])
