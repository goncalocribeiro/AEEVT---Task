#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - SOMA ALGORITHM - Self Organizing Migrating Algorithm - Stochastic Optimization Algorithms

"""
SOMA, which can also works on a population of individuals, 
is based on the self-organizing behavior of groups of individuals in a social environment. 
It can also be classified as an evolutionary algorithm, 
despite the fact that no new generations of individuals are created during the search
"""
import random
import Chrom
import FunctionSelect

def soma(func):
	if (func==1) or (func==2): #DeJong1 or DeJong2
		bounds = 5
		scale = 10
	elif func==3: #Schwefel
		bounds = 500
		scale = 1000
	else:
		print ("Check soma param")
		return

	#Algorithm parameters
	pathLength = 3 #length of path
	stepLength = 0.33 #length of step
	popSize = 25 #size of population
	maxIter = 46 #maximum iteration
	#Max. FES 10 036

	pop = InitArray(popSize)
	bestChrom = 1
	solution = [i for i in range(1,popSize+1)] #Initialize array with values from 1 to 25

	#Initialize first population
	for i in range(1,popSize):
		x = random.uniform(0,1) * scale - bounds
		y = random.uniform(0,1) * scale - bounds
		nextChrom = Chrom(x,y)
		pop[i] = nextChrom

	#Test of initial best
	for j in range(1,popSize):
		pop[j].setCost(functionSelect(func, pop[j].coord))

		if (pop[j].cost < pop[bestChrom].cost):
			bestChrom = j
			bestStep = pop[j].coord

	#Run SOMA
	

	return