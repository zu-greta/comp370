import pandas as pd
import re

#CSV file
data = pd.read_csv('IRAhandle_tweets_1.csv')
print(data.head())

#data collection
#keep the first 10000 tweets
data = data.head(10000)
#english filter
data = data[data['language'] == 'English']
#question mark filter out
data = data[~data['content'].str.contains('\?')]

#save in TSV file
data.to_csv('hw1_datacollection.tsv', sep='\t', index=False)

#data annotation
#trump_mention filter
data['trump_mention'] = data['content'].apply(lambda x: 'T' if re.search(r'\bTrump\b', x) else 'F')
data.to_csv('hw1_dataannotation.tsv', sep='\t', index=False)

#dataset.tsv
#load hw1_dataannotation.tsv
data = pd.read_csv('hw1_dataannotation.tsv', sep='\t')
data = data[['tweet_id', 'publish_date', 'content', 'trump_mention']]
data.to_csv('dataset.tsv', sep='\t', index=False, encoding='utf-8')

#data analysis
#load dataset.tsv
data = pd.read_csv('dataset.tsv', sep='\t')
#calculate the percentage of tweets that mention Trump
total_tweets = len(data)
trump_tweets = len(data[data['trump_mention'] == 'T'])
percentage = round(trump_tweets / total_tweets, 3)
#results.tsv
results = pd.DataFrame({
    'result': ['frac-trump-mentions'], 
    'value': [percentage]
})
results.to_csv('results.tsv', sep='\t', index=False, encoding='utf-8')