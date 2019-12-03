import unittest
from graph import Graph

class TestMakeGraph(unittest.TestCase):
	def setUp(self):
		graph_file = "test_data/graph_data.txt"
		with open(graph_file) as stream:
			self.adj = Graph(stream).get_adj()

	def test_adj(self):
		# 각 노드 별 간선 개수
		n_vertex_edge = [4,4,5,3,4,3,4]
		for vertex, n_edge in enumerate(n_vertex_edge):
			self.assertEqual(len(self.adj[vertex]), n_edge)