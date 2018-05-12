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
import SOMA_nextStep
import InitArray

bestChrom = 1
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

	pop = InitArray.initArray(popSize)
	global bestChrom
	solution = [i for i in range(1,popSize+1)] #Initialize array with values from 1 to 46

	#Initialize first population
	for i in range(0,popSize):
		x = random.uniform(0,1) * scale - bounds
		y = random.uniform(0,1) * scale - bounds
		nextChrom = Chrom.Chrom(x,y,0)
		pop[i] = nextChrom

	#Test of initial best
	for j in range(0,popSize):
		pop[j].setCost(FunctionSelect.functionSelect(func, pop[j].coord))

		if (pop[j].getCost() < pop[bestChrom].getCost()):
			bestChrom = j
			bestStep = pop[j].coord

	#Run SOMA
	for k in range(1,maxIter):
		for w in range(0,popSize):
			if (w != bestChrom): #is not the leader
				journeyLength = 0
				#The Journey of individual Chrom
				bestStep = pop[w].coord
				while (journeyLength < pathLength):
					#next step
					pop[w].coord = SOMA_nextStep.SOMA_nextStep(pop[w].coord, pop[bestChrom].coord, stepLength)
					stepCost = FunctionSelect.functionSelect(func, pop[w].coord)

					#check for best step of the individual
					if (stepCost <= pop[w].getCost()):
						pop[w].setCost(stepCost)
						bestStep = pop[w].coord
					journeyLength += stepLength
				#Set individual new best position (from the steps given)
				pop[w].coord = bestStep

		#check new best
		for u in range(0, popSize):
			if (pop[u].getCost() < pop[bestChrom].getCost()):
				bestChrom = u
		#add cost of best chromosome to the solution vector
	
	#Create solution vector
	for s in range(0,popSize):
		solution[s] = pop[s].getCost()
	return solution