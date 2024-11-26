"""
Write the script compute_network_stats.py which is run as follows:
	python compute_network_stats.py -i /path/to/<interaction_network.json> -o /path/to/<stats.json>
Using the networkx library, compute 
The top three most connected characters by degree centrality.
The top three most connected characters by weighted degree centrality (each edge contributes its weight = # of interactions)
The top three most connected characters by closeness centrality.
The top three most central characters by betweenness centrality.  
Your output file should have structure:
	{
“degree”: [c1, c2, c3],
“weighted_degree”: [c1, c2, c3],	“closeness”: [c1, c2, c3],
“betweenness”: [c1, c2, c3]}
As usual, the -i and -o arguments refer to any path (and not just a file name). Indentation won't matter in this exercise; 
you can have a one-line JSON file or a pretty-printed one.
Reflect on what differences are there and what they might mean.

"""

import argparse
import json
import networkx as nx

def compute_network_stats(input_path, output_path):
    """Compute network statistics using NetworkX."""
    # Load the interaction network
    with open(input_path, 'r') as file:
        interaction_network = json.load(file)

    # Build the graph
    G = nx.Graph()
    for character, interactions in interaction_network.items():
        for neighbor, weight in interactions.items():
            G.add_edge(character, neighbor, weight=weight)

    # Compute centrality measures
    degree_centrality = nx.degree_centrality(G)
    weighted_degree_centrality = {node: sum(data['weight'] for _, data in G[node].items()) for node in G.nodes()}
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G, weight='weight')

    # Find the top 3 characters for each metric
    top_degree = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:3]
    top_weighted_degree = sorted(weighted_degree_centrality, key=weighted_degree_centrality.get, reverse=True)[:3]
    top_closeness = sorted(closeness_centrality, key=closeness_centrality.get, reverse=True)[:3]
    top_betweenness = sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:3]

    # Prepare the output data
    stats = {
        "degree": top_degree,
        "weighted_degree": top_weighted_degree,
        "closeness": top_closeness,
        "betweenness": top_betweenness
    }

    # Write the results to the output file
    with open(output_path, 'w') as outfile:
        json.dump(stats, outfile, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Compute network statistics from interaction network.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input JSON file.")
    parser.add_argument("-o", "--output", required=True, help="Path to the output JSON file.")
    args = parser.parse_args()

    compute_network_stats(args.input, args.output)

if __name__ == "__main__":
    main()


# python3 compute_network_stats.py -i interaction_network.json -o stats.json
