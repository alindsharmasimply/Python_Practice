def outlier(L,n):
	L.sort()

	L1 = L[3:(len(L)-1)]

	print "the list with outliers removed"
	print L1
	print "The original list"
	print L

def main():
	L = []
	while True:
		x = input("Enter a value")
		if x == 0:
			break
		L.append(x)
	outlier(L,2)
main()