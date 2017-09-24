frequency = {}


def word_frequency():
    with open("test2.txt", 'r') as fp:
        for line in fp:
            for word in line.split():
                count = frequency.get(word, 0)
                frequency[word] = count + 1
    print frequency
    print sorted(frequency.values())


word_frequency()
