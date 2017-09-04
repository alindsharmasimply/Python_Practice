x = 4
pi = 3.0
a , b , c = 2 , 3 , 4
print "The 1 approximation is" , pi
for i in range(1,15):
	if i % 2 == 1:
		pi = pi + (4.0 / (a*b*c) )
	else:
		pi = pi - (4.0 / (a*b*c))
	a += 2
	b += 2
	c += 2
	print "The", (i+1) , "approximation of pi is" , pi