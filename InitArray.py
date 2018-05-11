#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - InitArray
import Chrom

def InitArray(arraySize):
	array = [Chrom(0,0)]
	for i in range(1,arraySize):
		array.append(Chrom(0,0))
	return array