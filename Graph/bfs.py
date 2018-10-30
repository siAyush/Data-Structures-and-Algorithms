import graph


def bfs(self, start):
    queue = list()
    queue.append(start)
    start.visited = True
    while queue:
        actual_node = queue.pop(0)
        print(actual_node.name)
        for i in self.graph:
            if not i.visited:
                queue.append(i)
                i.visited = True
