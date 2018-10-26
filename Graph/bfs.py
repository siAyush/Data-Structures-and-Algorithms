from collections import defaultdict

class Node():
    def __init__(self,name):
        self.name = name
        self.visited = False

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,start,end):              # start and ending vertex
        self.graph[start].append(end)

    def bfs(self,start):
        queue = []
        queue.append(start)
        start.visited = True
        while queue:
            actualnode = queue.pop(0)
            print(actualnode.name)
            for i in self.graph:
                if not i.visited:
                    queue.append(i)
                    i.visited = True


node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");

g = Graph()
g.add_edge(node1,node2)
g.add_edge(node1,node3)
g.add_edge(node2,node4)
g.add_edge(node4,node5)
g.bfs(node1)
print(g.graph.items())
