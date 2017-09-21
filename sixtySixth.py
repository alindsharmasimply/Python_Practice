fp = open("test2.txt","r")

L = []
maxi = 0
for i in range(22):
	word = fp.readline()
	if maxi < len(word):
		maxi = len(word)
		L.append(word)

fp.close()
print "The longest word is ", L[-1], "with length = ", maxi
