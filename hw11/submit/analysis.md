# What is the impact of including a stop word list?
Including a stop word list generally removes common words (like "the," "and," "is") that don't provide much information about the content. As a result, the word lists become more representative of the specific themes discussed in the texts.
Without removing stop words, the list may be dominated by these common terms, reducing the insightfulness of the results.

# What differences do you observe with TF-IDF?
TF-IDF assigns higher weights to words that are more significant across the entire dataset, thus highlighting unique terms that may not appear frequently but are important in distinguishing the content.
The naive method, on the other hand, focuses on sheer frequency, which can highlight repetitive but less informative words.

# Which method produces the best list?
Best for Relevance: TF-IDF tends to produce more meaningful lists when analyzing text for content insights, as it prioritizes words that differentiate documents from one another.
Best for Simplicity: The naive method is straightforward and may work well for a quick overview, but it often lacks depth compared to TF-IDF.