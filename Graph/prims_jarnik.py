import heapq


class Vertex:
    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.adjacenciesList = list()

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, weight, start_vertex, end_endvertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_endvertex

    def __lt__(self, other):
        return self.weight < other.weight


class Prims_Jarnik:
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.cost = 0
        self.spanning_tree = list()
        self.edge_heap = list()

    def calculate_spanning_tree(self, vertex):
        self.vertex_list.remove(vertex)
        while self.vertex_list:
            for edge in vertex.adjacenciesList:
                if edge.end_vertex in self.vertex_list:
                    heapq.heappush(self.edge_heap, edge)
            min_edge = heapq.heappop(self.edge_heap)
            self.spanning_tree.append(min_edge)
            print("Edge added to spanning tree: %s - %s" % (min_edge.start_vertex.name, min_edge.end_vertex.name))
            self.cost += min_edge.weight
            vertex = min_edge.end_vertex
            self.vertex_list.remove(vertex)


node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")

edge1 = Edge(100, node1, node2)
edge2 = Edge(100, node2, node1)
edge3 = Edge(1000, node1, node3)
edge4 = Edge(1000, node3, node1)
edge5 = Edge(0.01, node3,node2)
edge6 = Edge(0.01, node2, node3)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge3)
node2.adjacenciesList.append(edge2)
node2.adjacenciesList.append(edge6)
node3.adjacenciesList.append(edge4)
node3.adjacenciesList.append(edge5)

unvisitedList = list()
unvisitedList.append(node1)
unvisitedList.append(node2)
unvisitedList.append(node3)

algorithm = Prims_Jarnik(unvisitedList)
algorithm.calculate_spanning_tree(node2)


