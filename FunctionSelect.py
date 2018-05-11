import deJongFirst
import deJongSecond
import schwefel

def functionSelect(func, coord):
	if func == 1:
		return deJongFirst([coord.getX(), coord.getY()])
	elif func == 2:
		return deJongSecond([coord.getX(), coord.getY()])
	elif func == 3:
		return schwefel([coord.getX(), coord.getY()])
	else:
		print("Check func param")
		return