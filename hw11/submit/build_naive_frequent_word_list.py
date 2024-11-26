"""
Add stop word removal to your script such that it can be run as follows:

python3 build_naive_frequent_word_list.py -o naive_with_stops.json -s stopwords.txt football.json soccer.json montreal.json sports.json tennis.json volleyball.json

The stop word file is optional. If it's specified, then all the words in the stop word file list are removed from the candidate list of top words.
"""

import argparse
import json
import re
from collections import Counter

def clean_title(title):
    return re.sub(r'[^\w\s]', '', title).lower()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output file to save the word counts")
    parser.add_argument("files", nargs="+", help="Input files to process")
    parser.add_argument("-s", "--stopwords", help="File containing stopwords")
    args = parser.parse_args()

    word_counts = {}
    for file in args.files:
        with open(file, "r", encoding="utf-8") as f:
            posts = json.load(f)
            words = []
            for post in posts:
                title = clean_title(post['title'])
                # Split the title into words, if a stopword file is provided, remove the stopwords
                if args.stopwords:
                    with open(args.stopwords, "r", encoding="utf-8") as stopword_file:
                        stopwords = set(stopword_file.read().splitlines())
                        words.extend([word for word in title.split() if word not in stopwords])
                else:
                    words.extend(title.split())

            word_counts[file] = Counter(words).most_common(10)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(word_counts, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()