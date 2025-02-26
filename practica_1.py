import networkx as nx
import matplotlib.pyplot as plt

def build_last_graph ():
    graph = nx.Graph()
    with open("lastfm_asia_edges.csv", "r") as relationships_csv :
        relationships_csv.readline() # we use .readline() to skip the header (first line) by reading it before entering the for loop
        edges = set()
        for edge in relationships_csv:
            edge = edge.strip().split(",")
            edges.add((edge[0], edge[1]))
        graph.add_edges_from(edges)
    return graph

p1_graph = build_last_graph ()
