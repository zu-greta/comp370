# How many noise complaints per cause is there in each month of the year?
"""
columns from trimmed_data: created date (month), complaint type (noise) - descriptor (cause)
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('noise_complaints.csv')
df['created_date'] = pd.to_datetime(df['created_date'])
df['created_date'] = df['created_date'].dt.strftime('%m/%d/%Y')
df['month'] = pd.to_datetime(df['created_date']).dt.month # extract month from created_date
complaint_counts = df.groupby(['month', 'complaint_type']).size().unstack(fill_value=0) # count complaints per month and cause

# plot
complaint_counts.plot(kind='bar', stacked=True)
plt.title('Noise complaints per cause by month in 2020')
plt.xlabel('Month')
plt.ylabel('Number of complaints')
plt.legend(title='Cause', loc='upper right')
plt.xticks(np.arange(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.tight_layout()
plt.show()
