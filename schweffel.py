#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - Schweffel Function

"""
Schwefels function is deceptive in that the global minimum 
is geometrically distant, over the parameter space, from the next best local minima. 
Therefore, the search algorithms are potentially prone to convergence in the wrong direction.
"""

def schweffel(x):
	n = len(x)
	return 418.9829*n - sum( x * sin( sqrt( abs( x ))))