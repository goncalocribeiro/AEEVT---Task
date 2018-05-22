#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - DE ALGORITHM

import InitArray
import random
import Chrom
import FunctionSelect

def de(func):
	if (func==1) or (func==2): #DeJong1 or DeJong2
		bounds = 5
		scale = 10
	elif func==3: #Schwefel
		bounds = 500
		scale = 1000
	else:
		print ("Check DE param")
		return

	#Algorithm parameters
	factor = 0.9 #mutation factor
	cRate = 0.5 #crossover rate (!!! not used in code, don't change, see line 80)
	popSize = 50 #size of population
	maxIter = 2000 #maximum number of iterations
	#Max. FES 10 000

	solution = [i for i in range(1,maxIter+1)]
	currentPop = InitArray.initArray(popSize);
	bestChrom = 1;

	#Initializing first population
	for i in range(0,popSize):
		x = random.uniform(0,1) * scale - bounds
		y = random.uniform(0,1) * scale - bounds
		nextChrom = Chrom.Chrom(x,y,0)
		currentPop[i] = nextChrom

	#Test of initial best
	for j in range(0,popSize):
		pop[j].setCost(FunctionSelect.functionSelect(func, pop[j].coord))

		if (pop[j].getCost() < pop[bestChrom].getCost()):
			bestChrom = j

	#Run DE
	for k in range(1,maxIter):
		#Next generation creation
		nextPop = InitArray.initArray(popSize)
		for w in range(0,popSize):
			if (w!=1): #Reserved for the best chromosome
				#Random selection from population
				#r1 = best
				#r2 = random
				#r3 = random
				rList = [[rel] for rel in range(popSize)]
				random.shuffle(rList)

				if(w == rList[w]):
					del(rList[w]) #remove element from list

				r2 = rList[0]
				r3 = rList[1]

				r1Chrom = currentPop[bestChrom]
				r2Chrom = currentPop[r2]
				r3Chrom = currentPop[r3]

				#Mutation - Differential vector creation
				diffVx = r2Chrom.coord.getX() - r3Chrom.coord.getX()
				diffVy = r2Chrom.coord.getY() - r3Chrom.coord.getY()
				wDiffVx = diffVx * factor
				wDiffVy = diffVy * factor
				diffV = Chrom.Chrom(wDiffVx, wDiffVy);

				#Noisy vector creation
				noisyVx = diffV.coord.getX() + r1Chrom.coord.getX()
				noisyVy = diffV.coord.getY() + r1Chrom.coord.getY()
				noisyV = Chrom.Chrom(noisyVx, noisyVy)