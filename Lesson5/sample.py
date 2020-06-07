from collections import ChainMap

x =  ChainMap()
print(x)

s = input('Ввидите имя: ')
y = x.new_child({'name' : s})
print(y)
print(y['name'])
