def isInteger(a):
	f = 0
	a = a.strip()
	for i in range(len(a)):
		if a[0:].isdigit() == True:
			b = 0
		else:
			f = 1
	if f==1:
		print "The string is not an integer"
	else:
		print "The string is an integer"
def main():
	isInteger('  5sdf   ')
main()