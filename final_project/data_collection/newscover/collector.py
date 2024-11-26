import argparse
import json
import os
import requests
import re
from datetime import datetime

NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_latest_news(api_key, news_keywords, start_date, end_date, domains, sources, max_articles=100):
    """Fetch the latest news articles based on provided keywords, date range, and sources"""
    # Check if keywords are provided
    if not news_keywords:
        raise ValueError("Keywords must be provided.")
        
    # Check if keywords contain only alphabetic characters
    for keyword in news_keywords:
        if not re.match("^[a-zA-Z]+$", keyword):
            raise ValueError("Keywords must contain only alphabetic characters.")

    # Formulate the query string
    query = " OR ".join(news_keywords)  # Any keyword can appear in the article

    # Format the parameters for the API request
    params = {
        "apiKey": api_key,
        "q": query,
        "searchIn": "title",
        "from": start_date,
        "to": end_date,
        "language": "en",
        "domains": ",".join(domains),
        "sources": ",".join(sources),
        "pageSize": max_articles  # Fetch up to 100 articles
    }
    
    response = requests.get(NEWS_API_URL, params=params)
    
    # Raise an exception if the API call fails
    if response.status_code != 200:
        raise Exception(f"Error fetching news: {response.status_code} - {response.json().get('message', '')}")
    
    # Return the articles as a list of dictionaries
    return response.json().get("articles", [])

def load_api_key(file_path="newscover/tests/test_secrets.json"):
    with open(file_path, "r") as file:
        secrets = json.load(file)
    return secrets.get("api_key")

def main():
    parser = argparse.ArgumentParser(description="News Data Collector.")
    parser.add_argument("-k", "--api_key", help="NewsAPI key")
    parser.add_argument("-o", "--output_dir", required=True, help="Output directory")
    
    args = parser.parse_args()
    
    # Load the API key from file if not provided
    if not args.api_key:
        args.api_key = load_api_key()
    
    
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    domains_names = [
        "people.com", "yahoo.com", "nypost.com", "forbes.com",
        "cnbc.com", "cnn.com", "foxnews.com", "usatoday.com",
        "washingtonpost.com", "newsweek.com", "apnews.com", "cbsnews.com",
        "nbcnews.com", "businessinsider.com", "wsj.com", "huffpost.com",
        "substack.com", "reuters.com", "buzzfeed.com",
        "thehill.com", "politico.com", "breitbart.com", "variety.com", "sfgate.com",
        "dailydot.com", "zerohedge.com", "latimes.com", "rawstory.com", "nj.com",
        "thedailybeast.com", "msnbc.com", "today.com", "theatlantic.com", "the-sun.com"
    ]

    source_names = ["abc-news"]
    
    
    # Process the specific keyword set for "Kamala" or "Harris"
    print("Fetching news for keyword set: Kamala or Harris")
    try:
        # Define the date range for November 6 and 7
        # start_date = "2024-11-06"
        # end_date = "2024-11-07"

        # Define the date range for November 8 and 9
        # start_date = "2024-11-08"
        # end_date = "2024-11-09"

        start_date = "2024-11-08"
        end_date = "2024-11-12"
        
        # Fetch the news articles
        articles = fetch_latest_news(
            args.api_key,
            ["Kamala", "Harris"],
            start_date,
            end_date,
            domains_names,
            source_names,
            max_articles=100
        )
        
        output_file = os.path.join(args.output_dir, "kamala_harris_news_5.json")
        with open(output_file, "w") as outfile:
            json.dump(articles, outfile, indent=4)
        
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error fetching news: {e}")

if __name__ == "__main__":
    main()


#python3 -m newscover.collector -o newscover -i newscover/keywords.json -k 6dc564134ed74e4d8ea4350007d122eb