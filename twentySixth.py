import random
def password():
	for i in range(0,7):
		print chr(random.randrange(33,127)),
def main():
	password()
if __name__ == "__main__":
	main()