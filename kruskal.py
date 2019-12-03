from queue import PriorityQueue
from disjoint_set import DisjointSet


class Kruskal(object):

    def __init__(self, graph):
        pq = PriorityQueue()
        for edge in graph.get_edges():
            pq.put(edge)

        V = graph.get_num_node()
        disjoint_set = DisjointSet(V)

        minimum_spaning_tree = []
        while not pq.empty() or len(minimum_spaning_tree) < V-1:
            edge = pq.get()
            v = edge.either()
            w = edge.other(v)
            
            if not disjoint_set.isConnected(v,w):
                disjoint_set.union(v,w)
                minimum_spaning_tree.append(edge)
        self.mst = minimum_spaning_tree


    def get_minimum_spaning_tree(self):
        return self.mst