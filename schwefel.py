#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - Schwefel Function

"""
Schwefels function is deceptive in that the global minimum 
is geometrically distant, over the parameter space, from the next best local minima. 
Therefore, the search algorithms are potentially prone to convergence in the wrong direction.
"""
import math

def schwefel(x):
	n = len(x)
	s = 0
	cost = 0
	for i in range(0,n-1):
		s += (-x[i]) * math.sin( math.sqrt( abs( x[i] )))
	cost = 418.9829*n + s
	return cost