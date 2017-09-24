import string


def conditioned_Extractor():
    L = []
    for x in string.ascii_lowercase and "python":
        with open("letters/" + x + ".txt", "r") as fp:
            o = fp.read()
            L.append(o)
            fp.close()
    print L


conditioned_Extractor()
