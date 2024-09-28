import pandas as pd

#cd Documents/mcgill/u3/COMP370/hws/hw4

print("HW4")
#CSV file
#data = pd.read_csv('nyc_311_limit.csv', header=None, low_memory=False)

# CSV file (load in chunks)
chunksize = 10**6  # Process 1 million rows at a time

# Initialize an empty DataFrame to store processed chunks
data_chunks = []

for chunk in pd.read_csv('nyc_311_limit.csv', header=None, low_memory=False, chunksize=chunksize):
    data_chunks.append(chunk)
    print(f"Processed chunk with {len(chunk)} rows")

# Concatenate all chunks into a single DataFrame
data = pd.concat(data_chunks, ignore_index=True)

print("Data loaded")

'''
created date on column 2 MM/DD/YYYY
closed date on column 3 MM/DD/YYYY
incident zip on column 9

no column names
'''

#Remove rows with missing zip codes. At the beginning when you trim the data, you should only choose the rows with zipcode.
data = data.dropna(subset=[8])  
#Remove if there is no end date for a zipcode event.
data = data.dropna(subset=[2]) #drop rows with missing closed date
#For some rows the closed date is before the open date resulting in a negative response time. These rows should be removed. You can use some filter.
data[1] = pd.to_datetime(data[1], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')  
data[2] = pd.to_datetime(data[2], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
data = data.dropna(subset=[1, 2])
data = data[data[1] <= data[2]]  
#Include cases based on "open in 2020".
data = data[data[1].dt.year == 2020]
print("Data trimmed") 
#save in csv file
data.to_csv('trimmed_data.csv', sep=',', index=False, header=False)
print("Data saved")
