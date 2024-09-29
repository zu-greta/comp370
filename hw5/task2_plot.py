# How many complaints about sanitary issues from rodents are found for each location type?
"""
columns from trimmed_data: location type, complaint type (sanitary)
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('sanitary_complaints.csv')
# clean up location type
location_mapping = {
    "3+ Family Apartment Building": "3+ Family Apartment Building",
    "3+ Family Apt. Building": "3+ Family Apartment Building",
    "Other": "Other",
    "Other (Explain Below)": "Other",
    "Street": "Street",
    "Street Area": "Street",
}
df['location_type'] = df['location_type'].replace(location_mapping)
# count complaints per location type
complaint_counts = df.groupby(['location_type']).size()

# plot
ax = complaint_counts.plot(kind='bar')
plt.title('Sanitary complaints about rodents by location type in 2020')
plt.xlabel('Location type')
plt.ylabel('Number of complaints')
plt.xticks(rotation=90)

for p in ax.patches:
    ax.annotate(f'{p.get_height()}', 
                (p.get_x() + p.get_width() / 2, p.get_height()), 
                ha='center', va='bottom')
    
plt.tight_layout()
plt.show()