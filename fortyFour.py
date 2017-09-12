def tokenising(s):
	s = s.replace(' ','')
	L = []
	for i in range(0,len(s)):
		if s[i] == '*' or s[i] == '/' or s[i] == '^' or s[i] == '(' or s[i] == ')':
			L.append(s[i])
	return L
def main():
	s = raw_input("Enter a string ")
	print tokenising(s)
main()