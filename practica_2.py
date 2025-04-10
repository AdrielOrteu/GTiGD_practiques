import networkx as nx
import random
import typing
from grafSimple import *


def task_1():
    
    def simulate_coincidence(average, deviation):
        pass
    
    def how_many_cliques(n, average, deviation):
        pass
    


def task_2():
    pass


def task_3():
    import matplotlib.colors as mpl
    import matplotlib.pyplot as plt
    
    @timer
    def greedy_coloring(graph):
        # Apply greedy coloring
        graph_coloring = nx.greedy_color(graph) # creates a dictionary where the keys are the nodes and the values are the colors
        print(graph_coloring)
        unique_colors = set(graph_coloring.values())
        return graph, graph_coloring, unique_colors
    
    
    
    def show_colored_graph(graph):
        # Assign colors to nodes based on the greedy coloring
        graph_color_to_mpl_color = dict(zip(unique_colors, plt.cm.get_cmap("tab20").colors))  # creates a dictionary where the keys are the colors and the values are the tableau-color names (intermediate step for MatPlotLib to understand)
        node_colors = [graph_color_to_mpl_color[graph_coloring[n]] for n in G.nodes()]
        pos = nx.spring_layout(graph, seed=14)
        nx.draw(graph, pos, with_labels=True, node_color=node_colors)
        plt.show()
    
    
    test_list = [ [ (i**2, j**2) for j in range(2, i**2)] for i in range(10, 20)]
    print(test_list)
    for test_group in test_list:
        for test in test_group:
            print("\n###_NEW-TEST_###")
            G = create_simple_graph(test[0], test[1])
            print(test)
            # show_graph(G)
            
            G, graph_coloring, unique_colors = greedy_coloring(G)
            print(f"num of colors needed: {len(unique_colors)}\ncolors used dictionary: {graph_coloring}")
            # show_colored_graph(G)
    
task_3()
