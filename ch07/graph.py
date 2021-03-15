"""
Home-grown replacement for networkx IN CASE this package is not found.
This implementation is not meant to be production-quality, but simply
a stub object that provides a reasonable implementation.

Note: Doesn't offer capability to draw graphs.
"""
from algs.node import Node

class UndirectedGraph:
    """
    Use Dictionary to store all vertices. Values are lists of neighboring nodes.
    """
    def __init__(self):
        self.adjacency = {}
        self.positions = {}

    def add_node(self, u, pos=None):
        """Add node to graph, if not already there."""
        if u in self.adjacency:
            return
        self.adjacency[u] = None
        self.positions[u] = pos

    def add_nodes_from(self, nodes):
        """Add nodes to graph, if not already there."""
        for n in nodes:
            self.add_node(n)

    def __getitem__(self, u):
        """Get neighboring nodes to this node."""
        for node in self.adjacency[u]:
            yield node

    def nodes(self):
        """Return all nodes."""
        return self.adjacency.keys()

    def edges(self, u=None):
        """Return all edges. Make sure not to double count..."""
        all_nodes = list(self.nodes())
        
        if u:
            n = self.adjacency[u]
            while n:
                yield (u, n.value)
                n = n.next
        else:
            seen = []
            for u in all_nodes:
                n = self.adjacency[u]
                while n:
                    if not n.value in seen:
                        yield (u, n.value)
                    n = n.next
                seen.append(u)

    def neighbors(self, u):
        """Return neighboring nodes."""
        for node in self.adjacency[u]:
            yield node
    
    def add_edge(self, u, v):
        """Add edge (u,v) to a graph."""
        if not u in self.adjacency:
            self.adjacency[u] = None
            
        if not v in self.adjacency:
            self.adjacency[v] = None

        n = self.adjacency[v]
        while n:
            if n.value == v:
                return   # already there
            n = n.next
            
        self.adjacency[u] = Node(v, self.adjacency[u])
        self.adjacency[v] = Node(u, self.adjacency[v])

    def add_edges_from(self, edges):
        """Add edges to graph, if not already there."""
        for u,v in edges:
            self.add_edge(u,v)
            
class MatrixUndirectedGraph:
    """
    Use Two Dimensional Matrix to store whether there is an edge between U and V.
    """
    def __init__(self):
        self.matrix = None
        self.positions = []
        self.labels = []

    def add_node(self, u, pos=None):
        """Add node to graph, if not already there."""
        if u in self.labels:
            return
        self.labels.append(u)
        self.positions.append(pos)
        N = len(self.labels)

        # Either initialize 1x1 matrix or extend with new column and one new '0' in each column.
        if self.matrix is None:
            self.matrix =  [[0] * 1] * 1
        else:
            self.matrix.append([0] * (N-1))
            for i in range(N):
                self.matrix[i].append(0)

    def add_nodes_from(self, nodes):
        """Add nodes to graph, if not already there."""
        for n in nodes:
            self.add_node(n)

    def __getitem__(self, u):
        """Get neighboring nodes to this node by iterating over all nodes."""
        idx = self.labels.index(u)
        for j in range(len(self.labels)):
            if self.matrix[idx][j]:
                yield self.labels[j]

    def nodes(self):
        """Return all nodes."""
        for n in self.labels:
            yield n

    def edges(self, u=None):
        """Return all edges. Make sure not to double count..."""
        if u:
            idx = self.labels.index(u)
            for j in range(len(self.labels)):
                if self.matrix[idx][j]:
                    yield (self.labels[idx], self.labels[j])
        else:
            for i in range(len(self.labels)-1):
                for j in range(i+1, len(self.labels)):
                    if self.matrix[i][j]:
                        yield  (self.labels[i], self.labels[j]) 

    def neighbors(self, u):
        """Return neighboring nodes."""
        idx = self.labels.index(u)
        for j in range(len(self.labels)):
            if self.matrix[idx][j]:
                yield self.labels[j]

    def add_edge(self, u, v):
        """Add edge (u,v) to a graph."""
        if not u in self.labels:
            self.add_node(u)

        if not v in self.labels:
            self.add_node(v)

        # already there
        i = self.labels.index(u)
        j = self.labels.index(v)
        if self.matrix[i][j]:
            return
        self.matrix[i][j] = True
        self.matrix[j][i] = True

    def add_edges_from(self, edges):
        """Add edges to graph, if not already there."""
        for u,v in edges:
            self.add_edge(u,v)            

class DirectedGraph:
    """
    Use Dictionary to store all vertices. Values are lists of neighboring nodes.
    """
    def __init__(self):
        self.adjacency = {}
        self.positions = {}
 
    def add_node(self, u, pos=None):
        """Add node to graph, if not already there."""
        if u in self.adjacency:
            return
        self.adjacency[u] = []
        self.positions[u] = pos

    def add_nodes_from(self, nodes):
        """Add nodes to graph, if not already there."""
        for n in nodes:
            self.add_node(n)

    def __getitem__(self, u):
        """Get neighboring nodes to this node."""
        if u in self.adjacency:
            for node in self.adjacency[u]:
                yield node

    def nodes(self):
        """Return all nodes."""
        return self.adjacency.keys()

    def edges(self, u=None):
        """Return all edges."""
        if u:
            for v in self.adjacency[u]:
                yield (u, v)
        else:
            for u in self.nodes():
                for v in self.adjacency[u]:
                    yield (u, v)

    def add_edge(self, u, v):
        """Add edge from u => v."""
        if not u in self.adjacency:
            self.adjacency[u] = []

        if not v in self.adjacency:
            self.adjacency[u] = []

        # already there
        if v in self.adjacency[u]:
            return
        self.adjacency[u].append(v)

    def add_edges_from(self, edges):
        """Add edges to graph, if not already there."""
        for u,v in edges:
            self.add_edge(u,v)

class Replacement:
    """Provides an object which can fill the role of 'nx' in the graph chapter code."""
    def __init__(self):
        pass

    def Graph(self):
        """Create undirected graph."""
        return MatrixUndirectedGraph()    # UndirectedGraph

    def DiGraph(self):
        """Create directed graph."""
        return DirectedGraph()

    def topological_sort(self, digraph):
        """Link in with Topological sort."""
        from ch07.digraph_search import topological_sort
        return topological_sort(digraph)

    def get_node_attributes(self, graph):
        """I am not going to provide this capability."""
        return graph.positions

    def draw(self, graph, pos, with_labels = True, node_color="w", font_size=8, ax=None):
        """I am not going to provide this capability."""
        pass
