import os
import json
import argparse
from newscover.newsapi import fetch_latest_news

def load_keywords_from_file(input_file):
    try:
        with open(input_file, 'r') as f:
            keywords_dict = json.load(f)
        return keywords_dict
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {input_file}')
    except json.JSONDecodeError:
        raise Exception(f'Invalid JSON format in: {input_file}')

def save_results_to_file(results, output_file):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4) #indent for pretty printing

def collect_news(api_key, input_file, output_dir, lookback_days=10):
    keywords_dict = load_keywords_from_file(input_file)
    os.makedirs(output_dir, exist_ok=True) #create output directory if it doesn't exist

    for name, keywords in keywords_dict.items():
        keywords_str = ' '.join(keywords)
        print(f'Fetching news for {name}...')

        try:
            articles = fetch_latest_news(api_key, keywords_str, lookback_days)
            output_file = os.path.join(output_dir, f'{name}.json')
            save_results_to_file(articles, output_file)
            print(f'Successfully saved {len(articles)} articles to {output_file}')
        except Exception as e:
            print(f'Error fetching news for {name}: {e}')

def main():
    parser = argparse.ArgumentParser(description='Collect latest news articles from NewsAPI')
    parser.add_argument('api_key', type=str, help='Your NewsAPI API key')
    parser.add_argument('input_file', type=str, help='Path to JSON file containing news keywords')
    parser.add_argument('output_dir', type=str, help='Directory to save news articles')
    parser.add_argument('--lookback_days', type=int, default=10, help='Number of days to look back for news articles')
    args = parser.parse_args()

    collect_news(args.api_key, args.input_file, args.output_dir, args.lookback_days)

if __name__ == '__main__':
    main()
    