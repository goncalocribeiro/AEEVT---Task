#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - Second DeJong Function (Rosenbrock valley)

"""
Rosenbrocks valley is a classic optimization problem
also known as banana function or the second function of De Jong. 
The global optimum lays inside a long, narrow, parabolic shaped flat valley. 
To find the valley is trivial, however convergence to the global optimum 
is difficult and hence this problem has been frequently used to test the 
performance of optimization algorithms. Function has the following definition
"""

def deJongSecond(x):
	n = len(x)
	sum = 0
	for i in range(0,n-1):
		sum = sum + 100 * (x[i]**2 - x[i+1])**2 + (x[i]-1)**2
	return sum