print "Enter a list of numbers "
sum = 0
i = 0
while True:
	n = input()
	if n == 0:
		break
	sum = sum + n 
	i += 1
average = sum/i
print average