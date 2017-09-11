import random
def createDeck():
	L = []
	for i in ['s','c','d','h']:
		for j in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
			L.append(i + j)
	return L
def shuffle():
	L = createDeck()
	print L
	i = 0
	while i<52:
		
		pos = random.randrange(0,52)
		temp = L[pos]
		L[pos] = L[i]
		L[i] = temp
		i += 1
	print L
shuffle()