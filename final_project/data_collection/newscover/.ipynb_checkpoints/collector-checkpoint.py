import argparse
import json
import os
from newscover.newsapi import fetch_latest_news

def load_api_key(file_path="newscover/tests/test_secrets.json"):
    with open(file_path, "r") as file:
        secrets = json.load(file)
    return secrets.get("api_key")

def main():
    parser = argparse.ArgumentParser(description="News Data Collector.")
    parser.add_argument("-k", "--api_key", help="NewsAPI key")
    parser.add_argument("-b", "--lookback_days", type=int, default=10, help="Number of days to look back")
    parser.add_argument("-i", "--input_file", required=True, help="JSON input file")
    parser.add_argument("-o", "--output_dir", required=True, help="Output directory")
    
    args = parser.parse_args()
    
    # Load the API key from file if not provided
    if not args.api_key:
        args.api_key = load_api_key()
    
    # Load the keyword sets from the input file
    with open(args.input_file, "r") as infile:
        keyword_sets = json.load(infile)
    
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    # Process each keyword set and fetch news articles
    for name, keywords in keyword_sets.items():
        print(f"Fetching news for keyword set: {name} ({keywords})")
        try:
            # Modify the keywords query to enforce ALL keywords using "AND"
            articles = fetch_latest_news(args.api_key, keywords, lookback_days=args.lookback_days, use_all_keywords=True)
            
            output_file = os.path.join(args.output_dir, f"{name}.json")
            with open(output_file, "w") as outfile:
                json.dump(articles, outfile, indent=4)
                
            print(f"Results saved to {output_file}")
        except Exception as e:
            print(f"Error fetching news for {name}: {e}")

if __name__ == "__main__":
    main()