def isPrime(n):
	if n == 2:
		return True
	elif n%2 == 0:
		return False
	else:
		import math
		for d in range(3, int(math.sqrt(n))+1, 2):
			if n % d == 0:
				return False
		return True

looping = True
while looping:
	num = int(input("Enter whole number: "))
	if num < 0:
		print("Number < 0!")
	elif num >= 0:
		looping = False
		
if num == 0:
	print("No factors of 0.")
elif num == 1:
	print("Factor of 1 is 1 itself.")
else:
	looping = True
	print("Prime factors of {}: ".format(num), end="")
	i = 2
	while looping:
		if isPrime(i):
			if num > i:
				if num % i == 0:
					print("{}, ".format(i), end="")
					num = (num/i)
				else:
					i+=1
			else: 
				looping = False
				print("{}".format(i), end="")
				print(".")
		else: i+=1