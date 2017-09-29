def URL_cleaner():
    with open("urls.txt", "r") as fp:
        with open("urls_cleaned.txt", "w") as fpp:
            r = fp.readlines()
            for i in r:
                i = i.replace("s", "", 1)
                i = i[:6] + "/" + i[6:]
                fpp.write(i)
            fpp.close()
            fp.close()


URL_cleaner()
