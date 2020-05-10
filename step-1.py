def create_table(n):
	array = [0] * (n)
	array[0] = 1
	array[1] = 1

	for i in range(2, n):
		array[i] = array[i-1] + array[i-2]

	return array;

def step(n):
	print(array[n])
print("Starting values... ")
array = create_table(100000)
print("Ok.. ")
n = input("Plese input a int number: \nTo exit type 0  ")
while(int(n) > 0):
	step(int(n)-1 )
	n = input("Plese input a int number: \nTo exit type 0  ")