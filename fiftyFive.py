def anagram(s1, s2):
	l1 = len(s1)
	character = {}
	for i in s1:
		character[i] = True
	for j in s2:
		if j not in character:
			f = 0
			print "Not an anagram"
		else:
			f = 1
	if f == 1:
		print "Strings are anagram"

def main():
	anagram("live", "evil")
main()