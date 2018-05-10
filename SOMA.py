#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - SOMA ALGORITHM - Self Organizing Migrating Algorithm - Stochastic Optimization Algorithms

"""
SOMA, which can also works on a population of individuals, 
is based on the self-organizing behavior of groups of individuals in a social environment. 
It can also be classified as an evolutionary algorithm, 
despite the fact that no new generations of individuals are created during the search
"""
def soma(func):
	if (func==1) or (func==2): #DeJong1 or DeJong2
		bounds = 5
		scale = 10
	elif func==3: #Schweffel
		print "schweffel"
		bounds = 500
		scale = 1000
	else:
		print "Check soma param"
	return