import unittest
from disjoint_set import DisjointSet

class TestDisjointSet(unittest.TestCase):

	def setUp(self):
		self.disjoint_set = DisjointSet(6)
		self.disjoint_set.union(0,1)
		self.disjoint_set.union(1,2)
		self.disjoint_set.union(4,5)


	def test_disjoint_set(self):
		self.assertTrue(self.disjoint_set.isConnected(1,2))
		self.assertFalse(self.disjoint_set.isConnected(2,4))
		self.assertFalse(self.disjoint_set.isConnected(0,3))