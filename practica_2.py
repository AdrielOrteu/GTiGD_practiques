import networkx as nx
import random
import typing
from grafSimple import *
from practica_1 import components_bfs


def task_1():
    # G = create_simple_graph(20,10)
    G = project_graph_create()
    cliques_dict = dict()
    def simulate_coincidence(average=0.5, deviation=0.15):
        for edge in G.edges:
            w = random.normalvariate(average, deviation)
            if w < 0:
                w = 0
            elif w > 1:
                w = 1
            G[edge[0]][edge[1]]["weight"] = w
    
    def how_many_cliques(n, average=0.5, deviation=0.15):
        graph = nx.Graph()
        edges = set()
        for edge in G.edges:
            if G[edge[0]][edge[1]]["weight"] >= n:
                edges.add(edge)
        graph.add_edges_from(edges)
        graph_2, components_lst = components_bfs(graph=graph)
        
        for component in components_lst:
            if len(component) in cliques_dict:
                cliques_dict[len(component)] +=1
            else:
                cliques_dict[len(component)] = 1
        return graph, graph_2
    
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
    
    
    simulate_coincidence()
    #draw_weighted_graph(G)
    H, K = how_many_cliques(n=0.75)
    #show_graph(H)
    show_graph(K)
    print(cliques_dict)

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
    import pandas as pd
    
    @timer
    def greedy_coloring(graph, algorythm="random_sequential"):
        # Apply greedy coloring
        graph_coloring = nx.greedy_color(G=graph, strategy=algorythm) # creates a dictionary where the keys are the nodes and the values are the colors
        #print(graph_coloring)
        unique_colors = set(graph_coloring.values())
        return graph_coloring, unique_colors
      
    def show_colored_graph(graph, unique_colors, graph_coloring):
        # Assign colors to nodes based on the greedy coloring
        graph_color_to_mpl_color = dict(zip(unique_colors, plt.cm.get_cmap("tab20").colors))  # creates a dictionary where the keys are the colors and the values are the tableau-color names (intermediate step for MatPlotLib to understand)
        node_colors = [graph_color_to_mpl_color[graph_coloring[n]] for n in graph.nodes()]
        pos = nx.spring_layout(graph, seed=14)
        nx.draw(graph, pos, with_labels=True, node_color=node_colors)
        plt.show()
    
    def test_bipartite(graph):
        return nx.is_bipartite(graph)
    
    def test_algorithm():
        algorithm_properties = dict()
        test_graph = project_graph_create()
        algorythm_types = (
            "largest_first",
            "random_sequential",
            "smallest_last",
            "independent_set",
            "connected_sequential_bfs",
            "connected_sequential_dfs",
            "saturation_largest_first",
        )
        for algorythm in algorythm_types:
            # print(algorythm)
            avg_c = 0
            avg_t = 0
            for i in range(10):
                test_graph = project_graph_create()
                coloring, colors, t = greedy_coloring(test_graph, algorythm)
                avg_c += len(colors)
                avg_t += t
                # print(i)
                
            algorithm_properties [algorythm] = (avg_c/10, avg_t/10)
        
        return algorithm_properties
    
    def test_efficiency(algorythm):
        test_list = [i for i in range(100, 27808, 100)]
        print(test_list)
        size_dict = dict()
        for s in test_list:
            G = project_graph_create(size=s)
            graph_coloring, unique_colors, t = greedy_coloring(G, algorythm=algorythm)
            size_dict[s] = (len(unique_colors), t)
        return size_dict
    
    efficiency_dict = test_efficiency("smallest_last")
    time_df = pd.read_csv("Time.csv")
    for edge_num in efficiency_dict:
        print(efficiency_dict[edge_num])
        new_row = {"edge_num":edge_num, "colors_used": efficiency_dict[edge_num][0], "time_taken": efficiency_dict[edge_num][1]}
        #time_df.iloc[-1,0] = edge_num
        #time_df.iloc[-1,1] = efficiency_dict[edge_num][0]
        #time_df.iloc[-1,2] = efficiency_dict[edge_num][1]
        time_df = pd.concat([time_df, pd.DataFrame([new_row])])
    
    time_df.to_csv("Time.csv", index=False)
    

task_3()
