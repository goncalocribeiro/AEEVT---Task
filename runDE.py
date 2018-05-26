#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - RUN DE ALGORITHM

import DE
import statistics
import matplotlib.pyplot as plt

maxIt = 30

#------------------------------------------------------------------------------------ First DeJong Function
deDeJongFirstSolutions = []
deDeJongFirstBestOfEach = []

#Generate solution vector 30 times
for i in range(maxIt):
	#print(i)
	sResult = DE.de(1)
	deDeJongFirstSolutions.append(sResult)
	deDeJongFirstBestOfEach.append(sResult[DE.bestChrom])
	DE.bestChrom = 1

#Get data from the 30 best solutions
min_deDeJongFirstBestOfEach = min(deDeJongFirstBestOfEach)
max_deDeJongFirstBestOfEach = max(deDeJongFirstBestOfEach)
mean_deDeJongFirstBestOfEach = sum(deDeJongFirstBestOfEach) / len(deDeJongFirstBestOfEach)
median_deDeJongFirstBestOfEach = statistics.median(deDeJongFirstBestOfEach)
stDev_deDeJongFirstBestOfEach = statistics.stdev(deDeJongFirstBestOfEach)

#Sorting solutions
for i in range(len(deDeJongFirstSolutions)):
	deDeJongFirstSolutions[i].sort(reverse=True) 

#Plot each of the 30 solutions
plt.title('Convergence of First DeJong function')
plt.xlabel('Generation')
plt.ylabel('Cost Value')
for i in range(len(deDeJongFirstSolutions)):
	plt.plot(deDeJongFirstSolutions[i])
plt.show()


print("MIN: " + str(min_deDeJongFirstBestOfEach))
print("MAX: " + str(max_deDeJongFirstBestOfEach))
print("MEAN: " + str(mean_deDeJongFirstBestOfEach))
print("MEDIAN: " + str(median_deDeJongFirstBestOfEach))
print("StDEV: " + str(stDev_deDeJongFirstBestOfEach))
  
"""for j in range(maxIt):
  print("################## SOLUTIONS #######################")
  print(deDeJongFirstSolutions[j])
  print("***** BEST OF THEM ******")
  print(deDeJongFirstBestOfEach[j])"""
  
#------------------------------------------------------------------------------------ Second DeJong Function
deDeJongSecondSolutions = []
deDeJongSecondBestOfEach = []

#Generate solution vector 30 times
for i in range(maxIt):
	#print(i)
	sResult = DE.de(2)
	deDeJongSecondSolutions.append(sResult)
	deDeJongSecondBestOfEach.append(sResult[DE.bestChrom])
	DE.bestChrom = 1

#Get data from the 30 best solutions
min_deDeJongSecondBestOfEach = min(deDeJongSecondBestOfEach)
max_deDeJongSecondBestOfEach = max(deDeJongSecondBestOfEach)
mean_deDeJongSecondBestOfEach = sum(deDeJongSecondBestOfEach) / len(deDeJongSecondBestOfEach)
median_deDeJongSecondBestOfEach = statistics.median(deDeJongSecondBestOfEach)
stDev_deDeJongSecondBestOfEach = statistics.stdev(deDeJongSecondBestOfEach)

#Sorting solutions
for i in range(len(deDeJongSecondSolutions)):
	deDeJongSecondSolutions[i].sort(reverse=True) 

#Plot each of the 30 solutions
plt.title('Convergence of Second DeJong function')
plt.xlabel('Generation')
plt.ylabel('Cost Value')
for i in range(len(deDeJongSecondSolutions)):
	plt.plot(deDeJongSecondSolutions[i])
plt.show()

print("MIN: " + str(min_deDeJongSecondBestOfEach))
print("MAX: " + str(max_deDeJongSecondBestOfEach))
print("MEAN: " + str(mean_deDeJongSecondBestOfEach))
print("MEDIAN: " + str(median_deDeJongSecondBestOfEach))
print("StDEV: " + str(stDev_deDeJongSecondBestOfEach))

"""for j in range(maxIt):
  print("################## SOLUTIONS #######################")
  print(deDeJongSecondSolutions[j])
  print("***** BEST OF THEM ******")
  print(deDeJongSecondBestOfEach[j])"""

#------------------------------------------------------------------------------------ Schwefel Function
schwefelSolutions = []
schwefelBestOfEach = []

#Generate solution vector 30 times
for i in range(maxIt):
	print(i)
	sResult = DE.de(3)
	schwefelSolutions.append(sResult)
	schwefelBestOfEach.append(sResult[DE.bestChrom])

#Get data from the 30 best solutions
min_schwefelBestOfEach = min(schwefelBestOfEach)
max_schwefelBestOfEach = max(schwefelBestOfEach)
mean_schwefelBestOfEach = sum(schwefelBestOfEach) / len(schwefelBestOfEach)
median_schwefelBestOfEach = statistics.median(schwefelBestOfEach)
stDev_schwefelBestOfEach = statistics.stdev(schwefelBestOfEach)

#Sorting solutions
for i in range(len(schwefelSolutions)):
	schwefelSolutions[i].sort(reverse=True)

#Plot each of the 30 solutions
plt.title('Convergence of Schwefel function')
plt.xlabel('Generation')
plt.ylabel('Cost Value')
for i in range(len(schwefelSolutions)):
	plt.plot(schwefelSolutions[i])
plt.show()

print("MIN: " + str(min_schwefelBestOfEach))
print("MAX: " + str(max_schwefelBestOfEach))
print("MEAN: " + str(mean_schwefelBestOfEach))
print("MEDIAN: " + str(median_schwefelBestOfEach))
print("StDEV: " + str(stDev_schwefelBestOfEach))

"""for j in range(maxIt):
  print("################## SOLUTIONS #######################")
  print(schwefelSolutions[j])
  print("***** BEST OF THEM ******")
  print(schwefelBestOfEach[j])"""