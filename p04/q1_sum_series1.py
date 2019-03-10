def sum(i, o):
	if i < 1:
		return o
	else:
		return sum(i-1, o+1/i)

print(sum(int(input("i: ")), 0))
