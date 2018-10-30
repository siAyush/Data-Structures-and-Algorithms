class Graph:
    def __init__(self, directed=False):
        self.outgoing = {}
        self.incoming = {} if directed else self.outgoing

    def is_directed(self):
        return self.incoming is not self.outgoing

    def vertex_count(self):
        return len(self.outgoing)

    def vertices(self):
        return self.outgoing.keys()

    def edge_count(self):
        total = sum(len(self.outgoing[v]) for v in self.outgoing)
        return total if self.is_directed() else total//2

    def edges(self):
        result = set()
        for secondary_map in self.outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self,u,v):
        """
        :param u: start vertex
        :param v: end vertex
        :return: edge u to v or None if not adjacent
        """
        return self.outgoing[u][v]

    def degree(self, v, outgoing=True):
        """
        Return number of (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self.outgoing if outgoing else self.incoming
        return len(adj[v])

    def insert_vertex(self, v):
        self.outgoing[v] = {}
        if self.is_directed():
            self.incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        self.outgoing[u][v] = x
        self.incoming[v][u] = x
