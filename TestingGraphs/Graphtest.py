import plotly.graph_objects as go
import networkx as nx

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 4), (4, 5), (5, 1)])

pos = nx.spring_layout(G)

fig = go.Figure()

for edge in G.edges():
    fig.add_trace(go.Scatter(x=[pos[edge[0]][0], pos[edge[1]][0]],
                             y=[pos[edge[0]][1], pos[edge[1]][1]],
                             mode='lines', hoverinfo=None, line=dict(color='lightgreen')))

node_x = []
node_y = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers', marker=dict(size=10, color='orange'), hoverinfo=None))

fig.update_layout(xaxis_range=[-1.2, 1.2], yaxis_range=[-1.2, 1.2], title='Simple Network Graph')
fig.show()
