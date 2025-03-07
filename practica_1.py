import networkx as nx
import matplotlib.pyplot as plt
from networkx import Graph

from grafSimple import create_simple_graph, show_graph

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
test_graph = create_simple_graph()
show_graph(test_graph)



def components_bfs (graph):
    pass

def components_dfs (graph, current_node):
    dfs_graph = Graph()
    node_list = list(graph.nodes)
    edge_list = list(graph.edges)
    while len(node_list) != 0:
        for edge in edge_list:
            if current_node in edge:
                dfs_graph.add_edge(current_node, )
                current_node = edge[1]
                
        
        current_node = 1

