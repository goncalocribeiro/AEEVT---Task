#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - First DeJong Function

"""
The simplest test function is De Jong's function 1. 
It is also known as sphere model. It is continuos, convex and unimodal
"""

def deJongFirst(x):
	d = len(x)
	sum = 0
	for i in range(1,d):
		xi = x[i]
		sum = sum + xi^2
	return sum