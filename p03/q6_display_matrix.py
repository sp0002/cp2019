from random import randint
def print_matrix(n):
	for i in range(1,n+1):
		for p in range(1, n+1):
			print("{} ".format(randint(0, 1)), end="")
		print(" ")
		
print_matrix(int(input("Input number: ")))