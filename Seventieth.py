import math
import string


def foo():
    global c
    c = 2
    return c


foo()
print c
# Imp 1


def words(s):
    s = s.split(' ')
    print len(s)


words("Hello world people")
# Imp 2


def word_count():
    with open("words1.txt", "r") as fp:
        s = fp.read()
        fp.close()
        s = s.split()

    return len(s)


print word_count()
# Imp 3


def word_count2():
    with open("words2.txt", "r") as fp:
        s = fp.read()
        s = s.replace(',', ' ')
        s = s.split()
        return len(s)


print word_count2()
# Imp 4


def cosine_value():
    return math.cos(34)


print cosine_value()
# Imp 5


def write_letters():
    with open("tt.txt", "w") as fp:
        for x in string.ascii_lowercase:
            fp.write(x + "\n")
        fp.close()
    with open("tt.txt", "r") as fp:
        print fp.read()
        fp.close()


write_letters()
# Imp 6
