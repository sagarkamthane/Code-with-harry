# tuple : tuple is immutable data type in python (can not change values)

t = (1, 5, 8, 6, 3 , 9, 1, 1, 1)
print(t)

# t[0] = 10   #assignment not supported in tuples
print(t[0])

tu = (1) #wrong way to declare signleton tuple
tu = (1, )  #right way to declare signleton tuple
print(tu[0])

print(t.count(1))  #prints count of 1
print(t.index(8))  #prints index of 8
