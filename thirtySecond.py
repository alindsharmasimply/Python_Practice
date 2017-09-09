def intdup(n):
	L = []
	for i in range(2,n):
		if  n % i == 0:
			L.append(i)
	print "The divisors of", n, "are ="
	print L
def main():
	n = input("Enter a value ")
	intdup(n)
if __name__ == '__main__':
	main()