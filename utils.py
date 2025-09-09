import networkx as nx

def find_path(G, start, end):
    path = nx.dijkstra_path(G, start, end)
    length = nx.dijkstra_path_length(G, start, end)
    return path, length

def greedy_tsp(start, points, G):
    unvisited = set(points)
    path = [start]
    total_dist = 0
    current = start
    while unvisited:
        next_node = min(unvisited, key=lambda node: nx.dijkstra_path_length(G, current, node))
        total_dist += nx.dijkstra_path_length(G, current, next_node)
        path.append(next_node)
        unvisited.remove(next_node)
        current = next_node
    return path, total_dist
