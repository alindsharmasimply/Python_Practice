while True:
	signal = raw_input("Enter the 8-bit string ")
	if signal == ' ':
		break
	else:
		length = signal.count('1')
		if length % 2 == 0:
			print "Parity bit would be 0"
		else:
			print "Parity bit would be 1"