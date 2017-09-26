def users(s):
    with open("users.txt", "r") as fp:
        users = fp.readlines()
        users = [i.strip("\n") for i in users]
        if s in users:
            print "Username exists."
        else:
            print "Username is fine."
        fp.close()


def username():
    s = raw_input("Enter username ")
    users(s)


username()
