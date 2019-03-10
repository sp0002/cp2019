def reverse_int(i, o, k):
	if k > len(i):
		return o
	else:
		return reverse_int(i, o+i[-k], k+1)

print(reverse_int(input("Number to reverse: "), "", 1))
