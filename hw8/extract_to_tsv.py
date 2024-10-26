"""
Write a script extract_to_tsv.py that accepts one of the files you collected from Reddit and 
outputs a random selection of posts from that file to a tsv (tab separated value) file.  
It should function like this:

	python3 extract_to_tsv.py -o <out_file> <json_file> <num_posts_to_output>

If <num_posts_to_output> is greater than the file length, then the script should just output all lines.  
If there are more than <num_posts_to_output> (which is likely the case), then it should randomly select 
num_posts_to_output (the parameter you passed to the script) of them and just output those.

The output format (written to out_file) is:

	Name <tab> title <tab> coding
	<name of first post chosen> <tab> <title of first post chosen> <tab>	
    <name of second post chosen> <tab> <title of the second post chosen> <tab>	…	
    <name of the n'th post chosen> <tab> <title of the nth post chosen> <tab>

Here is an example:

Name	title	coding
t3_jmmrja	"Easy Computer Science classes"	
t3_jmm91k	"Cloudberry (+ Tri-pawed squirrel) Appreciation Post"	
t3_jmg17h	"Breaking a lease over a persistent cockroach infestation?"	
t3_jmfc0t	"Don't know how to cook"	
t3_jmfj91	"my bike is falling apart"	

Note that:
we're including the “name” field because it uniquely identifies the post, in case you ever need to go back 
and check something in the original data
whitespace between column value and the tab is optional
the third column “coding” is intentionally blank.  We'll be completing that in the next task.
We also need a specific output for this exercise (which will be completed on task 3). Run the following:

python3 extract_to_tsv.py -o annotated_mcgill.tsv mcgill.json 50
python3 extract_to_tsv.py -o annotated_concordia.tsv concordia.json 50

That means, run your script on your McGill and Concordia files you created, 50 lines in each. 
The output files, annotated_mcgill.tsv and annotated_concordia.tsv, should be submitted in the 
submission_template. Please check the README.md for further information.
"""
import argparse
import json
import random

def extract_to_tsv(out_file, json_file, num_posts_to_output):
    with open(json_file, 'r') as f:
        data = json.load(f)
        posts = data['data']['children']
        if num_posts_to_output > len(posts):
            num_posts_to_output = len(posts)
        random_posts = random.sample(posts, num_posts_to_output)
        with open(out_file, 'w') as fout:
            fout.write('Name\ttitle\tcoding\n')
            for post in random_posts:
                post_data = post['data']
                fout.write(f"{post_data['name']}\t{post_data['title']}\t\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out_file', required=True)
    parser.add_argument('json_file')
    parser.add_argument('num_posts_to_output', type=int)
    args = parser.parse_args()
    extract_to_tsv(args.out_file, args.json_file, args.num_posts_to_output)

if __name__ == '__main__':
    main()
