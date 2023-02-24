import numpy as np 
import random as rm
from tqdm import tqdm
from datetime import datetime
import time
import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt

#! Functions
def plotgraph(all_nodes,connections):
    G = nx.Graph()
    G.add_nodes_from(all_nodes)
    G.add_edges_from(connections)

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

def filter_list(check_list,a,b):
    return len(list(filter(lambda x: a <= x <= b, check_list)))

def check_pct(check_list,range_list):
    acc = 0
    for a,b in range_list:
        val = round(filter_list(check_list,a,b) / len(check_list) * 100,2)
        print(f"\033[90mPercentage of numbers in the range {a}-{b} : {val}\033[00m")
        acc += val
    
    return acc

def random_valandpct(range_list,population_pct,all_lists,p):
    for i,j in zip(range_list,population_pct):
        temp_list = list(range(i[0],i[1]))
        all_lists = all_lists + temp_list
        p = p + [j/len(temp_list)]*len(temp_list)
    return all_lists,p

def current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def append_matrix(x,y,z):
    global matrix
    global connections
    matrix[x, 0].append(y)
    matrix[x, 1].append(z)
    matrix[y, 0].append(x)
    matrix[y, 1].append(z)
    G.add_edge(x, y)
    connections.append(tuple([x,y]))

print("\n\t\033[01m\033[34mStarted\n\033[00m")


G = nx.Graph()


#! Code
start_time = current_time()
start = time.time()

rows = 200

all_nodes = list(range(0,rows))
connections = []
range_list = [[11,12],[2,3],[13,15],[5,6],[6,7]]

population_pct = [0.08,0.28,0.1,0.45,0.09]

interaction_level = [1,2,3]

all_lists, p = random_valandpct(range_list,population_pct,[],[])

int_list = np.random.choice(all_lists, size=rows, p=p)

matrix = np.empty((rows, 3), dtype=object)

for i in tqdm(range(rows)):
    G.add_node(i)
    matrix[i, 0] = []
    matrix[i, 1] = []

matrix[:, 2] = np.random.choice(int_list, size=rows)

population_alc_list = list(range(0,rows))

print()

for k in tqdm(range(rows)):
    while len(matrix[k, 0]) < matrix[k, 2]:

        relation = rm.choice(population_alc_list)
        interaction = rm.choice(interaction_level)

        if relation not in matrix[k, 0] and k not in matrix[relation, 0] and k != relation:
            append_matrix(k,relation,interaction)

        elif all(x in matrix[k, 0] for x in population_alc_list[1:]):

            new_row = np.array([[[], [], 0]], dtype=object)
            matrix = np.append(matrix, new_row, axis=0)

            population_alc_list.append(len(matrix)-1)

            append_matrix(k,len(matrix)-1,interaction)

    population_alc_list.remove(k)

np.savetxt("matrix.txt", matrix, delimiter=",", fmt='%s')

end = time.time()
end_time = current_time()

print(f"\n\t\033[90mStarted at : {start_time}\n\tEnd at : {end_time}\n\n\t\033[36m\033[01mTime taken : {(end-start)} s\033[00m\n")

print("\033[35mExpected\033[00m")

print(f"\033[92mPopulation Number: {rows}\033[00m")

sumofallInteraction = 0
for j in range(rows): sumofallInteraction += matrix[j, 2]
print(f"\033[33m{sumofallInteraction=}\033[00m")

check_pct(int_list,range_list)

new_int_list = []
for l in range(len(matrix)):new_int_list.append(matrix[l, 2])

print("-"*45)

print("\033[35mCreated\033[00m")

print(f"\033[92mPopulation Number: {len(matrix)}\033[00m")

sumofallFINALInteraction = 0
for j in range(rows): sumofallFINALInteraction += len(matrix[j, 0])
print(f"\033[33m{sumofallFINALInteraction=}\033[00m")
print(f"Diff: \033[92m{sumofallFINALInteraction-sumofallInteraction}\033[00m")

acc = check_pct(new_int_list,range_list)

print(f"\n\t\033[01m\033[34mAccuracy: {acc}%\n\033[00m")

# plotgraph(all_nodes=all_nodes,connections=connections)

# Draw the graph
# pos = nx.spring_layout(G)
# pos = nx.circular_layout(G)
# pos = nx.spectral_layout(G)
# nx.draw(G, pos, with_labels=False, node_color='green', edge_color='lightgreen', node_size=20)

# Show the graph
# plt.show()



degrees = dict(G.degree())

# Compute the color map based on the node degrees
vmin, vmax = min(degrees.values()), max(degrees.values())
cmap = plt.get_cmap('inferno')
node_colors = [cmap((degrees[n]-vmin)/(vmax-vmin)) for n in G.nodes()]

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=False, node_color=node_colors, edge_color='lightgrey', node_size=50)

# Show the graph
plt.show()