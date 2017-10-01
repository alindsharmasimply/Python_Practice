def encode(l):
    index = 1
    if len(l) == 0:
        return []
    while index < len(l) and l[index] == l[index - 1]:
        index += 1
    current = [l[index - 1], index]

    return current + encode(l[index:])


def decode(l):
    index = 1
    if len(l) == 0:
        return []
    current = []
    for i in range(0, l[index]):
        current.append(l[index - 1])

    return current + decode(l[index + 1:])


def main():
    x = encode(['A', 'A', 'A', 'B', 'B', 'C', 'C'])
    print x
    y = decode(x)
    print y


main()
