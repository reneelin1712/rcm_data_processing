import osmnx as ox
import geopandas as gpd
import networkx as nx
import pyrosm
import pandas as pd
import math

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

# Save the nodes and edges to CSV files
nodes_simplified.to_csv('nodes.csv')
edges_simplified.to_csv('edges.csv')

# Load the simplified graph from nodes and edges
nodes_df = pd.read_csv('nodes.csv', index_col='osmid')
edges_df = pd.read_csv('edges.csv')

# Function to sort neighbors clockwise
def sort_neighbors_clockwise(graph, node):
    node_data = graph.nodes[node]
    neighbors = list(graph.neighbors(node))
    print('neighbors',neighbors)

    def calculate_bearing(n):
        neighbor_data = graph.nodes[n]
        delta_x = neighbor_data['x'] - node_data['x']
        delta_y = neighbor_data['y'] - node_data['y']

        # Calculate the angle in radians between the line connecting the node and the neighbor
        # and the line parallel to the x-axis (East direction)
        angle = math.atan2(delta_y, delta_x)

        # Convert the angle to degrees and adjust it to represent bearing
        bearing = math.degrees(angle)
        bearing = (bearing + 360) % 360  # Ensure the bearing is positive
        return bearing

    # Sort neighbors based on bearing
    sorted_neighbors = sorted(neighbors, key=calculate_bearing)
    return sorted_neighbors

# Update each node in the graph with the sorted neighbors
for node in G_simplified.nodes():
    G_simplified.nodes[node]['sorted_neighbors'] = sort_neighbors_clockwise(G_simplified, node)

# print('graph.nodes',G_simplified.nodes)
# print('graph neigh',G_simplified.nodes[95663376]['sorted_neighbors'])

# Add sorted neighbors to nodes DataFrame
nodes_df['neighbors'] = nodes_df.index.map(lambda node_id: G_simplified.nodes[node_id]['sorted_neighbors'] if node_id in G_simplified.nodes else [])

# Convert neighbors to list (since they are returned as an iterator)
nodes_df['neighbors'] = nodes_df['neighbors'].apply(list)

# Save the updated nodes DataFrame to a new CSV file
nodes_df.to_csv('nodes_with_neighbors.csv')
