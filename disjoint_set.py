class DisjointSet(object):

	def __init__(self, n):
		self.parent = [i for i in range(n)]
		self.rank = [0 for _ in range(n)]


	def union(self, u, v):
		u = self.find(u)
		v = self.find(v)

		if u == v:
			return 

		if self.rank[u] > self.rank[v]:
			temp = v
			v = u
			u = temp

		self.parent[u] = v

		if self.rank[u] == self.rank[v]:
			self.rank[v] += 1


	def isConnected(self, u, v):
		return self.find(u) == self.find(v)


	def find(self, u):
		if u == self.parent[u]: 
			return u
		return self.find(self.parent[u])