from edge import Edge


class Graph(object):

	DATA_FORMAT_ERROR_MESSAGE = "간선 정보는  'source dest weight' 로 표기되어야 합니다." 

	def __init__(self, stream):
		edges = []
		num_node = -1
		
		for line in stream.readlines():
			line = line.strip(" \n\t")
			info =  line.split(" ")

			assert len(info) == 3, DATA_FORMAT_ERROR_MESSAGE

			v, w, weight = info
			v = int(v)
			w = int(w)
			weight= float(weight)

			num_node = max(num_node, v, w)

			edges.append(Edge(v, w, weight))
		num_node += 1

		self.num_node = num_node

		self.edges = edges
		
		self.adj = [[] for _ in range(self.num_node)]
		for edge in edges:
			self.addEdge(edge)


	def addEdge(self, edge):
		v = edge.either()
		w = edge.other(v)
		self.adj[v].append(edge)
		self.adj[w].append(edge)


	def get_edges(self):
		return self.edges


	def get_adj(self):
		return self.adj


	def get_num_node(self):
		return self.num_node
