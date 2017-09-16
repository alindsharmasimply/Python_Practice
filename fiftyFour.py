def unique(s):
	character = {}

	for i in s:
		character[i] = True

	print "The number of unique characters is ", len(character)

def main():
	unique("Hello World")

main()