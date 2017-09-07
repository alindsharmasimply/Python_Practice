listlist = [1,2,3,4,5]
print map(lambda x : x**2 + 3*x -1, listlist)
print filter(lambda x: x > 2 ,listlist)
print reduce(lambda x, y: x*y, listlist)

#Dictionaries
Dictionary = {'key1':'value1','key2':'value2'}
Dictionary['Ajju'] = 5
print Dictionary.keys()
print Dictionary.values()
Dictionary.clear()
print Dictionary.keys()
print Dictionary.values()
