import random

value = random.randrange(0,38)

if value == 37:
	pass
	print "The spin resulted in 00"
else:
	print "The spin resulted in" , value

if value == 37:
	pass
	print "Pay 00"
else:
	print "Print", value

if value % 2 != 0 and value >= 1 and value <= 9 or\
	value % 2 == 0 and value >= 12 and value <= 18 or\
	value % 2 != 0 and value >= 19 and value <= 27 or\
	value % 2 == 0 and value >= 30 and value <= 36:
	pass
	print "Pay Red"
elif value == 0 or value == 37:
	pass
else:
	print "Pay Black"

if value >= 1 and value <= 36:
	pass
	if value % 2 ==0:
		pass
		print "Pay Even"
	else:
		print "Pay Odd"

if value >= 1 and value <= 18:
	pass
	print "Pay 1 to 18"
elif value >= 19 and value <= 36:
	print "Pay 19 to 36"