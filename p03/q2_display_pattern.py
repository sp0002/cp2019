def display_pattern(n):
	if n>0:
		for i in range(n+1):
			if i > 0:
				for g in range(n, 0, -1):
					if g > i:
						print(" "*(len(str(g))+1), end="")
					elif g == i and g != 1:
						print("{} ".format(g), end="")
					elif g == 1:
						print("1")
					else:
						print("{} ".format(g), end="")
					
display_pattern(int(input("Enter a number: ")))