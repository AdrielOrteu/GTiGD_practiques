import networkx as nx
import matplotlib.pyplot as plt
import random

def create_simple_graph (num_nodes=10, num_edges=15):
    # Create an empty graph
    G = nx.Graph()
    # Add nodes
    G.add_nodes_from(range(num_nodes))

    edges = set()
    while len(edges) < num_edges:
        u, v = random.sample(range(num_nodes), 2)  # Pick two distinct nodes
        edges.add((u, v))
    G.add_edges_from(edges)
    return G

my_graph = create_simple_graph()

def show_graph (graph):
    nx.draw(graph, with_labels=True)
    plt.show()
