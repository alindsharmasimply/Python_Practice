def sentence(g):
	L = []
	s = ''
	for i in g:
		if i == ',' or i == '.' or i == ':' or i == '"' or i == '-' or i == '.' or i == '?' or i == '!':
			pass
		elif i == ' ':
			L.append(s)
			s = ''
		else:
			s = s + i
	print L
def main():
	g = raw_input("Enter the string")
	sentence(g)
	print "Don't come to me"
if __name__ == '__main__':
	main()