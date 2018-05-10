#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - First DeJong Function

def deJongFirst(x):
	d = length(x)
	sum = 0
	for i in range(1,d):
		xi = x[i]
		sum = sum + xi^2
	return sum