def check(L):
	LL = L
	LL = LL.sort()
	if LL == L:
		print "The list is in sorted order"
	else:
		print "The list is not in sorted order"
def main():
	L = []
	while True:
		l = input("Enter a value")
		if l == 0:
			break
		L.append(l)
	check(L)
main()