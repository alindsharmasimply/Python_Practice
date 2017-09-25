import json
import time
from pprint import *


def fullName():
    a = raw_input("Enter your first name ")
    b = raw_input("Enter your surname ")
    print "The first name is %s and the last name is %s " % (a, b)


# Imp 1


d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}


d["employees"].append(dict({"firstName": 'Alind', "lastName": 'Sharma'}))
# print d["employees"]
# Imp2


def json_file():
    with open("company.json", "w") as fp:
        json.dump(d, fp)
        fp.close()


# Imp 3


def json_to_dictionary():
    with open("company1.json", "r+") as fp:
        x = json.loads(fp.read())
        x["employees"].append(dict({"lastName": "Sharma", "firstName": "Alind"}))
        fp.seek(0)
        json.dump(x, fp, indent=4)
        fp.close()


# Imp 4


def enumeration():
    a = [1, 2, 3]
    for index, item in enumerate(a):
        print "Item %d has index %d " % (item, index)


# Imp 5

def infinitely():
    for i in range(10):
        time.sleep(i)
        print "Hello"


# Imp 6


def translator():
    a = raw_input("Enter your word ")
    d = dict(weather="clima", earth="terra", rain="chuva")
    print d[a]


# Imp 7

def advanced_translator():
    a = raw_input("Enter your word ")
    a = a.lower()
    d = dict(weather="clima", earth="terra", rain="chuva")
    try:
        print d[a]
    except Exception as e:
        print "Your word can't be found"


advanced_translator()
# Imp 8
