fp = open("test1.txt", "w")
fp.write("This is so cool. ")
fp.close()

fp = open("test1.txt", "r")
print fp.read()
fp.close()

fp = open("test1.txt", "a")
print fp.write("This is some new content.")
fp.close()

fp = open("test1.txt", "r")
print fp.read()
fp.close()