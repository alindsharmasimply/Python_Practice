def data_checker():
    L = ["Portugal", "Germany", "Munster", "Spain"]
    x = []
    for i in L:
        with open("countries-clean.txt", "r") as fp:
            lines = fp.readlines()
            fp.close()
        content = [j.rstrip('\n') for j in lines]
        if i not in content:
            pass
        else:
            x.append(i)
    print x


print data_checker()
