import unittest
from edge import Edge 


class TestEdgeOperator(unittest.TestCase):

	def setUp(self):
		self.v = 0
		self.w = 1
		self.A = Edge(self.v, self.w, 5)
		self.B = Edge(self.v, self.w, 5)
		self.C = Edge(self.v, self.w, 7)

	def test_either(self):
		self.assertEqual(self.A.either() == self.v, True)
		self.assertEqual(self.A.either() == self.w, False)

	def test_other(self):
		self.assertEqual(self.A.other(self.v) == self.w, True)
		self.assertEqual(self.A.other(self.w) == self.v, True)

	def test_eq(self):
		self.assertEqual(self.A == self.B, True)
		self.assertEqual(self.A == self.C, False)

	def test_ne(self):
		self.assertEqual(self.A != self.C, True)
		self.assertEqual(self.A != self.B, False)

	def test_ge(self):
		self.assertEqual(self.C >= self.A, True)
		self.assertEqual(self.B >= self.A, True)
		self.assertEqual(self.A >= self.C, False)

	def test_gt(self):
		self.assertEqual(self.C > self.A, True)
		self.assertEqual(self.B > self.A, False)
		self.assertEqual(self.A > self.C, False)

	def test_le(self):
		self.assertEqual(self.A <= self.C, True)
		self.assertEqual(self.A <= self.B, True)
		self.assertEqual(self.C <= self.A, False)

	def test_lt(self):
		self.assertEqual(self.A < self.C, True)
		self.assertEqual(self.A < self.B, False)
		self.assertEqual(self.C < self.A, False)

if __name__ == '__main__':
	unittest.main()