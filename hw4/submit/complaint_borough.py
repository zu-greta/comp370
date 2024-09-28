"""
Task 1: CLI investigation tool
Build a python-based command line tool borough_complaints.py that uses argparse to provide a UNIX-style command 
which outputs the number of each complaint type per borough for a given (creation) date range.
The command should take arguments in this way:
	borough_complaints.py -i <the input csv file> -s <start date> -e <end date> [-o <output file>]
If the output argument isn't specified, then just print the results (to stdout).
Results should be printed in a csv format like:
	complaint type, borough, count	derelict vehicles, Queens, 236	derelict vehicles, Bronx, 421	…
Note that borough_complaints.py -h should print a relatively nice help message thanks to argparse.
Commit your script, but not the data to your git repo.
"""


import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Count the number of each complaint type per borough for a given date range')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input CSV file')
    parser.add_argument('-s', '--start', type=str, required=True, help='Start date (format: MM/DD/YYYY)')
    parser.add_argument('-e', '--end', type=str, required=True, help='End date (format: MM/DD/YYYY)')
    parser.add_argument('-o', '--output', type=str, help='Output CSV file')
    args = parser.parse_args()

    # Load data
    try:
        data = pd.read_csv(args.input, low_memory=False, header=None, on_bad_lines='skip', sep=',') 
    except FileNotFoundError:
        print(f"Error: File {args.input} not found.")
        return
    
    #drop rows with missing borough
    data = data.dropna(subset=[25])
    #drop rows with missing complaint type
    data = data.dropna(subset=[5])

    # Count complaints per borough
    complaints = data.groupby([25, 5]).size().reset_index(name='count') # 25: borough, 5: complaint type
    complaints.columns = ['borough', 'complaint_type', 'count']

    # Output results
    if args.output:
        complaints.to_csv(args.output, index=False)
    else:
        print(complaints.to_csv(index=False))

if __name__ == '__main__':
    main()
