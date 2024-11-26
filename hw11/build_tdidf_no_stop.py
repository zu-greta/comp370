"""
Implement a separate script that computes the top 10 words for each input file based on their TF-IDF score (where each subreddit is considered the “document”). It should run as follows:
	python3 build_tdidf_no_stop.py -o tfidf_no_stops.json football.json soccer.json montreal.json sports.json tennis.json volleyball.json
The contract is the same except that your output file contains the tf-idf scores rather than the # of times they’re used.
"""

import argparse
import json
import re
from collections import Counter
from math import log

def clean_title(title):
    return re.sub(r'[^\w\s]', '', title).lower()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output file to save the word scores")
    parser.add_argument("files", nargs="+", help="Input files to process")
    args = parser.parse_args()

    word_counts = {}
    all_words = []
    for file in args.files:
        with open(file, "r", encoding="utf-8") as f:
            posts = json.load(f)
            words = []
            for post in posts:
                title = clean_title(post['title'])
                words.extend(title.split())
            all_words.extend(words)
            word_counts[file] = Counter(words)

    # Calculate the IDF for each word
    idf = {}
    for word in set(all_words):
        idf[word] = log(len(args.files) / sum(1 for file in args.files if word in word_counts[file]))

    # Calculate the TF-IDF score for each word
    word_scores = {}
    for file in args.files:
        word_scores[file] = {}
        for word in word_counts[file]:
            word_scores[file][word] = word_counts[file][word] * idf[word]

    # only keep the top 10 words
    for file in args.files:
        word_scores[file] = dict(Counter(word_scores[file]).most_common(10))
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(word_scores, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
