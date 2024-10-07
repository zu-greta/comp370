import requests
from datetime import datetime, timedelta

def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    """
    queries the NewsAPI and returns a python list of english news articles (represented as dictionaries) 
    containing those news keywords and published within the last <lookback_days>
    """

    if not news_keywords or not news_keywords.isalnum():
        raise ValueError('Invalid news keywords: News keywords must be non-empty and only contian alphanumberical characters')

    url = 'https://newsapi.org/v2/everything' 
    headers = {'Authorization': f'Bearer {api_key}'}

    today = datetime.now(datetime.timezone.utc)
    from_date = (today - timedelta(days=lookback_days)).strftime('%Y-%m-%d')

    params = {
        'q': news_keywords,
        'language': 'en',
        'from': from_date,
        'sortBy': 'publishedAt',
        'pageSize': 100
    }

    try :
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if 'articles' in data:
            return data['articles']
        else:
            print('No news articles found')
            return []
    
    except requests.RequestException as e:
        return Exception(f'Error fetching news from NewsAPI: {e}')
    
"""
if __name__ == '__main__':
    api_key = '6dc564134ed74e4d8ea4350007d122eb'
    news_keywords = 'coronavirus'
    lookback_days = 10

    articles = fetch_latest_news(api_key, news_keywords, lookback_days)
    for article in articles:
        print(article['title'], ' - ', article['publishedAt'])
"""