s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))

if (s1 + s2) > s3 and (s1 + s3) > s2 and (s2 + s3) > s1:
	print("Perimeter = {}".format((s1 + s2 + s3)))
else:
	print("Invalid triangle!")