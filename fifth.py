pos = raw_input("Enter position")
if pos[0] == 'a' or pos[0] == 'c' or pos[0] == 'e' or pos[0] == 'g' :
	if int(pos[1]) % 2 != 0:
		print "Its a black square"
	else:
		print "Its a white square"
elif pos[0] == 'b' or pos[0] == 'd' or pos[0] == 'f' or pos[0] == 'h':
	if int(pos[1]) % 2 != 0:
		print "Its a whhite square"
	else:
		print "Its a black square"