def countu(i, o):
	if i == "": return o
	elif i[0].isupper(): return countu(i[1:], o+1)
	else: return countu(i[1:], o)

print(countu(input("Type the string: "), 0))
