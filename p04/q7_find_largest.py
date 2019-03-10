def find_largest(i, o):
	if i == 0: return o
	elif i[0]>o: return find_largest(i.pop(0), o=i)
	else: return find_largest(i.pop(0), o)

a = []
x = int(input("How many elements? "))
for d in range(x):
	a.append(float(input("Enter a number: ")))
print(find_largest(a, -99999.9))
