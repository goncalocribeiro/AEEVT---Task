#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - Chrom class

import Coord

class Chrom:
	def __init__(self, x, y, cost):
		self.coord = Coord.Coord(x,y)
		self.cost = cost

	def setCost(self, cost):
		self.cost = cost

	def getCost(self):
		return self.cost