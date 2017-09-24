def sumsum():

    sum1 = 0
    while True:
        try:
            a = input("Enter a valid number to get the sum ")
            if a == ' ':
                break
            sum1 = sum1 + a
            print sum1, "\n"
        except Exception:
            print "Enter a valid number only "


sumsum()
