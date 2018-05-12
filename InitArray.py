#GONCALO RIBEIRO - goncalocribeiro@tecnico.ulisboa.pt
#AEEVT - InitArray
import Chrom

def initArray(arraySize):
	array = [Chrom.Chrom(0,0,0)]
	for i in range(1,arraySize):
		array.append(Chrom.Chrom(0,0,0))
	return array