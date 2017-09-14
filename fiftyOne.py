def reverseLookup(D , value):
	keys = []

	for key in D:
		if D[key] == value:
			keys.append(key)

	return keys
		
def main():
	D = {'k1' : 'Alind', 'k2' : 'Sagarika', 'k3' : 'Bhaskar'}
	print reverseLookup(D,'Sagarika')

main()