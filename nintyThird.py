s = ''


def decToBinary(a):
    global s
    if a == 0:
        return
    r = a % 2
    s = str(r) + s
    decToBinary(a // 2)


def main():
    a = input("Enter the number ")
    decToBinary(a)
    print s


main()
