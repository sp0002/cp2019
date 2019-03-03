looping = True
while looping:
	n1 = int(input("Enter first positive whole number: "))
	n2 = int(input("Enter second positive whole number: "))
	if n1 <= 0:
		print("Number must be more than 0!")
	elif n2 <= 0:
		print("Number must be more than 0!")
	else:
		looping = False

def findgcd(a,b):
	while b:
		a, b = b, a%b
	return a
	
print(findgcd(max(n1, n2), min(n1, n2)))