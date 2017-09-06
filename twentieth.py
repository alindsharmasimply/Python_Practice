def median(a, b, c):
	maxi = max(a,b,c)
	mini = min(a,b,c)
	return (a+b+c) - maxi - mini
def main():
	x, y, z = float(input("Enter the value")), float(input("Enter the value")), float(input("Enter the value"))
	print median(x, y, z)

main()