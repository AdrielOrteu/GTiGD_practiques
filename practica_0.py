import networkx as nx
import matplotlib.pyplot as plt
from networkx import DiGraph

G = nx.Graph() #is a simple graph
 #dG = nx.DiGraph() #is a directed graph
 #mG = nx.MultiGraph() #is a graph multi graph
 #dmG = nx.MultiDiGraph() #is a directed multi graph

# G.add_edge(1,2, weight=0.9) #crates an edge from vertex 1 to vertex 2, with a set weight (if nodes 1 and 2 don't exist it creates them)
# G.add_edge("A", "B")
# G.add_edge("B", "B")
# G.add_edge(1, "B")
# G.add_node("C")
# G.add_node(print) # you can pass as a node anything that is hashable (essentialy, if it's an object (functions in python are objects) )
# G.add_edge("C", print)
# G.add_edge("C",2)
# G.add_edge("A", 2)
# G.add_edge("A", "C")
# G.add_edge(1, list)
# nx.draw(G, with_labels=True)
# plt.show()




def brooklin_99_relationships ():
	G = nx.Graph()
	G.add_edge("jake", "charles")
	G.add_edge("jake", "raymond")
	G.add_edge("jake", "amy")
	G.add_edge("amy", "gina")
	G.add_edge("charles", "gina")
	return G

def XOI_sistem ():
	G = nx.DiGraph()
	G.add_nodes_from([2, 3])
	G.add_nodes_from(range(100, 110))
	H = nx.path_graph(10)
	G.add_nodes_from(H)
	G.add_edge(1, 2)
#	G.add_edges_from([(1, 2), (1, 3)])
	return G


brookin_99 = brooklin_99_relationships()
comunications_sistem = XOI_sistem()

nx.draw(brookin_99, with_labels=True)
plt.show()
nx.draw(comunications_sistem, with_labels=False)
plt.show()
