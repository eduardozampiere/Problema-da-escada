def create_table(n, array = []):
	if(len(array) <= 2):
		if n == 1: return [1]
		array = [0] * (n)
		array[0] = 1
		array[1] = 1
		for i in range(2, n):
			array[i] = array[i-1] + array[i-2]

		return array

	else:
		if n-1 < len(array):
			return array

		for i in range(len(array), n):
			array.append(array[i-1] + array[i-2])

		return array

n = int(input("Please input a int number:\nType 0 to exit "))
array = []
while(n > 0):
	array = create_table(n, array)
	print(array)
	n = int(input("Please input a int number:\nType 0 to exit "))