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
As usual, the -i and -o arguments refer to any path (and not just a file name). Indentation won't matter in this exercise; you can have a one-line JSON file or a pretty-printed one.
Reflect on what differences are there and what they might mean.

"""