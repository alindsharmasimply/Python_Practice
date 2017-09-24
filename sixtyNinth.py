
from collections import OrderedDict
import string

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
myList = range(1, 21)
print list(myList)
# Imp 1

myList2 = range(10, 201, 10)
print list(map(str, myList2))
# Imp 2

myList3 = [1, 3, 3, 4, 5, 6, 6]
print list(OrderedDict.fromkeys(myList3))
# Imp 3

d = {"a": 1, "b": 2, "c": 3}
print sum(d.values())
# Imp 4

d = dict((key, value) for key, value in d.iteritems() if value <= 2)
print d
# Imp 5

d = {"a": range(1, 11), "b": range(1, 11), "c": range(1, 11)}
print d.values()
# Imp 6

for x in string.ascii_lowercase:
    print x
# Imp 7
