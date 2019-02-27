asking = True
while asking:
	char_code = int(input("Enter ASCII code: "))
	if char_code <= 31:
		print("Unprintable! Used to control peripherals such as printers: " + chr(char_code))
	elif char_code == 127:
		print("Probably unprintable as this code represents delete: " + chr(char_code))
	elif 127 < char_code < 160:
		print("Non-standard displayable characters, may not be displayable: " + chr(char_code))
	elif char_code > 255:
		print("Not ASCII code! (probably)")
	else:
		print("Character: " + chr(char_code))
		asking = False