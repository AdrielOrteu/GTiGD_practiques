import networkx as nx
import random
import typing
from grafSimple import project_graph_create, create_simple_graph, show_graph


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
    
    G = create_simple_graph()
    # Apply greedy coloring
    show_graph(G)
    graph_coloring = nx.greedy_color(G) # creates a dictionary where the keys are the nodes and the values are the colors
    unique_colors = set(graph_coloring.values())
    # Assign colors to nodes based on the greedy coloring
    graph_color_to_mpl_color = dict(zip(unique_colors, mpl.TABLEAU_COLORS)) # creates a dictionary where the keys are the colors and the values are the color names (for MatPlotLib to understand)
    node_colors = [graph_color_to_mpl_color[graph_coloring[n]] for n in G.nodes()]
    print(node_colors)
    
    pos = nx.spring_layout(G, seed=14)
    nx.draw(G, pos, with_labels=True, node_color=node_colors)
    plt.show()
task_3()