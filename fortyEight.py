def isSublist(large, small):
	d = len(large) - len(small) + 1
	s = len(small)
	
	for i in range(d):
		k = 0
		f = 1
		for j in range(i, s + i):
			if small[k] == large[j]:
				pass
			else:
				f = 0
				break;
			k += 1
		if f == 1:
			print small, "is a sublist of", large
			break
		else:
			pass
def main():
	L = [1,2,3,4,5]
	S = [3,4]
	isSublist(L,S)
main()