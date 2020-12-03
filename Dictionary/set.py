#set is a collection of non repetative elements
emp = {}  #emptydictionary not set
print(type(emp))

#empty set correct syntax
a = set()
a.add(1)
a.add(2)
a.add(3)
a.add(3)
# a.add([4,5,6])        #list can't be added into set
a.add((4,5,6))          #tuple can be added
print(a)
print(len(a))
a.remove(3)
#a.remove(7)             #throws error as 7 is not present
print(a.pop())
print(a)
print(a.union({7, 8, 9, 0}))
print(a.intersection({1, 5, 2, 7}))
a.clear()
