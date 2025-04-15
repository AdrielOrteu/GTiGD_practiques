import networkx as nx
import random
import typing
from grafSimple import *


def task_1():
    G = create_simple_graph()
    def simulate_coincidence(average=0.5, deviation=0.15):
        for edge in G.edges:
            w = random.normalvariate(average, deviation)
            if w < 0:
                w = 0
            elif w > 1:
                w = 1
            G[edge[0]][edge[1]]["weight"] = w
    
    def how_many_cliques(n, average, deviation):
        pass
    
    simulate_coincidence()
    
    def draw_weighted_graph(graph):
        """
        Draws a weighted graph with labeled nodes and edge weights.
        """
        # Compute positions for the nodes
        pos = nx.spring_layout(graph)
        
        # Draw nodes and edges
        nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=700, edge_color='gray')
        
        # Extract and draw edge weights
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        edge_labels = {edge: f"{weight:.2f}" for edge, weight in edge_labels.items()}  # Format weights
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
        
        # Show the plot
        plt.title("Weighted Graph")
        plt.show()
    
    draw_weighted_graph(G)
    


def task_2():
    n = int(input("Introduce cantidad de números a elegir (n): "))
    m = int(input("Introduce cantidad de números posibles (m): "))

    combinacion = input("Introduce el código: ")
    combinacion = list(map(int, combinacion.split()))
    combinacion.sort()

    intentos = 0
    ganador = []

    while combinacion != ganador:
        ganador = random.sample(range(1, m + 1), n)
        ganador.sort()
        intentos += 1

    print(f"Has ganado tras {intentos} intentos.")





def task_3():
    import matplotlib.colors as mpl
    import matplotlib.pyplot as plt

    @timer
    def greedy_coloring(graph):
        # Apply greedy coloring
        graph_coloring = nx.greedy_color(graph) # creates a dictionary where the keys are the nodes and the values are the colors
        #print(graph_coloring)
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
    #print(test_list)
    for test_group in test_list:
        for test in test_group:
            #print("\n###_NEW-TEST_###")
            G = create_simple_graph(test[0], test[1])
            #print(test)
            # show_graph(G)

            G, graph_coloring, unique_colors = greedy_coloring(G)
            #print(f"num of colors needed: {len(unique_colors)}\ncolors used dictionary: {graph_coloring}")
            # show_colored_graph(G)


task_1()
