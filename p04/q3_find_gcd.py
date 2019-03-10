def findgcd(a,b):
	while b:
		return findgcd(b, a%b)
	return a

print(findgcd(24, 16))
print(findgcd(255, 25))
