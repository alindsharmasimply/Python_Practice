L = []

while True:
		
	n = input("Enter a value")
	if n == 0:
		break;
	L = L + [n]
L.sort()
print L
L.reverse()
print L