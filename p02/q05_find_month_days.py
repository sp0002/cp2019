def isLeap(year):
	if year%4 == 0:
		if year%100 == 0:
			if year%400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False
		
def days(month, leap):
	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		return 31
	elif month == 4 or month == 6 or month == 9 or month == 11:
		return 30
	elif leap == True:
		return 29
	else:
		return 28

mon = int(input("Enter month (1-12): "))
yearIn = int(input("Enter year: "))
print("Number of days: " + str(days(mon, isLeap(yearIn))))