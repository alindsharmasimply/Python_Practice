import string
import os


def extractor():
    L = []
    if not os.path.exists("letters"):
        os.makedirs("letters")
    for x in string.ascii_lowercase:
        with open("letters/" + x + ".txt", "w") as fp:
            fp.write(x)
            fp.close()
    for y in string.ascii_lowercase:
        with open("letters/" + y + ".txt", "r") as fp:
            o = fp.read()
            L.append(o)
            fp.close()
    print L


extractor()
