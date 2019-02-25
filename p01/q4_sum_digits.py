running = True
while running:
    num = str(input("Type a number between 0 and 1000: "))
    sum = 0
    if int(num) < 1001:
        for i in range(len(num)):
            sum += int(num[i])
        print("Sum of digits is: " + str(sum) + ".")
        running = False
    else:
        print("Number not between 0 and 1000!")
