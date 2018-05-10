#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - Second DeJong Function

def deJongSecond(x):
	n = length(x)
	sum = 0
	for i in range(1,n-1):
		xi = xx[i]
		sum = sum + 100 * (x[i]^2 - x[i+1])^2 + (x[i]-1)^2
	return sum