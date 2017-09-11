import random

def lottery():
	L = []
	for i in range(0,6):
		n = random.randrange(1,50)
		L.append(n)
	return L
def main():
	L = lottery()
	L.sort()
	print L
main()