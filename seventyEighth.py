import string
import random


def password_generator():
    for i in range(0, 6):
        print random.choice(list(string.printable)),
    print ' '


password_generator()


def password_generator2():
    characters = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?'
    password = random.sample(characters, 6)
    password = "".join(password)
    print password


password_generator2()
