from fractions import Fraction
def convert_ms(n):
	sec = Fraction(n, 1000)
	min = int(sec/60)
	hour = int(min/60)
	sec = sec % 60
	min = min % 60
	return str(round(hour, 0)) + ":" + str(round(min, 0)) + ":" + str(round(sec, 0))
	
print(convert_ms(int(input("Enter milliseconds: "))))