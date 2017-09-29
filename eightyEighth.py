def enteredValues():
    val = raw_input('Enter some values ')
    L = []
    val = val.replace(" ", "")
    L = val.split(',')
    with open("entered_values.txt", "w") as fp:
        for i in L:
            fp.write(i + "\n")
        fp.close()


enteredValues()
