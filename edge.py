class Edge(object):

	def __init__(self, v, w, weight):
		self.v = v
		self.w = w
		self.weight = weight

	def either(self):
		return self.v

	def other(self, v):
		return self.v if v == self.w else self.w

	def __repr__(self):
		return f'({self.v}, {self.w}, {self.weight})'

	def __eq__(self, other):
		return self.weight == other.weight

	def __ne__(self, other):
		return self.weight != other.weight

	def __ge__(self, other):
		return self.weight >= other.weight

	def __gt__(self, other):
		return self.weight > other.weight

	def __le__(self, other):
		return self.weight <= other.weight

	def __lt__(self, other):
		return self.weight < other.weight