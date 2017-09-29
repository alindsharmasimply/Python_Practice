def add_missing():
    L = ["Portugal", "Germany", "Spain"]
    with open("countries-missing.txt", "r") as fp:
        lines = fp.readlines()
        content = [i + '\n' for i in L]
        fp.close()

    updated_list = sorted(content + lines)

    with open("countries-updated.txt", "w") as fp:
        for i in updated_list:
            fp.write(i)
        fp.close()


add_missing()
