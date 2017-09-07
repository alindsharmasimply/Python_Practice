def checkPrime(a):
	f = 1
	for i in range(2,a,1):
		if a % i != 0:
			pass
		else:
			f = 0
	return f
def displayPrime(b):
	for i in range(2,b+1):
		if checkPrime(i) == 1:
			print i
