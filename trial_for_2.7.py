cost = 0
while True:
	age = raw_input("Enter age")
	if age == ' ':
		break;
	elif int(age) >= 3 and int(age) <=12:
		cost = cost + 14
	elif int(age) >= 65:
		cost = cost + 18
	else:
		cost = cost + 23
print "The cost for the group is " , cost