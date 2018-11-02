import graph


def dfs(graph, start):
    explored = []
    queue = [start]
    while queue:
        node = queue.pop()
        if node not in explored:
            explored.append(node)
            neighbours = [i for i in graph.outgoing[node].keys()]
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored