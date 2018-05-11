#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - Chrom class

import Coord

class Chrom:
	def __init__(self, x, y):
		self.coord = Coord(x,y)
		
	def setCost(self, cost):
		self.cost = cost