def countc(i, j, o, k):
	if k > len(i)-1: return o
	elif i[k] == j: return countc(i, j, o+1, k+1)
	else: return countc(i, j, o, k+1)

print(countc(input("Type the string: "), input("Character to find: "), 0, 0))
