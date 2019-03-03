print("Miles Kilometers Kilometres Miles")
for i in range(10):
	print(str(i+1) + (" "*(6-len(str(i+1)))) + "{:.3f}".format(round(((i+1)*1.60934), 3)) + 
	(" "*(11-len(str(round(((i+1)*1.60934), 3))))) + str(i*5+20) + 
	(" "*(11-len(str(i*5+20))) + "{:.3f}".format(round((i*5+20)/1.60934, 3))))