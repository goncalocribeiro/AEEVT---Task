#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - RUN SOMA ALGORITHM

import SOMA
import statistics

maxIt = 30

#First DeJong Function
somaDeJongFirstSolutions = []
somaDeJongFirstBestOfEach = []
for i in range(maxIt):
  sResult = SOMA.soma(1)
  somaDeJongFirstSolutions.append(sResult)
  somaDeJongFirstBestOfEach.append(sResult[SOMA.bestChrom])
  SOMA.bestChrom = 1

min_somaDeJongFirstBestOfEach = min(somaDeJongFirstBestOfEach)
max_somaDeJongFirstBestOfEach = max(somaDeJongFirstBestOfEach)
mean_somaDeJongFirstBestOfEach = sum(somaDeJongFirstBestOfEach) / len(somaDeJongFirstBestOfEach)
median_somaDeJongFirstBestOfEach = statistics.median(somaDeJongFirstBestOfEach)
stDev_somaDeJongFirstBestOfEach = statistics.stdev(somaDeJongFirstBestOfEach)

print(somaDeJongFirstBestOfEach)
print("MIN: " + str(min_somaDeJongFirstBestOfEach))
print("MAX: " + str(max_somaDeJongFirstBestOfEach))
print("MEAN: " + str(mean_somaDeJongFirstBestOfEach))
print("MEDIAN: " + str(median_somaDeJongFirstBestOfEach))
print("StDEV: " + str(stDev_somaDeJongFirstBestOfEach))
  
"""for j in range(maxIt):
  print("################## SOLUTIONS #######################")
  print(somaDeJongFirstSolutions[j])
  print("***** BEST OF THEM ******")
  print(somaDeJongFirstBestOfEach[j])"""
  
#Second DeJong Function
somaDeJongSecondSolutions = []
somaDeJongSecondBestOfEach = []
for i in range(maxIt):
  sResult = SOMA.soma(2)
  somaDeJongSecondSolutions.append(sResult)
  somaDeJongSecondBestOfEach.append(sResult[SOMA.bestChrom])
  SOMA.bestChrom = 1
  
min_somaDeJongSecondBestOfEach = min(somaDeJongSecondBestOfEach)
max_somaDeJongSecondBestOfEach = max(somaDeJongSecondBestOfEach)
mean_somaDeJongSecondBestOfEach = sum(somaDeJongSecondBestOfEach) / len(somaDeJongSecondBestOfEach)
median_somaDeJongSecondBestOfEach = statistics.median(somaDeJongSecondBestOfEach)
stDev_somaDeJongSecondBestOfEach = statistics.stdev(somaDeJongSecondBestOfEach)

print(somaDeJongFirstBestOfEach)
print("MIN: " + str(min_somaDeJongSecondBestOfEach))
print("MAX: " + str(max_somaDeJongSecondBestOfEach))
print("MEAN: " + str(mean_somaDeJongSecondBestOfEach))
print("MEDIAN: " + str(median_somaDeJongSecondBestOfEach))
print("StDEV: " + str(stDev_somaDeJongSecondBestOfEach))

"""for j in range(maxIt):
  print("################## SOLUTIONS #######################")
  print(somaDeJongSecondSolutions[j])
  print("***** BEST OF THEM ******")
  print(somaDeJongSecondBestOfEach[j])"""

#Schwefel Function
schwefelSolutions = []
schwefelBestOfEach = []
for i in range(maxIt):
  sResult = SOMA.soma(3)
  schwefelSolutions.append(sResult)
  schwefelBestOfEach.append(sResult[SOMA.bestChrom])
  SOMA.bestChrom = 1
  
min_schwefelBestOfEach = min(schwefelBestOfEach)
max_schwefelBestOfEach = max(schwefelBestOfEach)
mean_schwefelBestOfEach = sum(schwefelBestOfEach) / len(schwefelBestOfEach)
median_schwefelBestOfEach = statistics.median(schwefelBestOfEach)
stDev_schwefelBestOfEach = statistics.stdev(schwefelBestOfEach)

print(schwefelBestOfEach)
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