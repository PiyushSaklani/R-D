# import matplotlib.pyplot as plt
# import networkx as nx

# # Create an empty graph
# G = nx.Graph()

# # Add nodes to the graph
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)

# # Add edges to the graph
# G.add_edge(1, 2)
# G.add_edge(2, 3)
# G.add_edge(3, 1)

# # Draw the graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True)

# # Show the graph
# plt.show()

#!--------------------

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(range(1, 11))

# Add random edges to the graph
for i in range(1, 11):
    for j in range(i+1, 11):
        if np.random.random() < 0.3:  # add edge with 30% probability
            G.add_edge(i, j)

# Compute the node degrees
degrees = dict(G.degree())

# Compute the color map based on the node degrees
vmin, vmax = min(degrees.values()), max(degrees.values())
cmap = plt.get_cmap('coolwarm')
node_colors = [cmap((degrees[n]-vmin)/(vmax-vmin)) for n in G.nodes()]

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='lightgrey', node_size=300)

# Show the graph
plt.show()
