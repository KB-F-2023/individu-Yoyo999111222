def heuristic(node1, node2, graph):
    x1, y1 = graph[node1]['pos']
    x2, y2 = graph[node2]['pos']
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def astar(graph, start, goal):
    # initialize the starting values
    g = {start: 0}
    f = {start: heuristic(start, goal, graph)}
    visited = set()
    parent = {}

    # search for the shortest path
    while f:
        current_node = min(f, key=f.get)
        if current_node == goal:
            path = []
            while current_node in parent:
                path.append(current_node)
                current_node = parent[current_node]
            path.append(start)
            path.reverse()
            return path

        visited.add(current_node)
        del f[current_node]

        for neighbor, cost in graph[current_node]['edges'].items():
            if neighbor in visited:
                continue
            tentative_g = g[current_node] + cost
            if neighbor not in f or tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + heuristic(neighbor, goal, graph)
                parent[neighbor] = current_node

    # no path found
    return None


def print_shortest_path(graph, start, goal):
    path = astar(graph, start, goal)
    if path is not None:
        print(f"The shortest path from {start} to {goal} is:")
        print(" -> ".join(path))
        for node in graph:
            if node != goal:
                sld = heuristic(node, goal, graph)
                print(f'SLD from {node} to {goal}: {sld:.2f}')
    else:
        print(f"No path found from {start} to {goal}.")


if __name__ == "__main__":
    # define the graph
    graph = {
        'A': {'pos': (0, 0), 'edges': {'B': 1, 'C': 3, 'D': 7}},
        'B': {'pos': (1, 2), 'edges': {'E': 5}},
        'C': {'pos': (3, 4), 'edges': {'F': 2}},
        'D': {'pos': (5, 6), 'edges': {'G': 1, 'H': 2}},
        'E': {'pos': (3, 1), 'edges': {'H': 3}},
        'F': {'pos': (5, 3), 'edges': {'H': 5}},
        'G': {'pos': (7, 7), 'edges': {'H': 2}},
        'H': {'pos': (8, 8), 'edges': {}}
    }

    start = input("Enter the starting node: ")
    goal = input("Enter the goal node: ")

    print_shortest_path(graph, start, goal)
