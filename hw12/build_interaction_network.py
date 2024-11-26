"""
In this assignment, we are modeling the interaction network as who speaks to who.  
There is an (undirected) edge between two characters that speak to one another.  
The weight of the edge is how many times they speak to one another.

To keep our life simple, we're going to use a very simple proxy for “speaking to one another”.  
We will say that character X speaks to character Y whenever character Y has a line IMMEDIATELY after 
character X in an episode. So, for the following excerpt of dialog from an episode…

	Twilight Sparkle: Hey Pinkie. Sorry I accused you of being nosy.
	Pinkie Pie: It's okay, Twilight - we all have our rough days.
	Applejack: Come on, everypony!  We need to get a move-on.
	Spike: Hurray!

In this excerpt, we have the following interactions:
	
	Twilight Sparkles speaks to Pinkie Pie
	Pinkie Pie speaks to Apple Jack
	Applejack speaks to Spike

Of course, from the text, we can see that Pinkie Pie's comment wasn't *really* addressed to Apple Jack… 
highlighting how proxies can be wrong (and how hard it is to get interaction networks even remotely right). 
But for this assignment, we're going to assume it's a good proxy.

Keep the following in mind:
A character can't talk to itself
We're considering the top 101 most frequent characters, not just the ponies. Frequency is defined by # of speaking lines.
Don't include characters that contain the following words in their names: “others”, “ponies”, "and", "all". For example, 
"Fluttershy and other ponies" should not be considered.  
When skipping these records, the speaker that comes before won't have ANY follow on speaker (i.e., a plural character like 
"Fluttershy and other ponies" nulls out the interaction it's involved in)
Respect episode boundaries - interactions shouldn't carry over.
We are counting UNDIRECTED interactions - this means that if Spike speaks to Applejack and later Applejack speaks to Spike … 
then the number of interactions between them is 2.
Match characters by exact name. For example, do not bother to build an equivalence between "Twilight" and "Twilight Sparkle" 
if you encounter both types of references in the dialog. Same applies to "Young Applejack" and "Applejack"; we know they are 
the same, but your code should treat them differently. If you have the bandwidth, you're welcome to work on a method 
that merges them.


Your script, build_interaction_network.py, should work as follows

	python build_interaction_network.py -i /path/to/<script_input.csv> -o /path/to/<interaction_network.json>

where the interaction network json file should have structure…

	{
		“twilight sparkle”: {
        “spike”: <# of interactions between twilight sparkle and spike>,“applejack”: <# of interactions between ts and aj>,“pinkie pie”: <# of interactions between ts and pp>,
			…
		},
		“pinkie pie”: {
			“twilight sparkle”: <# of interactions between ts and pp>			...
		}
		...
	}

For consistency, lowercase all character names in the output JSON. 

As usual, the arguments -i and -o should take any path. Indentation won't matter in this exercise; you can have a one-line JSON file or a pretty-printed one.

"""

import argparse
import csv
import json
from collections import defaultdict

EXCLUDED_TERMS = ["others", "ponies", "and", "all"]

def is_valid_character(name):
    """Check if a character's name is valid based on exclusion rules."""
    name_lower = name.lower()
    return not any(term in name_lower for term in EXCLUDED_TERMS)

def build_interaction_network(input_path, output_path):
    """Build the interaction network from the input CSV."""
    # Initialize the network as a defaultdict of defaultdicts
    interaction_network = defaultdict(lambda: defaultdict(int))

    # Read the input CSV file
    with open(input_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        previous_speaker = None
        previous_episode = None

        for row in reader:
            episode = row["title"].strip()
            speaker = row["pony"].strip().lower()

            # Check for invalid characters
            if not is_valid_character(speaker):
                previous_speaker = None  # Nullify interaction when invalid
                continue

            # Check for episode boundary
            if episode != previous_episode:
                previous_speaker = None  # Reset speaker at new episode
                previous_episode = episode

            # Add interaction if valid
            if previous_speaker and previous_speaker != speaker:
                interaction_network[previous_speaker][speaker] += 1
                interaction_network[speaker][previous_speaker] += 1

            # Update previous speaker
            previous_speaker = speaker

    # Save the interaction network as JSON
    with open(output_path, 'w') as json_file:
        json.dump(interaction_network, json_file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Build character interaction network from dialog data.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input CSV file.")
    parser.add_argument("-o", "--output", required=True, help="Path to the output JSON file.")
    args = parser.parse_args()

    build_interaction_network(args.input, args.output)

if __name__ == "__main__":
    main()

# python3 build_interaction_network.py -i clean_dialog.csv -o interaction_network.json
