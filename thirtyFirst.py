def blank():
	L = []
	while True:
		
		s = raw_input("Enter the string ")
		if s == ' ':
			break
		if s not in L:
			L.append(s)
	print L
def main():
	blank()
main()