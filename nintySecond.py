count = 0


def six_vowels():
    global count
    i = input("Enter value ")
    if i == 0:
        return
    else:
        count = count + i
        six_vowels()


six_vowels()
print "The sum is = ", count
