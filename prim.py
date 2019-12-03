from queue import PriorityQueue

class Prim(object):

	EMPTY_GRAPH_ERROR_MESSAGE = "그래프는 최소한 한 개의 노드를 가져야 합니다."

	def __init__(self, graph):
		self.mst = []
		self.graph = graph
		V = self.graph.get_num_node()
		self.marked = [False] * graph.get_num_node()
		self.pq = PriorityQueue()

		assert V > 0, EMPTY_GRAPH_ERROR_MESSAGE

		self.visit(0)
		while not self.pq.empty() and len(self.mst) < V-1:
			edge = self.pq.get()
			v = edge.either()
			w = edge.other(v)
			
			if self.marked[v] and self.marked[w]:
				continue

			self.mst.append(edge)
			if not self.marked[v]:
				self.visit(v)
			if not self.marked[w]:
				self.visit(w)


	def visit(self, vertex):
		self.marked[vertex] = True
		for edge in self.graph.get_adj()[vertex]:
			if not self.marked[edge.other(vertex)]:
				self.pq.put(edge)


	def get_minimum_spaning_tree(self):
		return self.mst