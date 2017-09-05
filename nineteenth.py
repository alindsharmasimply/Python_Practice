import random
a = -1
b = -1
i = 10
k=0
while i!=0 :
	while True:
		k += 1
		flip = random.randrange(0,2)
		if flip == 0:
			print "T",
		else:
			print "H",
		check = flip
		if check == b == a:
			print "(", k, "flips )"
			k = 0
			break
		a = b
		b = check
	i = i-1
