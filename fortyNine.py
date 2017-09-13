def eratosthenes(L):
	L[1] = 0
	p = 2
	limit = len(L) - 1
	while p < limit:
		for j in range(p*2, limit + 1, p):
			L[j] = 0

		p = p + 1

		while p < limit and L[p] == 0:
			p = p + 1
	return L

def main():
	limit = input("Enter the limit ")
	L = []
	for i in range(limit +1):
		L.append(i)
	print eratosthenes(L)

main()