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


def show_graph (graph):
    nx.draw(graph, with_labels=True)
    plt.show()


def project_graph_create ():
    graph = nx.Graph()
    with open("lastfm_asia_edges.csv", "r") as relationships_csv :
        relationships_csv.readline() # we use .readline() to skip the header (first line) by reading it before entering the for loop
        edges = set()
        for edge in relationships_csv:
            edge = edge.strip().split(",")
            edges.add((edge[0], edge[1]))
        graph.add_edges_from(edges)
    return graph

