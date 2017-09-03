plate = raw_input("Enter your license plate number ")

f = 0
i = 0
g = 0
plate = plate.upper()
if len(plate) == 6:
	while i<3:
		if plate[i] >= 'A' and plate[i] <= 'Z':
			f = 1
		else:
			f = 0
			break
		i += 1
	while i>=3 and i<6:
		if int(plate[i]) >= 0 and int(plate[i]) <=9:
			g = 1
		else:
			g = 0
			break
		i += 1
	if f == 1 and g == 1:
		print "The plate is older style plate"
	else:
		print "The plate is not authorised"
	i = 0
	f = 0
	g = 0
elif len(plate) == 7:
	while i<4:
		if int(plate[i]) >= 0 and int(plate[i]) <=9:
			f = 1
		else:
			f = 0
			break
		i += 1
	while i>= 4 and i < 7:
		if plate[i] >= 'A' and plate[i] <= 'Z':
			g = 1
		else:
			g = 0
			break
		i += 1
	if f == 1 and g == 1:
		print "The plate is newer style plate"
	else:
		print "The plate is not authorised"
else:
	print "the plate is not authorised"