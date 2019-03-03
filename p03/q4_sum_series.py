from fractions import Fraction
def m_series(i):
	num = 0.0
	temp_num = i
	while temp_num > 1:
		num += Fraction(temp_num, (temp_num+1))
		temp_num -= 1
	num += Fraction(1, 2)
	return num
	
for x in range(1,21):
	print("{:<10}{:.4f}".format(x, m_series(x)))