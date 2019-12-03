import unittest
from graph import Graph
from kruskal import Kruskal

class TestKruskal(unittest.TestCase):

	def setUp(self):
		graph_file = "test_data/graph_data.txt"
		
		with open(graph_file) as stream:
			self.graph = Graph(stream)
			self.mst = Kruskal(self.graph).get_minimum_spaning_tree()
			

	def test_num_node(self):
		V = self.graph.get_num_node()
		self.assertEqual(len(self.mst), V-1)


	def test_compare_with_correct(self):
		correct = [(0,7), (1,7), (0,2), (2,3), (5,7), (4,5), (6,2)]

		for edge in self.mst:			
			v = edge.either()
			w = edge.other(v)

			in_correct = False
			for candidate in correct:
				if (v, w) == candidate or (w, v) == candidate:
					in_correct = True
			self.assertTrue(in_correct)