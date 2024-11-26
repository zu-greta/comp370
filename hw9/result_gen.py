"""
Using only your final labeled dataset, make a bar chart showing the relative abundance of each topic, 
contrasting Concordia and McGill. What differences do you observe?

final_labeled_dataset_concordia.tsv
final_labeled_dataset_mcgill.tsv
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
concordia = pd.read_csv('final_labeled_dataset_concordia.tsv', sep='\t')
mcgill = pd.read_csv('final_labeled_dataset_mcgill.tsv', sep='\t')

# Count the number of each topic in the 'coding' column
concordia_counts = concordia['coding'].value_counts()
mcgill_counts = mcgill['coding'].value_counts()

# Plot the data
fig, ax = plt.subplots()
concordia_counts.plot(kind='bar', color='blue', ax=ax, position=0, width=0.4)
mcgill_counts.plot(kind='bar', color='red', ax=ax, position=1, width=0.4)

# Add labels and title
plt.xlabel('Topic')
plt.ylabel('Number of Articles')
plt.title('Topic Abundance in Concordia and McGill Articles')

# Add a legend
plt.legend(['Concordia', 'McGill'])

# Show the plot
plt.show()

