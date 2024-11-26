"""
Write a script naive_frequent_word_list.py that computes the top 10 words that appear in the 200 
post titles based on absolute frequency. It should count the number of times each word appears in 
the titles and then rank order them. The script should run as follows:
	python3 naive_frequent_word_list.py -o naive_no_stops.json football.json soccer.json montreal.json sports.json tennis.json volleyball.json

Note that your script should accept an arbitrary number of word lists. Bear in mind that you need 
to clean the titles since they'll contain punctuation and such… which aren't actually a part of a word.
The output file should be a dictionary with the following form:

	{
		“<input_file_1>”: [
			[“<word1>”, <# of times the word1 is used>],
			[“<word2>”: <# of times the word2>,
			…
		],
		“input_file_2”: [
			…
		]
		...
	}
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
    args = parser.parse_args()

    word_counts = {}
    for file in args.files:
        with open(file, "r", encoding="utf-8") as f:
            posts = json.load(f)
            words = []
            for post in posts:
                title = clean_title(post['title'])
                words.extend(title.split())

            word_counts[file] = Counter(words).most_common(10)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(word_counts, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()