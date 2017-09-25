import random


def password():
    L = []
    with open("words2.txt", "r") as fp:
        s = fp.read()
        L = s.split()
        fp.close()
    print random.choice(L) + random.choice(L)


password()
