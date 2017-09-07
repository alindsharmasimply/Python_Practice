def caps():
	s = raw_input("Enter a string")
	s = '  ' + s
	l = len(s)
	s1 = ''
	for i in range(l):
		if s[i] == 'i' and s[i-1] == ' ' and s[i+1] == ' ':
			s1 = s1 + 'I'
		elif s[i-1] == ' ' and (s[i-2] == ',' or s[i-2] == '.' or s[i-2] == '?' or s[i-2] == '!'):
			s1 = s1 + s[i].upper()
		else:
			s1 = s1 + s[i]
	print s1
def main():
	caps()
main()