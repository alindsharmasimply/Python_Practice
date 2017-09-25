import requests

r = requests.get("http://www.pythonhow.com/data/universe.txt")
t = r.text[:]
print t

print t.count('a')

