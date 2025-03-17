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


def tree_to_russian_doll(tree, head):
    pass

def components_bfs (graph):
    pass

def components_dfs (graph, current_node):
    dfs_graph = Graph()
    dfs_dict = dict()
    visited_nodes = set()
    node_list = list(graph.nodes)
    
    while len(node_list) > len(visited_nodes):
        visited_nodes.add(current_node)
        adj_edges = list(graph.adj[current_node])
        
        n=0
        while adj_edges[n] in visited_nodes and n < (len(adj_edges)-1):
            n+=1
        
        if adj_edges[n] in visited_nodes:
            current_node = dfs_dict[current_node]
        else:
            dfs_dict[adj_edges[n]] = current_node
            dfs_graph.add_edge(current_node, adj_edges[n])
            current_node = adj_edges[n]
    return dfs_graph

a = list(p1_graph.nodes)
test_G = components_dfs(p1_graph, a[0])
# show_graph(test_G)
