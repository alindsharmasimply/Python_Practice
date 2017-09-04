
message = raw_input("Enter the message ")
shift = input("Enter the shift ")
new_message = ''
for i in range(len(message)):
	if message[i] >= 'a' and message[i] <= 'z':
		pos = ord(message[i]) + shift
		character = chr(pos)
		new_message = new_message + character
	elif message[i] >= 'A' and message[i] <= 'Z':
		pos = ord(message[i]) + shift
		character = chr(pos)
		new_message = new_message + character
if shift > 0:
	print "The encoded message is" , new_message
else :
	print "The decoded message is", new_message