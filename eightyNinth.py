def endless():
    while True:
        with open("everything.txt", "a+") as fp:
            a = raw_input("Enter a value ")
            if not a == 'CLOSE':
                fp.write(a + '\n')
            else:
                break
                fp.close()


endless()
