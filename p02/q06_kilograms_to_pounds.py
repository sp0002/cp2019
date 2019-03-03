print("Kilograms Pounds")
for i in range(10):
	print(str(i+1) + (" "*(10-len(str(i+1)))) + "{:.1f}".format((i+1)*2.2))