def countRange(L, min, max):
	count = 0
	for i in L:
		if i >= min and i<= max:
			count = count + 1
	return count
def main():
	L = []
	while True:
		c = input("Enter a value ")
		if c == 0:
			break
		L.append(c)
	cc = countRange(L, 4, 10)
	print "The number of values from 4 to 10 are ", cc
main()