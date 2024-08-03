import osmnx as ox
import geopandas as gpd
import networkx as nx
import pyrosm
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# Read the extracted PBF file
osm = pyrosm.OSM('athens_extract.osm.pbf')

# Get the network data
network_type = 'driving'  # Change this to 'walking', 'cycling', etc., if needed
nodes, edges = osm.get_network(network_type=network_type, nodes=True)

# Create a NetworkX graph from edges
G = osm.to_graph(nodes, edges, graph_type="networkx")

# Simplify the graph
G_simplified = ox.simplify_graph(G)

# Extract nodes and edges from the simplified graph
nodes_simplified, edges_simplified = ox.graph_to_gdfs(G_simplified, nodes=True, edges=True)

# Plot the simplified graph
fig, ax = ox.plot_graph(G_simplified, node_size=10, edge_linewidth=1)

# Print nodes and edges
print("Nodes:\n", nodes_simplified)
print("\nEdges:\n", edges_simplified)

nodes_simplified.to_csv('nodes.csv')
edges_simplified.to_csv('edges.csv')