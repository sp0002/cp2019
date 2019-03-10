def sum(i, o):
	if i < 1:
		return o
	else:
		return sum(i-1, o+i/(2*i+1))

print(sum(int(input("i: ")), 0))
