unsortedArray = [2,5,7,1,3,11,8,10,-1,4,6,9,55,0]

def sortMyArray(array):
	arrayTemp = []
	while len(array) != 0:
		i = array.index(min(array))
		arrayTemp.append(array.pop(i))
	return arrayTemp

print(sortMyArray(unsortedArray))