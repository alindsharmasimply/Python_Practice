def pigLatin(s):
	s1 = ''
	i = 1
	if s[0] not in ['a','e','i','o','u']:
		while True:
			if s[i] not in ['a','e','i','o','u']:
				s1 = s1 + s[i]
			else:
				s = s + s1 + 'ay'
				break
			i += 1
		s = s[len(s1)+1:]
	else:
		s = s + 'way'
	return s
def main():
	d = raw_input("Enter the string for encoding ")
	s = pigLatin(d)
	print s
main()