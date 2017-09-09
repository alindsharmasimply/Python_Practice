def perfect(n):
	sum = 0
	for i in range(1,n):
		if n%i == 0:
			sum = sum + i
	if sum == n:
		print "The number", n, "is a perfect number"
def main():
	for i in range(1,10001):
		perfect(i)
if __name__ == '__main__':
	main()