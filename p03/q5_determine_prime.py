def is_prime(n):
	if n == 2:
		return True
	elif n%2 == 0 or n <= 1:
		return False
	else:
		import math
		for d in range(3, int(math.sqrt(n))+1, 2):
			if n % d == 0:
				return False
		return True

looping = True
e = 2
nth = 1
while looping:
	if nth < 1001:
		if is_prime(e):
			if nth % 10 == 0:
				print(e)
				nth += 1
				e += 1
			else:
				print("{}".format(e)+" "*(5-len(str(e))), end="")
				nth += 1
				e += 1
		else:
			e += 1
	else:
		looping = False
