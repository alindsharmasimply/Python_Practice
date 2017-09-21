import sys

sys.argv = raw_input()

fp = open(sys.argv , "r")
for line in fp:
	print line,

fp.close()