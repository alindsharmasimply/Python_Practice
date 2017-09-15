import random

def diceRoll():
	d1 = random.randrange(1,7)
	d2 = random.randrange(1,7)
	return d1 + d2

def main():
	expected = {2 : 1/36, 3 : 2/36, 4 : 3/36, 5 : 4/36, 6 : 5/36, 7 : 6/36, 8 : 5/36, 9 : 4/36, 10 : 3/36, 11 : 2/36, 12 : 1/36}

	counts = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

	for i in range(1000):
	 	t = diceRoll()
	 	counts[t] = counts[t] + 1

	for i in sorted(counts.keys()):
	 	print "%5d %11.2f %8.2f" % (i, counts[i] / 1000 * 100, expected[i] * 100)
main()