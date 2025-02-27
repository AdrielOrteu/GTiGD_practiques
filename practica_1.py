import networkx as nx
import matplotlib.pyplot as plt
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

node_id = 0
if node_id in test_graph:
    print(f"Node {node_id}: {list(test_graph.neighbors(node_id))}")
else:
    print(f"Node {node_id} not found.")
print(test_graph.nodes)
print(type(test_graph.nodes))
print(list(test_graph.nodes)[0])

def components_bfs (graph):
    pass

def components_dfs (graph):
    pass

