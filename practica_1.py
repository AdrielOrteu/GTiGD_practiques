import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.Graph()
node_lst = [0,1,2,3,4,5,6,7,8,9]
G.add_nodes_from(node_lst)
for i in range(15):
	a = random.randint(0, 9)
	b = random.randint(0, 9)
	while a in chosen and b in chosen and a != b:
		a = random.randint(0,9)
		b = random.randint(0, 9)
	G.add_edge(a,b)
