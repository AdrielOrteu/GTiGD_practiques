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
    G = create_simple_graph()
    # Apply greedy coloring
    graph_coloring = nx.greedy_color(G)
    unique_colors = set(graph_coloring.values())
    
    # Assign colors to nodes based on the greedy coloring
    graph_color_to_mpl_color = dict(zip(unique_colors, mpl.TABLEAU_COLORS))
    node_colors = [graph_color_to_mpl_color[graph_coloring[n]] for n in G.nodes()]
    
    pos = nx.spring_layout(G, seed=14)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=500,
        node_color=node_colors,
        edge_color="grey",
        font_size=12,
        font_color="#333333",
        width=2,
    )
    
    show_graph(G)
task_3()