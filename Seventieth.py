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


def homologous_sum():
    a = [1, 2, 3]
    b = (3, 6, 9)
    for i, j in zip(a, b):
        print i + j


homologous_sum()
# Imp 7


def two_by_two():
    with open("two_by_two.txt", "w") as fp:
        for x, y, z in zip(string.ascii_lowercase[::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3]):
            fp.write(x + y + z + '\n')
        fp.close()

    with open("two_by_two.txt", "r") as fp:
        print fp.read()
        fp.close()


two_by_two()
# Imp 8
