import pandas as pd

# Load the dataset
df = pd.read_csv('trimmed_data.csv', low_memory=False, header=None)

# Ensure the date columns are in datetime format
df[1] = pd.to_datetime(df[1], format='%Y-%m-%d %H:%M:%S', errors='coerce')  # creation date
df[2] = pd.to_datetime(df[2], format='%Y-%m-%d %H:%M:%S', errors='coerce')  # closed date

# Remove rows where the incident is not yet closed
df = df.dropna(subset=[2])

# Calculate the response time in hours
df['response_time_hours'] = (df[2] - df[1]).dt.total_seconds() / 3600

# Create a new column for year-month
df['month'] = df[1].dt.to_period('M')

# Group by zipcode and month to calculate the average response time
zipcode_monthly_avg = df.groupby([8, 'month'])['response_time_hours'].mean().reset_index()
# Rename the columns
zipcode_monthly_avg.columns = ['zipcode', 'month', 'avg_response_time_hours']

# Save the pre-processed data
zipcode_monthly_avg.to_csv('task4_2.csv', index=False)