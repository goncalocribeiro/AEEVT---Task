#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - SOMA NEXT STEP - Self Organizing Migrating Algorithm - Stochastic Optimization Algorithms
"""
Arguments: current coordinates and best coordinates
Return: next stepping point
"""

def SOMA_nextStep(currentCoord, bestCoord, stepLength):
	random = random.uniform(0,1)*4
	newCoord = currentCoord

	if (bestCoord.getX() <= currentCoord.getX()): #Best coordinate is on the left side
		if (bestCoord.getY() <= currentCoord.getY()): #Best coordinate is below
			if (random < 1):
				#nothing happens
			elif (random <= 2):
				newCoord.setX(newCoord.getX() - stepLength)
			elif (random <= 3):
				newCoord.setY(newCoord.getY() - stepLength)
			else:
				newCoord.setX(newCoord.getX() - stepLength)
				newCoord.setY(newCoord.getY() - stepLength)
		else: #Best coordinate is above
			if (random < 1):
				#nothing happens
			elif (random <= 2):
				newCoord.setX(newCoord.getX() - stepLength)
			elif (random <= 3):
				newCoord.setY(newCoord.getY() + stepLength)
			else:
				newCoord.setX(newCoord.getX() - stepLength)
				newCoord.setY(newCoord.getY() + stepLength)
	else: #Best coordinate is on the right side
		if (bestCoord.getY() <= currentCoord.getY()): #Best coordinate is below
			if (random < 1):
				#nothing happens
			elif (random <= 2):
				newCoord.setX(newCoord.getX() + stepLength)
			elif (random <= 3):
				newCoord.setY(newCoord.getY() - stepLength)
			else:
				newCoord.setX(newCoord.getX() + stepLength)
				newCoord.setY(newCoord.getY() - stepLength)
		else: #Best coordinate is above
			if (random < 1):
				#nothing happens
			elif (random <= 2):
				newCoord.setX(newCoord.getX() + stepLength)
			elif (random <= 3):
				newCoord.setY(newCoord.getY() + stepLength)
			else:
				newCoord.setX(newCoord.getX() + stepLength)
				newCoord.setY(newCoord.getY() + stepLength)
	return newCoord