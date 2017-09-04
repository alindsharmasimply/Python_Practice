s = raw_input("Enter a string ")
reverse = ''
for i in range(len(s)-1,-1,-1):
	reverse = reverse + s[i]
if s == reverse:
	print "The string is a palindrome"
else:
	print "The string is not a palindrome"