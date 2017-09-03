year = input("Enter a year")

if year % 400 == 0:
	pass
	print "It is a leap year"
elif year % 100 == 0:
	print "It is not a leap year"
elif year % 4 == 0:
	print "It is a leap year"
else:
	print "Its not a leap year"