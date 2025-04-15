import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import pandas as pd

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        
        with open("Time.csv", "a") as time_register:
            time_register.write(f"node_num,edge_num,{t2 - t1:.6f}\n")
        #print(f"Execution time: {t2 - t1:.6f} seconds")
        return result
    return wrapper

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
    pos = nx.spring_layout(graph, seed=14)
    nx.draw(graph, pos, with_labels=True)
    plt.show()


def project_graph_create (size=27808):
    graph = nx.Graph()
    with open("lastfm_asia_edges.csv", "r") as relationships_csv :
        relationships_csv.readline() # we use .readline() to skip the header (first line) by reading it before entering the for loop
        edges = set()
        n=1
        for edge in relationships_csv:
            edge = edge.strip().split(",")
            edges.add((edge[0], edge[1]))
            if n >= size:
                break
        graph.add_edges_from(edges)
    return graph

