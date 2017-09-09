def fraction(a,b):
	mini = min(a,b)
	while a % mini != 0 or b % mini !=0:
		mini = mini - 1
	print a/mini , b/mini
def main():
	fraction(12,36)
if __name__ == '__main__':
	main()