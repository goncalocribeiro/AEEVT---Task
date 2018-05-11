#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - Schweffel Function

"""
Schwefels function is deceptive in that the global minimum 
is geometrically distant, over the parameter space, from the next best local minima. 
Therefore, the search algorithms are potentially prone to convergence in the wrong direction.
"""
import math

def schwefel(x):
	n = len(x)
	for i in range(0,n):
		x[i] = 418.9829*n + (-x[i]) * math.sin( math.sqrt( abs( x[i] )))
	return x