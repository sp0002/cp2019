running = True
while running:
	mark = int(input("Enter score: "))
	if 0 < mark <= 100:
		if 70 <= mark <= 100:
			print("Grade A!")
			running = False
		elif 60 <= mark <= 69:
			print("Grade B!")
			running = False
		elif 55 <= mark <= 59:
			print("Grade C.")
			running = False
		elif 50 <= mark <= 54:
			print("Grade D.")
			running = False
		elif 45 <= mark <= 49:
			print("Grade E.")
			running = False
		elif 35 <= mark <= 44:
			print("Grade S.  :(")
			running = False
		elif 0 <= mark <= 34:
			print("Grade U.  :(")
			running = False
	else:
		print("Invalid! Score must be within 0-100.")