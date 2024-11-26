from argparse import ArgumentParser
import pandas as pd
import json


def main(output_file, json_file):
   with open(json_file) as input_file:
       data = json.load(input_file)
  
   lis = []
   for article in data:
       lis.append([article["title"], article["description"], ""])
  
   df = pd.DataFrame(lis, columns =['title', 'description', 'coding'])
   df.to_csv(output_file, sep="\t", index=False)


if __name__ == "__main__":
   # python3 articles_to_tsv.py -o <out_file> <json_file>
   parser = ArgumentParser()
   parser.add_argument("-o", help="Output file", required=True)
   parser.add_argument("json_file", help="JSON file")
   args = parser.parse_args()
   main(args.o, args.json_file)