def sumd(i, o):
	if i == '': return o
	else:
		return sumd(i[1:], o+int(i[0]))

print(sumd((input("Enter an interger: ")), 0))
