def findgcd(a,b):
	while b:
		a, b = b, a%b
	return a

print(findgcd(24, 16))
print(findgcd(255, 25))