import random
count = 0
max = 0
for i in range(1,101):
	n = random.randrange(1,101)
	if max < n:
		max = n
		print n
	elif max == n:
		max = n
		print n, "=> Updated"
		count += 1
	else:
		print n
print "The maximum value is", max
print "The number of times it got updated is", count