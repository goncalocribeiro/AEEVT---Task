#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - First DeJong Function

def deJongFirst(xx):
	d = length(xx)
	sum = 0
	for i in range(1,d):
		xi = xx[i]
		sum = sum + xi^2
	return sum